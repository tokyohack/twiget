@echo off
title twiget
cd "%~dp0"
python .\twiget.py
if %ERRORLEVEL% == 1 (
  echo �G���[�����A�I�����܂��B
  pause
) else (
  exit /b
  )
