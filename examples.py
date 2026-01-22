"""
Example usage script for the financial modelling system.
"""

import pandas as pd
from datetime import datetime, timedelta
from financial_modelling import (
    DataManager,
    FinancialModel,
    PortfolioModel,
    MetricsCalculator,
    PortfolioOptimizer,
)
from financial_modelling.config import DEFAULT_ETFS, RISK_FREE_RATE


def example_basic_analysis():
    """Example: Basic ETF analysis."""
    print("=" * 60)
    print("EXAMPLE 1: Basic ETF Analysis")
    print("=" * 60)

    # Fetch data for select ETFs
    dm = DataManager()
    tickers = ["VAS.AX", "VGS.AX", "VDHG.AX"]

    print(f"\nFetching data for: {tickers}")
    dm.fetch_data(tickers)

    # Analyze each ETF
    prices = dm.get_combined_data()
    for ticker in tickers:
        if ticker in prices.columns:
            model = FinancialModel(prices[ticker], RISK_FREE_RATE)
            metrics = model.calculate_metrics()

            print(f"\n{ticker}:")
            print(f"  Annual Return:    {metrics.annualized_return * 100:.2f}%")
            print(f"  Volatility:       {metrics.annualized_volatility * 100:.2f}%")
            print(f"  Sharpe Ratio:     {metrics.sharpe_ratio:.2f}")
            print(f"  Sortino Ratio:    {metrics.sortino_ratio:.2f}")
            print(f"  Max Drawdown:     {metrics.max_drawdown * 100:.2f}%")
            print(f"  Cumulative Return: {metrics.cumulative_return * 100:.2f}%")


def example_portfolio_analysis():
    """Example: Portfolio analysis and metrics."""
    print("\n" + "=" * 60)
    print("EXAMPLE 2: Portfolio Analysis")
    print("=" * 60)

    # Fetch data
    dm = DataManager()
    tickers = ["VAS.AX", "VGS.AX", "VAP.AX"]
    dm.fetch_data(tickers)

    # Get returns
    returns = dm.get_returns()
    print(f"\nLoaded data with {len(returns)} trading days")

    # Create equal-weight portfolio
    weights = pd.Series([1/3, 1/3, 1/3], index=tickers)
    portfolio = PortfolioModel(returns, weights, RISK_FREE_RATE)

    print("\nEqual-Weight Portfolio Metrics:")
    print(f"  Portfolio Return:     {portfolio.calculate_portfolio_return() * 100:.2f}%")
    print(f"  Portfolio Volatility: {portfolio.calculate_portfolio_volatility() * 100:.2f}%")
    print(f"  Sharpe Ratio:         {portfolio.calculate_portfolio_sharpe():.2f}")
    print(f"  VaR (95%):           {portfolio.calculate_var(0.95) * 100:.2f}%")
    print(f"  CVaR (95%):          {portfolio.calculate_cvar(0.95) * 100:.2f}%")

    # Correlation analysis
    print("\nCorrelation Matrix:")
    print(portfolio.calculate_correlation_matrix())


def example_optimization():
    """Example: Portfolio optimization."""
    print("\n" + "=" * 60)
    print("EXAMPLE 3: Portfolio Optimization")
    print("=" * 60)

    # Fetch data
    dm = DataManager()
    tickers = ["VAS.AX", "VGS.AX", "VAP.AX"]
    dm.fetch_data(tickers)
    returns = dm.get_returns()

    # Initialize optimizer
    optimizer = PortfolioOptimizer(returns, RISK_FREE_RATE)

    # Max Sharpe Portfolio
    print("\n📈 Maximum Sharpe Ratio Portfolio:")
    max_sharpe = optimizer.optimize_max_sharpe()
    print("Weights:")
    for ticker, weight in max_sharpe.weights.items():
        print(f"  {ticker}: {weight * 100:.2f}%")
    print(f"Expected Return:  {max_sharpe.expected_return * 100:.2f}%")
    print(f"Volatility:       {max_sharpe.volatility * 100:.2f}%")
    print(f"Sharpe Ratio:     {max_sharpe.sharpe_ratio:.2f}")

    # Min Volatility Portfolio
    print("\n🛡️ Minimum Volatility Portfolio:")
    min_vol = optimizer.optimize_min_volatility()
    print("Weights:")
    for ticker, weight in min_vol.weights.items():
        print(f"  {ticker}: {weight * 100:.2f}%")
    print(f"Expected Return:  {min_vol.expected_return * 100:.2f}%")
    print(f"Volatility:       {min_vol.volatility * 100:.2f}%")
    print(f"Sharpe Ratio:     {min_vol.sharpe_ratio:.2f}")

    # Equal Weight
    print("\n⚖️ Equal Weight Portfolio:")
    equal_weight = optimizer.equal_weight()
    print("Weights:")
    for ticker, weight in equal_weight.weights.items():
        print(f"  {ticker}: {weight * 100:.2f}%")
    print(f"Expected Return:  {equal_weight.expected_return * 100:.2f}%")
    print(f"Volatility:       {equal_weight.volatility * 100:.2f}%")
    print(f"Sharpe Ratio:     {equal_weight.sharpe_ratio:.2f}")


def example_advanced_metrics():
    """Example: Advanced risk metrics."""
    print("\n" + "=" * 60)
    print("EXAMPLE 4: Advanced Risk Metrics")
    print("=" * 60)

    # Fetch data
    dm = DataManager()
    tickers = ["VAS.AX", "VGS.AX"]
    dm.fetch_data(tickers)
    returns = dm.get_returns()

    # Calculate advanced metrics
    print("\nAdvanced Metrics:")
    for ticker in tickers:
        if ticker in returns.columns:
            ret = returns[ticker]

            print(f"\n{ticker}:")
            print(f"  Skewness:         {MetricsCalculator.calculate_skewness(ret):.4f}")
            print(f"  Kurtosis:         {MetricsCalculator.calculate_kurtosis(ret):.4f}")
            print(f"  Win Rate:         {MetricsCalculator.calculate_win_rate(ret) * 100:.2f}%")

            stress = MetricsCalculator.calculate_stress_test(ret, percentile=5)
            print(f"  Worst Return:     {stress['worst_return'] * 100:.2f}%")
            print(f"  Worst 5 Avg:      {stress['worst_5_return'] * 100:.2f}%")
            print(f"  Worst 10 Avg:     {stress['worst_10_return'] * 100:.2f}%")


if __name__ == "__main__":
    print("\n🚀 Financial Modelling System - Usage Examples\n")

    example_basic_analysis()
    example_portfolio_analysis()
    example_optimization()
    example_advanced_metrics()

    print("\n" + "=" * 60)
    print("✅ Examples completed!")
    print("=" * 60)
