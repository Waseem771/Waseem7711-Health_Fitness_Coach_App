# 🚀 Deployment Guide - Health & Fitness Coach App

This guide provides step-by-step instructions for deploying your Health & Fitness Coach App on various platforms.

## 🌟 Streamlit Cloud (Recommended - Free & Easy)

Streamlit Cloud is the easiest way to deploy your Streamlit app for free!

### Steps:
1. **Sign up** at [share.streamlit.io](https://share.streamlit.io/)
2. **Connect GitHub**: Link your GitHub account
3. **Select Repository**: Choose `Waseem771/Waseem7711-Health_Fitness_Coach_App`
4. **Deploy**: Click "Deploy" button
5. **Access**: Your app will be live at `https://your-app-name.streamlit.app`

### Requirements:
- GitHub repository (✅ Already set up)
- requirements.txt file (✅ Already included)
- app.py file (✅ Already included)

---

## 🐳 Docker Deployment

Deploy using Docker for containerized environments.

### Prerequisites:
- Docker installed on your system

### Steps:
```bash
# Clone the repository
git clone https://github.com/Waseem771/Waseem7711-Health_Fitness_Coach_App.git
cd Waseem7711-Health_Fitness_Coach_App

# Build the Docker image
docker build -t fitness-coach-app .

# Run the container
docker run -p 8501:8501 fitness-coach-app
```

Your app will be available at `http://localhost:8501`

---

## 🌐 Heroku Deployment

Deploy to Heroku for production-ready hosting.

### Prerequisites:
- Heroku account
- Heroku CLI installed

### Steps:
```bash
# Clone and navigate to repository
git clone https://github.com/Waseem771/Waseem7711-Health_Fitness_Coach_App.git
cd Waseem7711-Health_Fitness_Coach_App

# Login to Heroku
heroku login

# Create Heroku app
heroku create your-unique-app-name

# Deploy to Heroku
git push heroku main

# Open your app
heroku open
```

### Required Files (✅ Already included):
- `Procfile` - Tells Heroku how to run your app
- `runtime.txt` - Specifies Python version
- `requirements.txt` - Lists dependencies

---

## 📱 GitHub Pages (Portfolio Landing)

A beautiful landing page for your app portfolio.

### Automatic Deployment:
- GitHub Actions is configured to automatically deploy to GitHub Pages
- Your portfolio will be available at: `https://waseem771.github.io/Waseem7711-Health_Fitness_Coach_App/`

### Manual Setup:
1. Go to your repository settings
2. Navigate to "Pages" section
3. Select "Source" as "GitHub Actions"
4. The workflow will automatically deploy your landing page

---

## 💻 Local Development

For local testing and development:

### Option 1: Quick Start Scripts
```bash
# Linux/Mac
./start_app.sh

# Windows
start_app.bat
```

### Option 2: Manual Setup
```bash
# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py
```

---

## 🔧 Configuration Options

### Environment Variables:
- `PORT` - Server port (default: 8501)
- `STREAMLIT_SERVER_HEADLESS` - Run in headless mode (default: true)

### Streamlit Configuration:
The app includes a `.streamlit/config.toml` file with optimized settings for deployment.

---

## 🎨 Customization

### Theme Colors:
Edit `.streamlit/config.toml` to change the app's color scheme:
```toml
[theme]
primaryColor = "#FF6B6B"           # Primary accent color
backgroundColor = "#FFFFFF"        # Background color
secondaryBackgroundColor = "#F0F2F6"  # Sidebar color
textColor = "#262730"              # Text color
```

### App Content:
- Edit `app.py` to modify app functionality
- Update `index.html` to customize the landing page
- Modify `README.md` for documentation updates

---

## 🚨 Troubleshooting

### Common Issues:

1. **Requirements Installation Error**
   ```bash
   pip install --upgrade pip
   pip install -r requirements.txt --no-cache-dir
   ```

2. **Port Already in Use**
   ```bash
   streamlit run app.py --server.port=8502
   ```

3. **Memory Issues on Heroku**
   - Heroku free tier has memory limitations
   - Consider upgrading to a paid plan for better performance

4. **GitHub Pages Not Loading**
   - Check GitHub Actions tab for deployment status
   - Ensure GitHub Pages is enabled in repository settings

---

## 📞 Support

If you encounter any issues:

1. Check the [GitHub Issues](https://github.com/Waseem771/Waseem7711-Health_Fitness_Coach_App/issues)
2. Create a new issue with detailed error messages
3. Contact: [Waseem Hassan](https://github.com/Waseem771)

---

## 🎉 Success!

Once deployed, your Health & Fitness Coach App will be live and accessible to users worldwide!

### What's Next?
- Share your app URL with friends and family
- Monitor usage through platform analytics
- Collect user feedback for improvements
- Consider adding new features based on user needs

Happy deploying! 🚀