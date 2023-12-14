@echo off
title  M-Terminal Installer
echo Starting installer...
py -m pip install pyserial
py -m pipinstall colorama
echo Finished installing
echo Starting build...
pyinstaller --onefile main.py
echo Cleaning up...
del main.spec
del main.py
rmdir /s /q build
move dist\main.exe M-Terminal.exe
rmdir /s /q dist
echo Finished building
pause