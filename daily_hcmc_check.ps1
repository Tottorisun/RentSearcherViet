$ErrorActionPreference = "Continue"
Set-Location "D:\Мои разработки\Rent Searcher"

$logDir = "D:\Мои разработки\Rent Searcher\daily_check_logs"
if (-not (Test-Path $logDir)) { New-Item -ItemType Directory -Path $logDir | Out-Null }

$stamp = Get-Date -Format "yyyy-MM-dd_HHmmss"
$logFile = Join-Path $logDir "check_$stamp.log"

$prompt = Get-Content "D:\Мои разработки\Rent Searcher\daily_hcmc_check_prompt.txt" -Raw

$prompt | & "C:\Users\User\.local\bin\claude.exe" -p --permission-mode dontAsk *>&1 | Tee-Object -FilePath $logFile
