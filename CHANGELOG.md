# Changelog

All notable changes to this project will be documented in this file.

## [1.0.0] - 2025-01-22

### Added
- Initial release of Financial Modelling System
- DataManager for fetching and caching ETF data from Yahoo Finance
- FinancialModel for analyzing individual ETFs
  - Annualized return, volatility, Sharpe ratio, Sortino ratio, max drawdown
  - Rolling metrics calculation
- PortfolioModel for multi-asset portfolio analysis
  - Portfolio return, volatility, Sharpe ratio
  - VaR and CVaR calculations
  - Correlation and covariance matrices
  - Beta calculation
- MetricsCalculator for comprehensive metrics
  - Skewness, kurtosis, win rate
  - Recovery factor, Calmar ratio
  - Information and Treynor ratios
  - Monte Carlo VaR/CVaR simulation
  - Herfindahl index and effective N
  - Stress testing
- PortfolioOptimizer for portfolio optimization
  - Maximum Sharpe ratio optimization
  - Minimum volatility optimization
  - Target return optimization
  - Efficient frontier generation
  - Equal weight and market-cap weight portfolios
- Interactive Streamlit dashboard
  - ETF performance metrics
  - Price history visualization
  - Returns distribution analysis
  - Correlation heatmap
  - Portfolio optimization interface
  - Efficient frontier visualization
- Comprehensive test suite with pytest
- Example usage scripts
- Full documentation and API reference
- Configuration module for customization

### Features
- Data caching to avoid redundant downloads
- Support for 10 major Australian ETFs
- Customizable risk-free rate
- Flexible date range selection
- Export functionality for analysis data

---

## Future Roadmap

### v1.1.0 (Planned)
- Real-time data streaming
- Genetic algorithm optimization
- Extended backtesting framework
- Performance attribution analysis

### v1.2.0 (Planned)
- Machine learning-based predictions
- Multi-currency support
- GARCH volatility models
- Advanced risk metrics

### v2.0.0 (Long-term)
- REST API
- Web interface improvements
- Mobile app
- Integration with trading platforms
