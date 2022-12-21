@echo off
echo start build
@del ..\releases.zip >nul
@rd /s/q bin >nul
@rd /s/q ghostcp >nul
set http_proxy=http://127.0.0.1:7890
set https_proxy=http://127.0.0.1:7890
git clone https://github.com/macronut/ghostcp/
cd ghostcp
go build
cd ..
mkdir bin
copy .\ghostcp\ghostcp.exe .\bin
copy .\needfile\* .\bin /Y
copy ..\default.conf .\bin /Y
7z.exe a -r ./releases.zip ./bin
copy .\releases.zip ..\
rd /s/q ghostcp
rd /s/q bin
del releases.zip
echo done.
pause