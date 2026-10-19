@echo off
title ONYX PLATFORM - COMMAND CENTER
color 0A
echo =======================================================
echo     [SYSTEM] INITIATING ONYX CTI PLATFORM (DEMO)
echo =======================================================
set PYTHON_CMD=python
where python >nul 2>&1
if %errorlevel% neq 0 (
    where py >nul 2>&1
    if %errorlevel% neq 0 (
        echo [ERREUR] Python n'est pas installe.
        pause
        exit /b 1
    ) else (
        set PYTHON_CMD=py
    )
)

echo [+] ARMING BACKEND (Uvicorn / FastAPI / ZERO LATENCY)
start "ONYX BACKEND" cmd /k "cd /d "%~dp0onyx-api" && set STANDALONE_MODE=true && %PYTHON_CMD% -m uvicorn onyx_api.main:app --host 0.0.0.0 --port 8000"

echo [+] ARMING FRONTEND (Next.js / 3D Engine)
start "ONYX FRONTEND" cmd /k "cd /d "%~dp0onyx-dashboard" && npm run dev"

echo.
echo [WAIT] Initializing Websockets and WebGL matrix (10 seconds)...
timeout /t 10 /nobreak >nul

echo.
echo [+] FIRING NLP STRESS TEST (SciBERT Injection)
start "ONYX STRESS TEST" cmd /k "cd /d "%~dp0" && %PYTHON_CMD% test_ia_live.py"

echo.
echo [!] LAUNCH SEQUENCE COMPLETE.
echo [!] ACCESS DASHBOARD AT: http://localhost:3000
start chrome "http://localhost:3000"
echo =======================================================
