# Australian ETF Financial Modelling System

A comprehensive financial modelling and analysis system for Australia's 10 largest ETFs. This system provides tools for data analysis, portfolio optimization, risk management, and performance visualization.

## 🎯 Features

- **Data Management**: Fetch and cache historical ETF data from Yahoo Finance
- **Financial Metrics**: Calculate comprehensive performance metrics (Sharpe, Sortino, max drawdown, etc.)
- **Portfolio Optimization**: Optimize portfolios using Modern Portfolio Theory
  - Maximum Sharpe Ratio
  - Minimum Volatility
  - Equal Weight
  - Target Return optimization
- **Risk Analysis**: Calculate VaR, CVaR, beta, and other risk metrics
- **Visualization Dashboard**: Interactive Streamlit dashboard for analysis and visualization
- **Advanced Metrics**: Skewness, kurtosis, stress testing, rolling metrics, and more

## 📋 Supported ETFs

Default included Australian ETFs:
- **VAS.AX** - Vanguard Australian Shares
- **VGS.AX** - Vanguard Global Shares
- **VGAD.AX** - Vanguard Global Shares Hedged
- **VAP.AX** - Vanguard Developed Markets Index
- **IVV.AX** - iShares Core S&P 500 ETF
- **IVE.AX** - iShares Global Ex-Australia ETF
- **DHHF.AX** - Diversified High Yield Fund
- **VDHG.AX** - Vanguard Diversified High Growth ETF

## 🚀 Quick Start

### Installation

```bash
# Clone repository
git clone <repository-url>
cd 2025-Australia-s-10-Largest-ETFs

# Install dependencies
pip install -e .
```

### Usage

#### 1. **Interactive Dashboard**
```bash
streamlit run app.py
```
Access at `http://localhost:8501`

#### 2. **Python API**
```python
from financial_modelling import DataManager, PortfolioOptimizer

# Fetch data
dm = DataManager()
dm.fetch_data(['VAS.AX', 'VGS.AX'])

# Optimize portfolio
returns = dm.get_returns()
optimizer = PortfolioOptimizer(returns)
result = optimizer.optimize_max_sharpe()

print(f"Optimal Weights: {result.weights}")
print(f"Expected Return: {result.expected_return:.2%}")
print(f"Volatility: {result.volatility:.2%}")
print(f"Sharpe Ratio: {result.sharpe_ratio:.2f}")
```

#### 3. **Example Scripts**
```bash
python examples.py
```

## 📊 Core Modules

### DataManager
Handles data collection, caching, and retrieval.

```python
from financial_modelling import DataManager

dm = DataManager(cache_dir="data/cache")

# Fetch data
data = dm.fetch_data(
    tickers=['VAS.AX', 'VGS.AX'],
    start_date='2023-01-01',
    end_date='2024-01-01'
)

# Get returns
returns = dm.get_returns(method='log')

# Export data
dm.export_data('etf_prices.csv')
```

### FinancialModel
Analyze individual ETF performance.

```python
from financial_modelling import FinancialModel

prices = dm.data['VAS.AX']['VAS.AX']
model = FinancialModel(prices, risk_free_rate=0.04)

metrics = model.calculate_metrics()
print(f"Annual Return: {metrics.annualized_return:.2%}")
print(f"Volatility: {metrics.annualized_volatility:.2%}")
print(f"Sharpe Ratio: {metrics.sharpe_ratio:.2f}")
print(f"Max Drawdown: {metrics.max_drawdown:.2%}")
print(f"Sortino Ratio: {metrics.sortino_ratio:.2f}")
```

### PortfolioModel
Analyze multi-asset portfolios.

```python
from financial_modelling import PortfolioModel
import pandas as pd

returns = dm.get_returns()
weights = pd.Series([0.5, 0.5], index=['VAS.AX', 'VGS.AX'])

portfolio = PortfolioModel(returns, weights)
print(f"Portfolio Return: {portfolio.calculate_portfolio_return():.2%}")
print(f"Portfolio Volatility: {portfolio.calculate_portfolio_volatility():.2%}")
print(f"Sharpe Ratio: {portfolio.calculate_portfolio_sharpe():.2f}")
print(f"VaR (95%): {portfolio.calculate_var(0.95):.2%}")
print(f"CVaR (95%): {portfolio.calculate_cvar(0.95):.2%}")
```

### PortfolioOptimizer
Optimize portfolio weights using various strategies.

```python
from financial_modelling import PortfolioOptimizer

optimizer = PortfolioOptimizer(returns, risk_free_rate=0.04)

# Maximum Sharpe Ratio
max_sharpe = optimizer.optimize_max_sharpe()
print(f"Weights: {max_sharpe.weights}")
print(f"Sharpe Ratio: {max_sharpe.sharpe_ratio:.2f}")

# Minimum Volatility
min_vol = optimizer.optimize_min_volatility()
print(f"Volatility: {min_vol.volatility:.2%}")

# Efficient Frontier
frontier = optimizer.generate_efficient_frontier(num_portfolios=100)
```

### MetricsCalculator
Calculate advanced financial metrics.

