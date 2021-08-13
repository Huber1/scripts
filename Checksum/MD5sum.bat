echo off
cd /D %UserProfile%
echo.

echo sha265-checksum Generator
echo select file path. you are in your user directory
echo to chose file.txt in Downloads, use downloads\file.txt
echo.

set /p location=File path:  

echo.

certUtil -hashfile %location% MD5

pause