"""
Financial models for analyzing ETF performance.
"""

import numpy as np
import pandas as pd
from typing import Optional, Tuple
from dataclasses import dataclass
from datetime import datetime


@dataclass
class FinancialMetrics:
    """Container for financial metrics."""
    annualized_return: float
    annualized_volatility: float
    sharpe_ratio: float
    sortino_ratio: float
    max_drawdown: float
    cumulative_return: float


class FinancialModel:
    """Base financial model for analyzing individual ETFs."""

    def __init__(self, prices: pd.Series, risk_free_rate: float = 0.04):
        """
        Initialize FinancialModel.

        Args:
            prices: Series of price data
            risk_free_rate: Risk-free rate for Sharpe ratio calculation
        """
        self.prices = prices
        self.risk_free_rate = risk_free_rate
        self.returns = prices.pct_change().dropna()

    def calculate_metrics(self) -> FinancialMetrics:
        """Calculate key financial metrics."""
        ann_return = self.calculate_annualized_return()
        ann_volatility = self.calculate_annualized_volatility()
        sharpe = self.calculate_sharpe_ratio(ann_return, ann_volatility)
        sortino = self.calculate_sortino_ratio(ann_return)
        max_dd = self.calculate_max_drawdown()
        cum_return = (1 + self.returns).prod() - 1

        return FinancialMetrics(
            annualized_return=ann_return,
            annualized_volatility=ann_volatility,
            sharpe_ratio=sharpe,
            sortino_ratio=sortino,
            max_drawdown=max_dd,
            cumulative_return=cum_return,
        )

    def calculate_annualized_return(self) -> float:
        """Calculate annualized return."""
        total_return = (self.prices.iloc[-1] / self.prices.iloc[0]) - 1
        years = len(self.prices) / 252
        if years == 0:
            return 0
        return (1 + total_return) ** (1 / years) - 1

    def calculate_annualized_volatility(self) -> float:
        """Calculate annualized volatility (standard deviation)."""
        return self.returns.std() * np.sqrt(252)

    def calculate_sharpe_ratio(
        self, annualized_return: Optional[float] = None, volatility: Optional[float] = None
    ) -> float:
        """
        Calculate Sharpe Ratio.

        Sharpe Ratio = (Return - Risk-Free Rate) / Volatility
        """
        if annualized_return is None:
            annualized_return = self.calculate_annualized_return()
        if volatility is None:
            volatility = self.calculate_annualized_volatility()

        # Handle Series case
        if isinstance(volatility, pd.Series):
            volatility = volatility.iloc[0] if len(volatility) > 0 else 0
        if isinstance(annualized_return, pd.Series):
            annualized_return = annualized_return.iloc[0] if len(annualized_return) > 0 else 0
            
        if volatility == 0:
            return 0
        return (annualized_return - self.risk_free_rate) / volatility

    def calculate_sortino_ratio(
        self, annualized_return: Optional[float] = None, target_return: float = 0
    ) -> float:
        """
        Calculate Sortino Ratio (focuses on downside volatility).

        Sortino Ratio = (Return - Target Return) / Downside Volatility
        """
        if annualized_return is None:
            annualized_return = self.calculate_annualized_return()
        
        # Handle Series case
        if isinstance(annualized_return, pd.Series):
            annualized_return = annualized_return.iloc[0] if len(annualized_return) > 0 else 0

        downside_returns = self.returns[self.returns < target_return]
        downside_volatility = downside_returns.std() * np.sqrt(252)
        
        # Handle Series case
        if isinstance(downside_volatility, pd.Series):
            downside_volatility = downside_volatility.iloc[0] if len(downside_volatility) > 0 else 0

        if downside_volatility == 0:
            return 0
        return (annualized_return - target_return) / downside_volatility

    def calculate_max_drawdown(self) -> float:
        """Calculate maximum drawdown from peak to trough."""
        cumulative = (1 + self.returns).cumprod()
        running_max = cumulative.expanding().max()
        drawdown = (cumulative - running_max) / running_max
        return drawdown.min()

    def calculate_rolling_volatility(self, window: int = 30) -> pd.Series:
        """Calculate rolling volatility."""
        return self.returns.rolling(window=window).std() * np.sqrt(252)

    def calculate_rolling_return(self, window: int = 252) -> pd.Series:
        """Calculate rolling annualized return."""
        return self.returns.rolling(window=window).apply(
            lambda x: (1 + x).prod() ** (252 / len(x)) - 1
        )


