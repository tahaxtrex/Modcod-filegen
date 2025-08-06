@echo off
echo 🛠️ Building Executable for Article Document Generator...

:: Step 1: Upgrade pip and install dependencies
echo 📦 Installing Python dependencies...
python -m pip install --upgrade pip
python -m pip install pandas openpyxl docxtpl pyinstaller

:: Step 2: Clean old builds
echo 🧹 Cleaning up old build directories...
rmdir /s /q build
rmdir /s /q dist
del main.spec 2>nul

:: Step 3: Build the executable
echo 🚀 Running PyInstaller...
pyinstaller --onefile --add-data "input;input" main.py

:: Step 4: Finish
if exist dist\main.exe (
  echo ✅ Build complete: dist\main.exe
) else (
  echo ❌ Build failed
)

pause
