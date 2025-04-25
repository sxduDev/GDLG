@echo off
python --version >nul 2>&1

IF %ERRORLEVEL% NEQ 0 (
    echo Python not found. Downloading...
    curl -o python-installer.exe https://www.python.org/ftp/python/3.13.3/python-3.13.3-amd64.exe
    start /wait python-installer.exe /quiet InstallAllUsers=1 PrependPath=1
    del python-installer.exe
    echo Python installed.
    python --version
    pip install random
    pip install os
    pip install sys
    pip install json
    pip install datetime
    pip install numpy
    pip install sounddevice
    pip install webbrowser
    pip install pygetwindow
    pip install pyautogui
    pip install time
    pip install traceback
    pip install subprocess
    pip install logging

) ELSE (
    echo Python is already downloaded:
    python --version
    pip install random
    pip install os
    pip install sys
    pip install json
    pip install datetime
    pip install numpy
    pip install sounddevice
    pip install webbrowser
    pip install pygetwindow
    pip install pyautogui
    pip install time
    pip install traceback
    pip install subprocess
    pip install logging
)

pause