class PortfolioModel:
    """Model for analyzing portfolio of multiple ETFs."""

    def __init__(
        self, returns: pd.DataFrame, weights: Optional[pd.Series] = None, risk_free_rate: float = 0.04
    ):
        """
        Initialize PortfolioModel.

        Args:
            returns: DataFrame of returns for multiple assets
            weights: Series with weights for each asset (default: equal weight)
            risk_free_rate: Risk-free rate
        """
        self.returns = returns
        self.risk_free_rate = risk_free_rate

        if weights is None:
            weights = pd.Series(1 / len(returns.columns), index=returns.columns)
        self.weights = weights

    def set_weights(self, weights: pd.Series) -> None:
        """Set portfolio weights."""
        if not np.isclose(weights.sum(), 1.0):
            weights = weights / weights.sum()
        self.weights = weights

    def calculate_portfolio_return(self) -> float:
        """Calculate portfolio return."""
        return (self.returns.mean() * self.weights).sum() * 252

    def calculate_portfolio_volatility(self) -> float:
        """Calculate portfolio volatility."""
        cov_matrix = self.returns.cov() * 252
        portfolio_var = np.dot(self.weights.values, np.dot(cov_matrix, self.weights.values))
        return np.sqrt(portfolio_var)

    def calculate_portfolio_sharpe(self) -> float:
        """Calculate portfolio Sharpe ratio."""
        ret = self.calculate_portfolio_return()
        vol = self.calculate_portfolio_volatility()
        if vol == 0:
            return 0
        return (ret - self.risk_free_rate) / vol

    def calculate_correlation_matrix(self) -> pd.DataFrame:
        """Get correlation matrix of returns."""
        return self.returns.corr()

    def calculate_covariance_matrix(self) -> pd.DataFrame:
        """Get covariance matrix of returns."""
        return self.returns.cov() * 252

    def calculate_var(self, confidence: float = 0.95) -> float:
        """
        Calculate Value at Risk (VaR).

        Args:
            confidence: Confidence level (default 95%)

        Returns:
            VaR as percentage
        """
        portfolio_returns = (self.returns * self.weights.values).sum(axis=1)
        return np.percentile(portfolio_returns, (1 - confidence) * 100)

    def calculate_cvar(self, confidence: float = 0.95) -> float:
        """
        Calculate Conditional Value at Risk (CVaR).

        Args:
            confidence: Confidence level (default 95%)

        Returns:
            CVaR as percentage
        """
        portfolio_returns = (self.returns * self.weights.values).sum(axis=1)
        var = np.percentile(portfolio_returns, (1 - confidence) * 100)
        return portfolio_returns[portfolio_returns <= var].mean()

    def calculate_beta(self, market_returns: pd.Series) -> float:
        """Calculate portfolio beta relative to market."""
        portfolio_returns = (self.returns * self.weights.values).sum(axis=1)
        covariance = portfolio_returns.cov(market_returns)
        market_variance = market_returns.var()
        if market_variance == 0:
            return 0
        return covariance / market_variance

    def get_metrics_summary(self) -> dict:
        """Get summary of portfolio metrics."""
        return {
            "return": self.calculate_portfolio_return(),
            "volatility": self.calculate_portfolio_volatility(),
            "sharpe_ratio": self.calculate_portfolio_sharpe(),
            "var_95": self.calculate_var(0.95),
            "cvar_95": self.calculate_cvar(0.95),
        }
