#!/bin/bash

echo "🛠️ Building Executable for Article Document Generator..."

# === Step 1: Check for virtual environment (optional) ===
if [ -f "venv/bin/activate" ]; then
  echo "🔄 Activating virtual environment..."
  source venv/bin/activate
fi

# === Step 2: Install dependencies ===
echo "📦 Installing Python dependencies..."
pip install --upgrade pip
pip install pandas openpyxl docxtpl pyinstaller

# === Step 3: Remove old builds ===
echo "🧹 Cleaning up old build directories..."
rm -rf build dist __pycache__ main.spec

# === Step 4: Build executable ===
echo "🚀 Running PyInstaller..."
pyinstaller --onefile --add-data "input;input" main.py

# === Step 5: Completion Message ===
if [ -f "dist/main.exe" ]; then
  echo "✅ Build complete: dist/main.exe"
else
  echo "❌ Build failed"
fi
