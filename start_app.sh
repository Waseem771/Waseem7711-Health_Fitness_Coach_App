#!/bin/bash

echo "🏋️‍♂️ Health & Fitness Coach App - Quick Start Script"
echo "=================================================="

# Check if Python is installed
if ! command -v python &> /dev/null; then
    echo "❌ Python is not installed. Please install Python 3.7+ and try again."
    exit 1
fi

echo "✅ Python is available"

# Check if pip is installed
if ! command -v pip &> /dev/null; then
    echo "❌ pip is not installed. Please install pip and try again."
    exit 1
fi

echo "✅ pip is available"

# Install requirements
echo "📦 Installing required packages..."
pip install -r requirements.txt

if [ $? -ne 0 ]; then
    echo "❌ Failed to install requirements. Please check your internet connection and try again."
    exit 1
fi

echo "✅ All packages installed successfully"

# Run the Streamlit app
echo "🚀 Starting the Health & Fitness Coach App..."
echo "🌐 The app will open in your default browser"
echo "🔗 If it doesn't open automatically, visit: http://localhost:8501"
echo ""
echo "To stop the app, press Ctrl+C"
echo ""

streamlit run app.py