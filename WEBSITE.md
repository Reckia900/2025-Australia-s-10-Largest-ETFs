# 🌐 Running the Financial Modelling System Website

## Quick Start (3 Steps)

### Step 1: Install Dependencies
```bash
pip install -e .
```

### Step 2: Run the Web Dashboard
```bash
streamlit run app.py
```

### Step 3: Open in Browser
Navigate to: **http://localhost:8501**

---

## 📱 What You'll See

### Beautiful Interactive Dashboard with 5 Main Tabs:

#### 📊 Overview Tab
- Individual ETF performance metrics
- Annual returns, volatility, Sharpe ratios
- Maximum drawdown statistics
- Normalized price history chart

#### 📈 Technical Analysis Tab
- Returns distribution histograms
- Statistical analysis (skewness, kurtosis)
- Return statistics for each ETF
- Visual distribution patterns

#### 🔗 Correlation Tab
- Correlation matrix heatmap
- Asset relationship analysis
- Diversification statistics
- Average/min/max correlations

#### 🎯 Optimization Tab
- Three optimization strategies
  - Maximum Sharpe Ratio (best risk-adjusted returns)
  - Minimum Volatility (safest portfolio)
  - Equal Weight (simple diversification)
- Portfolio allocation pie chart
- Performance metrics display
- Efficient frontier visualization

#### 📋 Summary Tab
- Analysis period details
- Selected ETFs list
- Download data as CSV

---

## 🎨 Features of the Web Interface

✨ **Professional Design**
- Gradient purple theme
- Responsive layout for all devices
- Smooth hover effects
- Clean, modern styling

📊 **Interactive Charts**
- Price history with multiple ETFs
- Correlation heatmaps
- Portfolio allocation pie charts
- Efficient frontier scatter plots
- Returns distribution histograms

⚙️ **Sidebar Controls**
- ETF selection with multi-select
- Custom date range picker
- Risk-free rate adjustment
- System information panel

🔄 **Real-time Updates**
- Data fetched from Yahoo Finance
- Automatic caching for performance
- Loading indicators
- Error handling with helpful messages

---

## 📋 Configuration Options

### Sidebar Controls:

1. **📈 ETF Selection**
   - Select any combination of available ETFs
   - Default: First 3 ETFs selected

2. **📅 Time Period**
   - Start Date: Pick any historical date
   - End Date: Default is today
   - Default: 5 years of historical data

3. **💰 Risk-Free Rate**
   - Adjust annual risk-free rate (0-10%)
   - Default: 4% (Australian government bonds)
   - Used for Sharpe ratio calculations

---

## 📊 Available Metrics

### Performance Metrics
- **Annual Return**: Geometric average annual return
- **Volatility**: Standard deviation of returns
- **Cumulative Return**: Total return over period

### Risk-Adjusted Metrics
- **Sharpe Ratio**: Return per unit of risk (>1 is good)
- **Sortino Ratio**: Return per unit of downside risk
- **Max Drawdown**: Largest peak-to-trough decline

### Portfolio Metrics
- **VaR (95%)**: Maximum expected loss
- **CVaR (95%)**: Average loss beyond VaR
- **Beta**: Systematic risk relative to market
- **Diversification**: Effective number of positions

### Distribution Metrics
- **Skewness**: Asymmetry of returns (-0.5 to 0.5 is good)
- **Kurtosis**: Tail heaviness (lower is better)
- **Win Rate**: Percentage of positive daily returns

---

## 🎯 How to Use Each Tab

### Overview Tab
1. View overall performance of selected ETFs
2. Compare Sharpe ratios
3. Check price trends over time
4. Identify best performers

### Technical Analysis Tab
1. Analyze return distributions
2. Check for extreme values
3. Compare volatility patterns
4. Identify skewed returns

### Correlation Tab
1. Understand diversification benefits
2. Identify correlated assets
3. Find complementary ETFs
4. Optimize for low correlation

### Optimization Tab
1. Select optimization strategy
2. View recommended weights
3. Check expected returns & volatility
4. Explore efficient frontier
5. Find your optimal portfolio

### Summary Tab
1. Review analysis parameters
2. Download data for external analysis
3. Export for reporting

---

## 💻 Python Code Access

You can also use the system programmatically:

```python
from financial_modelling import DataManager, PortfolioOptimizer

# Create data manager
dm = DataManager()

# Fetch data
dm.fetch_data(['VAS.AX', 'VGS.AX'])

# Get returns
returns = dm.get_returns()

# Optimize portfolio
optimizer = PortfolioOptimizer(returns)
result = optimizer.optimize_max_sharpe()

print(result.weights)
print(result.expected_return)
print(result.sharpe_ratio)
```

---

## 🌐 Static HTML Landing Page

A professional landing page is also available at:
**index.html**

Open in any browser to see:
- Project overview
- Feature highlights
- Installation instructions
- Technology stack
- Getting started guide

---

## 🚀 Running Examples

To see example usage:

```bash
python examples.py
```

This demonstrates:
- Basic ETF analysis
- Portfolio analysis
- Portfolio optimization
- Advanced metrics

---

## 🧪 Running Tests

To verify everything works:

```bash
pytest tests/ -v
pytest tests/ --cov=financial_modelling
```

---

## 📁 Project Structure

```
├── app.py                      # Main Streamlit web application
├── index.html                  # Static landing page
├── examples.py                 # Usage examples
├── financial_modelling/        # Core package
│   ├── data_manager.py        # Data fetching & caching
│   ├── models.py              # Financial models
│   ├── metrics.py             # Metrics calculation
│   ├── optimization.py        # Portfolio optimization
│   └── config.py              # Configuration
├── tests/                      # Unit tests
├── README.md                   # Full documentation
├── CONTRIBUTING.md            # Contribution guide
└── QUICKSTART.py             # Quick start script
```

---

## ⚙️ System Requirements

- **Python**: 3.10 or higher
- **RAM**: 4GB minimum (8GB recommended)
- **Disk**: 500MB for data cache
- **Browser**: Any modern browser (Chrome, Firefox, Safari, Edge)
- **Internet**: Required for data fetching

---

## 🔧 Troubleshooting

### Dashboard won't start?
```bash
pip install --upgrade streamlit
streamlit run app.py --logger.level=debug
```

### Data fetch errors?
- Check internet connection
- Verify ETF symbols are valid
- Clear cache: `rm -rf data/cache/`

### Slow performance?
- Use fewer ETFs
- Reduce time period
- Close other applications

---

## 📞 Support

For issues or questions:
1. Check README.md for detailed documentation
2. Review examples.py for usage patterns
3. Run tests to verify installation
4. Check CONTRIBUTING.md for guidelines

---

## ⚖️ Important Disclaimer

⚠️ **This system is for educational and analytical purposes only.**

- **Not financial advice**: Always consult a licensed financial advisor
- **Past performance**: Does not guarantee future results
- **Risk warning**: All investments carry risk, including loss of principal
- **Validate**: Always validate with your own analysis
- **Diversify**: Use this as one input, not the sole basis for decisions

---

## 🎓 Learning Resources

- **README.md**: Complete API documentation
- **examples.py**: Code examples
- **Financial Theory**: Look up Modern Portfolio Theory, Sharpe ratios, efficient frontier
- **Data**: Yahoo Finance documentation

---

Enjoy analyzing your ETF portfolio! 📊
