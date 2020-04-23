@echo off
set ZIP=C:\PROGRA~1\7-Zip\7z.exe a -tzip -y -r
set REPO=humpty
set PACKAGE_ID=humpty_dumpty
set NAME=humpty_dumpty
set VERSION=0.1.0

fsum -r -jm -md5 -d%REPO% * > checksum.md5
move checksum.md5 %REPO%/checksum.md5

echo %VERSION% >%REPO%/VERSION


cd %REPO%

quick_manifest.exe "Humpty Dumpty Convert V1 V2" "%PACKAGE_ID%" >manifest.json
%ZIP% ../%NAME%_v%VERSION%_Anki21.ankiaddon *


quick_manifest.exe "Humpty Dumpty Convert V1 V2" "%NAME%" >manifest.json
%ZIP% ../%NAME%_v%VERSION%_CCBC.adze *

