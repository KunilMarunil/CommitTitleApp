@echo off
echo Building CommitTitleApp.exe...
python -m PyInstaller --onefile --noconsole CommitTitleApp.py
echo Selesai! Lihat folder dist\
pause