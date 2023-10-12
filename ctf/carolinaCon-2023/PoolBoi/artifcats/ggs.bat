@echo off

cd /d %~dp0

xdelta.exe -d -f -s %1 "./ctfgoods.rick" "ctf.roll"

echo.
echo Done!

pause