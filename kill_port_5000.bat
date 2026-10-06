@echo off
echo =======================================
echo Killing active process on Port 5000...
echo =======================================
for /f "tokens=5" %%a in ('netstat -aon ^| findstr :5000 ^| findstr LISTENING') do (
    echo Terminating PID: %%a
    taskkill /F /PID %%a >nul 2>&1
)
timeout /t 1 >nul
echo Port 5000 is now free.
