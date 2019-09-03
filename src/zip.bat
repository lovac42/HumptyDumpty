@echo off
set ZIP=C:\PROGRA~1\7-Zip\7z.exe a -tzip -y -r
set REPO=humpty
set NAME=humpty_dumpty
set VERSION=0.0.3

fsum -r -jm -md5 -d%REPO% * > checksum.md5
move checksum.md5 %REPO%/checksum.md5

quick_manifest.exe "Humpty Dumpty" "%REPO%" >%REPO%/manifest.json


echo %VERSION% >%REPO%/VERSION


cd %REPO%
%ZIP% ../%NAME%_v%VERSION%_Anki21.ankiaddon *

%ZIP% ../%NAME%_v%VERSION%_CCBC.adze *
