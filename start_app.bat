@echo off
echo 🏋️‍♂️ Health ^& Fitness Coach App - Quick Start Script
echo ==================================================

:: Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Python is not installed. Please install Python 3.7+ and try again.
    pause
    exit /b 1
)

echo ✅ Python is available

:: Check if pip is installed
pip --version >nul 2>&1
if errorlevel 1 (
    echo ❌ pip is not installed. Please install pip and try again.
    pause
    exit /b 1
)

echo ✅ pip is available

:: Install requirements
echo 📦 Installing required packages...
pip install -r requirements.txt

if errorlevel 1 (
    echo ❌ Failed to install requirements. Please check your internet connection and try again.
    pause
    exit /b 1
)

echo ✅ All packages installed successfully

:: Run the Streamlit app
echo 🚀 Starting the Health ^& Fitness Coach App...
echo 🌐 The app will open in your default browser
echo 🔗 If it doesn't open automatically, visit: http://localhost:8501
echo.
echo To stop the app, press Ctrl+C
echo.

streamlit run app.py

pause