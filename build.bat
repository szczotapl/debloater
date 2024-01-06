@echo off
echo Building debloater

echo Installing pyinstaller...
pip install pyinstaller > build.log 2>&1
echo Installed pyinstaller!

echo Installing wxPython...
pip install wxPython > build.log 2>&1
echo Installed wxPython!

echo Building exe...
pyinstaller --onefile src\debloater.py > build.log 2>&1
echo Built exe!

echo Copying exe file...
copy /Y dist\debloater.exe . > build.log 2>&1
echo Copied exe file!

echo Cleaning up...
rmdir /s /q build > build.log 2>&1
rmdir /s /q dist > build.log 2>&1
del /q debloater.spec > build.log 2>&1
echo Cleaned up!

echo Done!
pause > build.log 2>&1
