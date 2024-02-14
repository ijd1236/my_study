@echo off

setlocal enabledelayedexpansion

set /a count=0
for /d %%d in (mycom*) do (
    set "folder=%%d"
    set "folder=!folder:~5!"
    if !folder! gtr !count! set /a count=!folder!
)

set /a count+=1
mkdir mycom!count!

exit /b