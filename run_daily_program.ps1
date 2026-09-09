param(
    # Оставлены ради совместимости с launcher.ps1, который зовёт скрипты проекта
    # с этими параметрами. Программе они не нужны: суточный цикл один на все
    # города, деления на hcmc/othercities больше нет.
    [string]$PromptFile = "",
    [string]$LogPrefix = "pipeline",
    [switch]$NoPublish
)

# Суточный прогон ПРОГРАММОЙ, а не сессией модели.
#
# ЗАЧЕМ ЭТОТ ФАЙЛ ОТДЕЛЬНО ОТ run_daily_check.ps1. Тот запускает
# `$prompt | claude.exe -p`, то есть каждый прогон зависит от того, дошла ли
# сессия до конца и не истёк ли вход. run_pipeline.py делает то же самое кодом:
# сбор с Chợ Tốt по девяти городам, dotproperty, кандидаты Telegram,
# обслуживание, карта, сборка и публикация. Он сам ведёт лог, сам берёт замок и
# сам пишет владельцу, если фатальный шаг не прошёл.
#
# Здесь остаётся ровно то, чего программа о себе знать не может: не запустился
# сам python. В этом случае лог пуст и оповестить некому -- поэтому обёртка.

$ErrorActionPreference = "Stop"
[Console]::OutputEncoding = [System.Text.Encoding]::UTF8
$OutputEncoding = [System.Text.Encoding]::UTF8

$root = $PSScriptRoot
Set-Location $root
$logDir = Join-Path $root "daily_check_logs"
if (-not (Test-Path $logDir)) { New-Item -ItemType Directory -Path $logDir | Out-Null }
$stamp = Get-Date -Format "yyyy-MM-dd_HHmmss"
$logFile = Join-Path $logDir "${LogPrefix}_wrapper_$stamp.log"

function Say-Owner {
    param([string]$Text)
    try {
        $say = 'D:\MyDev\AI_CONTEXT\TASKS\gelios_say.py'
        if (-not (Test-Path -LiteralPath $say)) { return "нет $say" }
        return (& python $say $Text) -join ' '
    } catch { return "оповестить не удалось: $($_.Exception.Message)" }
}

try {
    $args = @("run_pipeline.py")
    if (-not $NoPublish) { $args += "--publish" }

    "[$stamp] запуск: python $($args -join ' ')" | Add-Content -LiteralPath $logFile -Encoding UTF8
    & python @args *>&1 | ForEach-Object {
        $_
        Add-Content -LiteralPath $logFile -Value ([string]$_) -Encoding UTF8
    }
    $code = $LASTEXITCODE

    if ($code -ne 0) {
        # Про фатальный шаг владельцу уже написал сам run_pipeline.py -- второй
        # раз о том же не пишем, чтобы одна беда не приходила дважды.
        $msg = "run_pipeline.py вернул код $code -- подробности в daily_check_logs"
        $msg; Add-Content -LiteralPath $logFile -Value $msg -Encoding UTF8
        exit $code
    }
    "готово" | Add-Content -LiteralPath $logFile -Encoding UTF8
}
catch {
    # Сюда попадаем, когда не стартовал сам python: программа ничего не написала
    # и написать не могла.
    $err = ($_ | Out-String)
    $err; Add-Content -LiteralPath $logFile -Value $err -Encoding UTF8
    Say-Owner "RentSearcher: суточный прогон не запустился вовсе ($($_.Exception.Message)). Программа не стартовала, лог пуст."
    exit 1
}
