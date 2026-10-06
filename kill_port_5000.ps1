$port = 5000
Write-Host "Checking for processes listening on port $port..." -ForegroundColor Cyan
$connections = Get-NetTCPConnection -LocalPort $port -ErrorAction SilentlyContinue

if ($connections) {
    foreach ($conn in $connections) {
        $pId = $conn.OwningProcess
        if ($pId -and $pId -ne 0) {
            $pName = (Get-Process -Id $pId -ErrorAction SilentlyContinue).ProcessName
            Write-Host "Terminating $pName (PID $pId)..." -ForegroundColor Yellow
            Stop-Process -Id $pId -Force -ErrorAction SilentlyContinue
        }
    }
    Start-Sleep -Seconds 1
    Write-Host "Port $port is now completely free!" -ForegroundColor Green
} else {
    Write-Host "No process found holding port $port. It is already free." -ForegroundColor Green
}
