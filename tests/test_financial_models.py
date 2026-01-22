"""
Unit tests for the financial modelling system.
"""

import pytest
import numpy as np
import pandas as pd
from datetime import datetime, timedelta

from financial_modelling import (
    DataManager,
    FinancialModel,
    PortfolioModel,
    MetricsCalculator,
    PortfolioOptimizer,
)


@pytest.fixture
def sample_prices():
    """Create sample price data."""
    dates = pd.date_range(start="2023-01-01", periods=252, freq="D")
    prices = pd.Series(
        np.random.choice([100 * (1.001 ** i) for i in range(100)], size=252),
        index=dates,
    )
    return prices


@pytest.fixture
def sample_returns():
    """Create sample returns data."""
    dates = pd.date_range(start="2023-01-01", periods=252, freq="D")
    data = {
        "ETF1": np.random.normal(0.0005, 0.01, 252),
        "ETF2": np.random.normal(0.0005, 0.012, 252),
        "ETF3": np.random.normal(0.0006, 0.011, 252),
    }
    return pd.DataFrame(data, index=dates)


class TestFinancialModel:
    """Test FinancialModel class."""

    def test_annualized_return(self, sample_prices):
        """Test annualized return calculation."""
        model = FinancialModel(sample_prices)
        ret = model.calculate_annualized_return()
        assert isinstance(ret, float)

    def test_annualized_volatility(self, sample_prices):
        """Test annualized volatility calculation."""
        model = FinancialModel(sample_prices)
        vol = model.calculate_annualized_volatility()
        assert vol > 0

    def test_sharpe_ratio(self, sample_prices):
        """Test Sharpe ratio calculation."""
        model = FinancialModel(sample_prices)
        sharpe = model.calculate_sharpe_ratio()
        assert isinstance(sharpe, float)

    def test_max_drawdown(self, sample_prices):
        """Test max drawdown calculation."""
        model = FinancialModel(sample_prices)
        dd = model.calculate_max_drawdown()
        assert dd <= 0  # Drawdown should be negative

    def test_metrics(self, sample_prices):
        """Test metrics calculation."""
        model = FinancialModel(sample_prices)
        metrics = model.calculate_metrics()
        assert metrics.annualized_volatility > 0
        assert metrics.max_drawdown <= 0


class TestPortfolioModel:
    """Test PortfolioModel class."""

    def test_portfolio_return(self, sample_returns):
        """Test portfolio return calculation."""
        portfolio = PortfolioModel(sample_returns)
        ret = portfolio.calculate_portfolio_return()
        assert isinstance(ret, float)

    def test_portfolio_volatility(self, sample_returns):
        """Test portfolio volatility calculation."""
        portfolio = PortfolioModel(sample_returns)
        vol = portfolio.calculate_portfolio_volatility()
        assert vol > 0

    def test_correlation_matrix(self, sample_returns):
        """Test correlation matrix calculation."""
        portfolio = PortfolioModel(sample_returns)
        corr = portfolio.calculate_correlation_matrix()
        assert isinstance(corr, pd.DataFrame)
        assert corr.shape == (3, 3)

    def test_var_cvar(self, sample_returns):
        """Test VaR and CVaR calculation."""
        portfolio = PortfolioModel(sample_returns)
        var = portfolio.calculate_var()
        cvar = portfolio.calculate_cvar()
        assert var < cvar < 0  # Both should be negative


class TestMetricsCalculator:
    """Test MetricsCalculator class."""

    def test_calculate_returns(self, sample_prices):
        """Test return calculation."""
        returns = MetricsCalculator.calculate_returns(sample_prices)
        assert len(returns) < len(sample_prices)
        assert returns.notna().sum() > 0

    def test_cumulative_returns(self, sample_prices):
        """Test cumulative return calculation."""
        returns = MetricsCalculator.calculate_returns(sample_prices)
        cum_returns = MetricsCalculator.calculate_cumulative_returns(returns)
        assert cum_returns.iloc[0] == returns.iloc[0]

    def test_skewness(self, sample_prices):
        """Test skewness calculation."""
        returns = MetricsCalculator.calculate_returns(sample_prices)
        skew = MetricsCalculator.calculate_skewness(returns)
        assert isinstance(skew, float)

    def test_win_rate(self, sample_prices):
        """Test win rate calculation."""
        returns = MetricsCalculator.calculate_returns(sample_prices)
        wr = MetricsCalculator.calculate_win_rate(returns)
        assert 0 <= wr <= 1

    def test_herfindahl_index(self):
        """Test Herfindahl index calculation."""
        weights = pd.Series([0.5, 0.3, 0.2])
        hhi = MetricsCalculator.calculate_herfindahl_index(weights)
        assert 0 < hhi <= 1

    def test_effective_n(self):
        """Test effective number of positions."""
        weights = pd.Series([0.25, 0.25, 0.25, 0.25])
        effective_n = MetricsCalculator.calculate_effective_n(weights)
        assert effective_n == 4


class TestPortfolioOptimizer:
    """Test PortfolioOptimizer class."""

    def test_equal_weight(self, sample_returns):
        """Test equal weight portfolio."""
        optimizer = PortfolioOptimizer(sample_returns)
        result = optimizer.equal_weight()
        assert np.isclose(result.weights.sum(), 1.0)
        assert all(result.weights == 1/3)

    def test_max_sharpe(self, sample_returns):
        """Test max Sharpe optimization."""
        optimizer = PortfolioOptimizer(sample_returns)
        result = optimizer.optimize_max_sharpe()
        assert np.isclose(result.weights.sum(), 1.0)
        assert all(result.weights >= 0)

    def test_min_volatility(self, sample_returns):
        """Test min volatility optimization."""
        optimizer = PortfolioOptimizer(sample_returns)
        result = optimizer.optimize_min_volatility()
        assert np.isclose(result.weights.sum(), 1.0)
        assert all(result.weights >= 0)

    def test_efficient_frontier(self, sample_returns):
        """Test efficient frontier generation."""
        optimizer = PortfolioOptimizer(sample_returns)
        frontier = optimizer.generate_efficient_frontier(num_portfolios=20)
        assert "volatilities" in frontier
        assert "returns" in frontier
        assert len(frontier["volatilities"]) > 0


class TestDataManager:
    """Test DataManager class."""

    def test_initialization(self):
        """Test DataManager initialization."""
        dm = DataManager()
        assert dm.cache_dir is not None

    def test_get_combined_data_empty(self):
        """Test combined data with no data loaded."""
        dm = DataManager()
        data = dm.get_combined_data()
        assert data.empty


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
