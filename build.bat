@echo off
title Building ScreenResAI...
setlocal
echo.
echo  Screen Resolution AI Assistant -- Build Script
echo.
python --version >nul 2>&1
if %ERRORLEVEL% neq 0 (echo [ERROR] Python not found. Install from python.org & pause & exit /b 1)
echo [1/5] Upgrading pip...
python -m pip install --upgrade pip --quiet
echo [2/5] Installing requirements...
pip install -r requirements.txt --quiet
if %ERRORLEVEL% neq 0 (echo [ERROR] pip install failed & pause & exit /b 1)
echo [3/5] Installing PyInstaller...
pip install pyinstaller --quiet
echo [4/5] Cleaning previous build...
if exist build rd /s /q build
if exist dist rd /s /q dist
echo [5/5] Compiling EXE (2-4 minutes)...
pyinstaller ScreenResAI.spec --noconfirm --clean
if %ERRORLEVEL% neq 0 (echo [ERROR] PyInstaller failed & pause & exit /b 1)
echo.
echo BUILD COMPLETE! Output: dist\ScreenResAI.exe
echo.
pause
