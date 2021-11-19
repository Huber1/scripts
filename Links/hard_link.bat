echo off
cd /D %UserProfile%
echo.

echo Hard Link generator
echo select folder path. you are in your user directory
echo.

set /p link=Link file path:  
set /p target=Target file path:  

echo.

mklink /J %link% %target%

pause