@echo off
title  M-Terminal Installer
echo Looking for older versions...
del M-Terminal.exe
timeout /nobreak /t 3 >nul
cls
echo Starting installer...
py -m pip install pyserial
py -m pip install colorama
py -m pip install pyinstaller
echo Finished installing
timeout /nobreak /t 3 >nul
cls
echo Starting build...
pyinstaller --onefile main.py
cls
echo Cleaning up...
del main.spec
del main.py
rmdir /s /q build
move dist\main.exe M-Terminal.exe
rmdir /s /q dist
timeout /nobreak /t 3 >nul
cls
echo Finished building
pause
