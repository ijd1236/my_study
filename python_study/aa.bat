@echo off

set iterations=5

for /l %%i in (1, 1, %iterations%) do (
    call bb.bat
    :wait
    timeout /t 1 >nul
    tasklist | find "cmd.exe" | find "bb.bat" >nul
    if not errorlevel 1 goto wait
)

exit