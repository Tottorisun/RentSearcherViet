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
#
# ЗАДАЧА ПЛАНИРОВЩИКА ЗОВЁТ ЭТОТ ФАЙЛ НАПРЯМУЮ, минуя
# C:\Users\User\.rent-searcher-scheduler\launcher.ps1. Тот читал путь к проекту
# из project_path.txt, а там до сих пор лежит прежнее имя папки
# «D:\Мои разработки\Rent Searcher». После переименования каждый запуск по
# расписанию умирал на этой строке, не написав ни одной строки лога: 10 сентября
# 2026 задача отработала в 11:12 с кодом 1, и понять это можно было только из
# launcher_crash.log. Косвенность, которую никто не обновляет, -- это не гибкость,
# а лишняя деталь, способная сломаться молча. Путь к проекту теперь стоит прямо
# в действии задачи.

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
    # С 11 сентября 2026 сайт собирает и публикует СЕРВЕР (Netcup, таймер
    # rentsearcher-pipeline.timer, 05:00 и 17:00 по Вьетнаму): компьютер ночью
    # выключен. Здесь остаётся то, что может только этот ПК: группы Facebook (вход
    # в личный аккаунт владельца с адреса дата-центра грозит блокировкой) и каналы
    # Telegram (их кандидатов разбирает сессия здесь же). --publish отсюда больше
    # не передаётся: два публикующих прогона столкнулись бы на пуше.
    $args = @("run_pipeline.py", "--candidates-only")

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
