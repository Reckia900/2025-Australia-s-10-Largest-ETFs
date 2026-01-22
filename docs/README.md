# GitHub Pages Deployment Guide

Your financial modelling system website is now ready to publish to GitHub Pages!

## 📋 What's in this `/docs` folder:

- **index.html** - Complete website with embedded CSS and all content
- **_config.yml** - GitHub Pages configuration file

## 🚀 To Publish (3 Steps):

### Step 1: Commit and Push Changes

```bash
git add docs/
git commit -m "Add GitHub Pages deployment"
git push origin main
```

### Step 2: Enable GitHub Pages in Repository Settings

1. Go to your repository on GitHub: https://github.com/Reckia900/2025-Australia-s-10-Largest-ETFs
2. Click **Settings** → **Pages**
3. Under "Build and deployment":
   - **Source**: Select "Deploy from a branch"
   - **Branch**: Select `main`
   - **Folder**: Select `/ (root)` or `/docs`
   - Click **Save**

### Step 3: Access Your Live Website

Wait 1-2 minutes for GitHub to build and deploy, then visit:

🌐 **https://reckia900.github.io/2025-Australia-s-10-Largest-ETFs/**

## 📱 What You Get:

✅ **Static HTML Landing Page** - Professional website with all features documented
✅ **Interactive Diagrams** - Feature cards and ETF listings
✅ **Getting Started Guide** - Installation and usage instructions
✅ **Code Examples** - Python API usage examples
✅ **Responsive Design** - Works on mobile, tablet, and desktop

## 🎯 For the Interactive Dashboard:

The Streamlit dashboard (`app.py`) requires a running server. To use it locally:

```bash
# Install dependencies
pip install -e .

# Run the dashboard
streamlit run app.py
```

For online deployment of the Streamlit dashboard, see: https://docs.streamlit.io/streamlit-cloud

## 📚 Project Structure:

```
2025-Australia-s-10-Largest-ETFs/
├── docs/                          # GitHub Pages content
│   ├── index.html                 # Main website
│   └── _config.yml                # GitHub Pages config
├── financial_modelling/           # Python package
│   ├── __init__.py
│   ├── config.py
│   ├── data_manager.py
│   ├── models.py
│   ├── metrics.py
│   └── optimization.py
├── tests/                         # Test suite
├── app.py                         # Streamlit dashboard
├── examples.py                    # Usage examples
├── README.md                      # API documentation
├── pyproject.toml                 # Package config
└── LICENSE
```

## ✨ Next Steps:

1. ✅ Verify your website is live
2. 📖 Update GitHub repo description to include the link
3. 🔗 Share the link: https://reckia900.github.io/2025-Australia-s-10-Largest-ETFs/
4. 🚀 (Optional) Deploy the Streamlit dashboard to Streamlit Cloud

---

**Questions?** Check the main README.md for detailed documentation!
