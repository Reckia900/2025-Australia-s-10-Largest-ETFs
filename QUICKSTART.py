#!/usr/bin/env python
"""
Quick Start Guide - Financial Modelling System

This script demonstrates the basic usage patterns.
"""

import sys
import os

# Add the package to path
sys.path.insert(0, os.path.dirname(__file__))

print("=" * 70)
print("FINANCIAL MODELLING SYSTEM - QUICK START GUIDE")
print("=" * 70)

print("\n📦 Installation:")
print("-" * 70)
print("pip install -e .")
print("pip install -e '.[dev]'  # For development")

print("\n🚀 Running the Dashboard:")
print("-" * 70)
print("streamlit run app.py")
print("Then open: http://localhost:8501")

print("\n📊 Python API Usage:")
print("-" * 70)
print("""
from financial_modelling import DataManager, PortfolioOptimizer

# 1. Fetch ETF data
dm = DataManager()
dm.fetch_data(['VAS.AX', 'VGS.AX', 'VDHG.AX'])

# 2. Get returns
returns = dm.get_returns()

# 3. Optimize portfolio
optimizer = PortfolioOptimizer(returns)
result = optimizer.optimize_max_sharpe()

# 4. View results
print(f"Weights: {result.weights}")
print(f"Return: {result.expected_return:.2%}")
print(f"Volatility: {result.volatility:.2%}")
print(f"Sharpe Ratio: {result.sharpe_ratio:.2f}")
""")

print("\n📚 Run Examples:")
print("-" * 70)
print("python examples.py")

print("\n🧪 Run Tests:")
print("-" * 70)
print("pytest tests/ -v")
print("pytest tests/ --cov=financial_modelling")

print("\n📖 Documentation:")
print("-" * 70)
print("See README.md for comprehensive documentation")
print("See CONTRIBUTING.md for contribution guidelines")
print("See CHANGELOG.md for version history")

print("\n🔑 Key Components:")
print("-" * 70)
print("""
1. DataManager
   - Fetch historical ETF data
   - Cache and manage data locally
   - Export/import data

2. FinancialModel
   - Analyze individual ETF performance
   - Calculate risk metrics
   - Rolling statistics

3. PortfolioModel
   - Multi-asset portfolio analysis
   - Risk calculations (VaR, CVaR)
   - Correlation analysis

4. PortfolioOptimizer
   - Maximum Sharpe ratio
   - Minimum volatility
   - Target return optimization
   - Efficient frontier

5. MetricsCalculator
   - Advanced risk metrics
   - Stress testing
   - Distribution analysis
""")

print("\n✨ Main Features:")
print("-" * 70)
print("""
✓ Historical data from Yahoo Finance
✓ Modern Portfolio Theory optimization
✓ Risk metrics: VaR, CVaR, Beta, etc.
✓ Interactive dashboard
✓ Efficient frontier visualization
✓ Stress testing
✓ Correlation analysis
✓ Advanced metrics: Sharpe, Sortino, Calmar ratios
""")

print("\n⚠️  Important Notes:")
print("-" * 70)
print("""
1. This is for educational and analytical purposes
2. Not financial advice - consult a professional
3. Past performance ≠ future results
4. All investments carry risk
5. Validate with your own analysis
""")

print("\n" + "=" * 70)
print("Ready to get started? Run: streamlit run app.py")
print("=" * 70 + "\n")
