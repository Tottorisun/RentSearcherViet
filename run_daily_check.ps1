param(
    [string]$PromptFile = "daily_hcmc_check_prompt.txt",
    [string]$LogPrefix = "hcmc"
)

$ErrorActionPreference = "Stop"
[Console]::OutputEncoding = [System.Text.Encoding]::UTF8
$OutputEncoding = [System.Text.Encoding]::UTF8

$root = $PSScriptRoot
Set-Location $root

$logDir = Join-Path $root "daily_check_logs"
if (-not (Test-Path $logDir)) { New-Item -ItemType Directory -Path $logDir | Out-Null }

$stamp = Get-Date -Format "yyyy-MM-dd_HHmmss"
$logFile = Join-Path $logDir "${LogPrefix}_check_$stamp.log"

try {
    $promptFile = Join-Path $root $PromptFile
    $prompt = Get-Content -LiteralPath $promptFile -Raw -Encoding UTF8
    if (-not $prompt) { throw "Prompt file was empty or unreadable: $promptFile" }

    $claudeExe = "$env:USERPROFILE\.local\bin\claude.exe"
    # Stream every line to the console AND append it to the log as UTF-8.
    # Tee-Object on this PowerShell build has no -Encoding parameter and wrote
    # UTF-16LE, which `cat`/`grep`/Python-by-default cannot read (2 Sep 2026
    # audit); Add-Content -Encoding UTF8 keeps the live streaming, so partial
    # output still survives a kill/timeout.
    $prompt | & $claudeExe -p --permission-mode dontAsk *>&1 | ForEach-Object {
        $_
        Add-Content -LiteralPath $logFile -Value ([string]$_) -Encoding UTF8
    }
    # A pipeline doesn't throw on its own -- claude.exe can fail (e.g. expired auth)
    # while this script still reaches here and would otherwise report success.
    if ($LASTEXITCODE -ne 0) {
        $msg = "SCRIPT ERROR: claude.exe exited with code $LASTEXITCODE -- see output above (often an auth/session problem, run 'claude auth status' to check)."
        $msg; Add-Content -LiteralPath $logFile -Value $msg -Encoding UTF8
        exit 1
    }
}
catch {
    $err = ($_ | Out-String)
    $err; Add-Content -LiteralPath $logFile -Value $err -Encoding UTF8
    $msg = "SCRIPT ERROR: $($_.Exception.Message)"
    $msg; Add-Content -LiteralPath $logFile -Value $msg -Encoding UTF8
    exit 1
}
