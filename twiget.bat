@echo off
title twiget
cd "%~dp0"
python .\twiget.py
if %ERRORLEVEL% == 1 (
  echo エラー発生、終了します。
  pause
) else (
  exit /b
  )
