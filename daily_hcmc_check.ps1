$ErrorActionPreference = "Stop"
[Console]::OutputEncoding = [System.Text.Encoding]::UTF8
$OutputEncoding = [System.Text.Encoding]::UTF8

$root = $PSScriptRoot
Set-Location $root

$logDir = Join-Path $root "daily_check_logs"
if (-not (Test-Path $logDir)) { New-Item -ItemType Directory -Path $logDir | Out-Null }

$stamp = Get-Date -Format "yyyy-MM-dd_HHmmss"
$logFile = Join-Path $logDir "check_$stamp.log"

try {
    $promptFile = Join-Path $root "daily_hcmc_check_prompt.txt"
    $prompt = Get-Content -LiteralPath $promptFile -Raw -Encoding UTF8
    if (-not $prompt) { throw "Prompt file was empty or unreadable: $promptFile" }

    $claudeExe = "$env:USERPROFILE\.local\bin\claude.exe"
    $prompt | & $claudeExe -p --permission-mode dontAsk *>&1 | Tee-Object -FilePath $logFile
}
catch {
    $_ | Out-String | Tee-Object -FilePath $logFile -Append
    "SCRIPT ERROR: $($_.Exception.Message)" | Tee-Object -FilePath $logFile -Append
    exit 1
}