```python
from financial_modelling import MetricsCalculator

returns = dm.get_returns()['VAS.AX']

# Risk metrics
skewness = MetricsCalculator.calculate_skewness(returns)
kurtosis = MetricsCalculator.calculate_kurtosis(returns)
win_rate = MetricsCalculator.calculate_win_rate(returns)

# Rolling metrics
rolling = MetricsCalculator.calculate_rolling_metrics(returns, window=30)

# Stress testing
stress = MetricsCalculator.calculate_stress_test(returns, percentile=5)

# Risk concentration
hhi = MetricsCalculator.calculate_herfindahl_index(weights)
effective_n = MetricsCalculator.calculate_effective_n(weights)
```

## 📈 Key Metrics Explained

### Performance Metrics
- **Annualized Return**: Geometric average annual return
- **Volatility (Std Dev)**: Annualized standard deviation of returns
- **Cumulative Return**: Total return over period
- **Max Drawdown**: Largest peak-to-trough decline

### Risk-Adjusted Metrics
- **Sharpe Ratio**: Excess return per unit of risk
  - Formula: (Return - Risk-Free Rate) / Volatility
  - Higher is better (>1 is good)
  
- **Sortino Ratio**: Excess return per unit of downside risk
  - Only penalizes negative volatility
  - Preferred by many practitioners
  
- **Calmar Ratio**: Return per unit of max drawdown
  - Good for strategies with large drawdowns
  
- **Information Ratio**: Excess return vs benchmark per tracking error
  - Measures active management skill

### Risk Metrics
- **Value at Risk (VaR)**: Maximum expected loss at confidence level
- **Conditional VaR (CVaR)**: Average loss beyond VaR threshold
- **Beta**: Systematic risk relative to market
- **Correlation**: Relationship between asset returns

### Distribution Metrics
- **Skewness**: Asymmetry of return distribution
  - Negative skew = higher risk of large losses
  
- **Kurtosis**: Tail heaviness
  - Higher kurtosis = fatter tails (more extreme events)

## 🎯 Portfolio Optimization Strategies

### Maximum Sharpe Ratio
Finds the portfolio with the best risk-adjusted returns.
- Best for risk-aware investors
- Balances return and volatility
- Recommended for most investors

### Minimum Volatility
Minimizes portfolio volatility regardless of return.
- Best for conservative investors
- Focuses on downside protection
- Often called "defensive" portfolio

### Target Return
Minimizes volatility for a specified return level.
- Useful for specific return goals
- Balances risk for defined objectives
- Can be used for liability matching

## 📊 Dashboard Features

The interactive Streamlit dashboard includes:

1. **Overview Tab**
   - Individual ETF performance metrics
   - Normalized price history chart

2. **Analysis Tab**
   - Returns distribution histograms
   - Statistical summaries

3. **Correlation Tab**
   - Correlation matrix heatmap
   - Diversification analysis

4. **Optimization Tab**
   - Portfolio optimization strategies
   - Allocation visualization
   - Efficient frontier plot
   - Risk-return tradeoff analysis

## 🧪 Testing

Run the test suite:

```bash
pytest tests/ -v
pytest tests/ --cov=financial_modelling  # With coverage
```

## 📁 Project Structure

```
2025-Australia-s-10-Largest-ETFs/
├── financial_modelling/          # Main package
│   ├── __init__.py
│   ├── config.py                 # Configuration & constants
│   ├── data_manager.py           # Data fetching & caching
│   ├── models.py                 # Financial models
│   ├── metrics.py                # Metrics calculation
│   └── optimization.py           # Portfolio optimization
├── app.py                        # Streamlit dashboard
├── examples.py                   # Usage examples
├── tests/                        # Unit tests
│   ├── __init__.py
│   └── test_financial_models.py
├── pyproject.toml               # Project configuration
├── README.md                    # This file
└── LICENSE                      # MIT License
```

## 📦 Dependencies

- **numpy, pandas**: Data manipulation and numerical computing
- **scikit-learn, scipy**: Statistical and optimization algorithms
- **yfinance**: Financial data fetching
- **plotly**: Interactive visualizations
- **streamlit**: Web dashboard framework
- **pytest**: Testing framework

## 🔧 Configuration

Edit `financial_modelling/config.py` to customize:
- Default ETF tickers
- Risk-free rate
- Lookback periods
- Trading days per year
- Optimization constraints

## ⚠️ Disclaimer

This system is for educational and analytical purposes. It is not financial advice. 

**Always conduct your own due diligence and consult with a licensed financial advisor before making investment decisions.**

Past performance does not guarantee future results. All investments carry risk, including potential loss of principal.

## 📝 License

MIT License - see LICENSE file for details

## 🤝 Contributing

Contributions are welcome! Areas for enhancement:
- Additional optimization algorithms (genetic, particle swarm)
- Machine learning features
- Real-time data updates
- Factor analysis
- Performance attribution
- Multi-currency support

## 📧 Support

For issues, questions, or suggestions, please open an issue in the repository.

---

**Version**: 1.0.0  
**Last Updated**: January 2026  
**Maintained by**: Financial Analytics Team

