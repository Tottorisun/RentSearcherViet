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
    # Tee-Object on this PowerShell build has no -Encoding parameter -- write log as
    # PowerShell's default (UTF-16LE) rather than crashing; it's still readable in any
    # real editor, and streaming live means partial output survives a kill/timeout.
    $prompt | & $claudeExe -p --permission-mode dontAsk *>&1 | Tee-Object -FilePath $logFile
    # A pipeline doesn't throw on its own -- claude.exe can fail (e.g. expired auth)
    # while this script still reaches here and would otherwise report success.
    if ($LASTEXITCODE -ne 0) {
        "SCRIPT ERROR: claude.exe exited with code $LASTEXITCODE -- see output above (often an auth/session problem, run 'claude auth status' to check)." | Tee-Object -FilePath $logFile -Append
        exit 1
    }
}
catch {
    ($_ | Out-String) | Tee-Object -FilePath $logFile -Append
    "SCRIPT ERROR: $($_.Exception.Message)" | Tee-Object -FilePath $logFile -Append
    exit 1
}
