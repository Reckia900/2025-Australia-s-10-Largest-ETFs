#!/usr/bin/env bash
# Installation and setup script for the Financial Modelling System

echo "╔═══════════════════════════════════════════════════════════════╗"
echo "║  Australian ETF Financial Modelling System - Setup Guide      ║"
echo "╚═══════════════════════════════════════════════════════════════╝"
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed. Please install Python 3.10 or higher."
    exit 1
fi

echo "✓ Python found: $(python3 --version)"
echo ""

# Create virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    echo "📦 Creating virtual environment..."
    python3 -m venv venv
    echo "✓ Virtual environment created"
fi

# Activate virtual environment
echo "📦 Activating virtual environment..."
source venv/bin/activate

# Install dependencies
echo "📥 Installing dependencies..."
pip install --upgrade pip setuptools wheel

# Install package
echo "📦 Installing financial_modelling package..."
pip install -e .

# Install optional dev dependencies
echo "📦 Installing development dependencies..."
pip install -e ".[dev]"

echo ""
echo "╔═══════════════════════════════════════════════════════════════╗"
echo "║  ✅ Setup Complete!                                           ║"
echo "╚═══════════════════════════════════════════════════════════════╝"
echo ""

echo "🚀 To start the web dashboard, run:"
echo "   streamlit run app.py"
echo ""

echo "📚 To run example scripts:"
echo "   python examples.py"
echo ""

echo "🧪 To run tests:"
echo "   pytest tests/ -v"
echo ""

echo "📖 For more information, see:"
echo "   - README.md (comprehensive documentation)"
echo "   - CONTRIBUTING.md (contribution guidelines)"
echo "   - python QUICKSTART.py (quick start guide)"
echo ""
