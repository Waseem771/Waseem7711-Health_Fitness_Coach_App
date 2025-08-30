#!/usr/bin/env python3
"""
Deployment Validation Script for Health & Fitness Coach App
Validates that all required files are present and properly configured.
"""

import os
import sys
from pathlib import Path

def check_file_exists(file_path, description):
    """Check if a file exists and return status"""
    if os.path.exists(file_path):
        print(f"✅ {description}: {file_path}")
        return True
    else:
        print(f"❌ {description}: {file_path} - MISSING")
        return False

def check_file_content(file_path, required_content, description):
    """Check if file contains required content"""
    if os.path.exists(file_path):
        with open(file_path, 'r') as f:
            content = f.read()
            if required_content in content:
                print(f"✅ {description}")
                return True
            else:
                print(f"❌ {description} - Content not found")
                return False
    else:
        print(f"❌ {description} - File missing")
        return False

def main():
    print("🔍 Health & Fitness Coach App - Deployment Validation")
    print("=" * 60)
    
    all_good = True
    
    # Check core app files
    core_files = [
        ("app.py", "Main Streamlit application"),
        ("requirements.txt", "Python dependencies"),
        ("README.md", "Project documentation"),
    ]
    
    for file_path, description in core_files:
        if not check_file_exists(file_path, description):
            all_good = False
    
    # Check deployment configuration files
    deployment_files = [
        (".streamlit/config.toml", "Streamlit configuration"),
        ("Procfile", "Heroku deployment config"),
        ("runtime.txt", "Python runtime specification"),
        ("Dockerfile", "Docker container config"),
        (".gitignore", "Git ignore file"),
    ]
    
    for file_path, description in deployment_files:
        if not check_file_exists(file_path, description):
            all_good = False
    
    # Check portfolio and documentation
    docs_files = [
        ("index.html", "Portfolio landing page"),
        ("DEPLOYMENT.md", "Deployment guide"),
        ("QUICK_START.md", "Quick start guide"),
    ]
    
    for file_path, description in docs_files:
        if not check_file_exists(file_path, description):
            all_good = False
    
    # Check GitHub Actions workflows
    workflow_files = [
        (".github/workflows/deploy.yml", "GitHub Pages workflow"),
        (".github/workflows/test-and-deploy.yml", "Testing workflow"),
    ]
    
    for file_path, description in workflow_files:
        if not check_file_exists(file_path, description):
            all_good = False
    
    # Check quick start scripts
    script_files = [
        ("start_app.sh", "Linux/Mac start script"),
        ("start_app.bat", "Windows start script"),
    ]
    
    for file_path, description in script_files:
        if not check_file_exists(file_path, description):
            all_good = False
    
    print("\n🔍 Content Validation")
    print("-" * 30)
    
    # Validate app.py content
    content_checks = [
        ("app.py", "def app():", "Main app function defined"),
        ("app.py", "streamlit", "Streamlit imported"),
        ("requirements.txt", "streamlit", "Streamlit dependency listed"),
        ("Procfile", "streamlit run app.py", "Heroku command configured"),
        ("index.html", "Health & Fitness Coach", "Landing page title present"),
    ]
    
    for file_path, required_content, description in content_checks:
        if not check_file_content(file_path, required_content, description):
            all_good = False
    
    print("\n" + "=" * 60)
    
    if all_good:
        print("🎉 SUCCESS! Your app is ready for deployment!")
        print("\nNext steps:")
        print("1. Deploy to Streamlit Cloud: https://share.streamlit.io/")
        print("2. Enable GitHub Pages in repository settings")
        print("3. Share your live app with users!")
        return 0
    else:
        print("❌ ISSUES FOUND! Please fix the missing files/content above.")
        print("\nRefer to DEPLOYMENT.md for detailed instructions.")
        return 1

if __name__ == "__main__":
    sys.exit(main())