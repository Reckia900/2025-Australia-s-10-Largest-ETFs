"""
Metrics calculation module for detailed financial analysis.
"""

import numpy as np
import pandas as pd
from typing import Dict, Tuple, List
from datetime import datetime, timedelta


class MetricsCalculator:
    """Calculate comprehensive financial metrics."""

    @staticmethod
    def calculate_returns(
        prices: pd.Series, method: str = "simple", periods: int = 1
    ) -> pd.Series:
        """
        Calculate returns.

        Args:
            prices: Series of prices
            method: "simple" or "log"
            periods: Number of periods for return calculation

        Returns:
            Series of returns
        """
        if method == "log":
            return np.log(prices / prices.shift(periods))
        else:
            return prices.pct_change(periods=periods)

    @staticmethod
    def calculate_cumulative_returns(returns: pd.Series) -> pd.Series:
        """Calculate cumulative returns over time."""
        return (1 + returns).cumprod() - 1

    @staticmethod
    def calculate_volatility(
        returns: pd.Series, periods_per_year: int = 252
    ) -> float:
        """Calculate annualized volatility."""
        return returns.std() * np.sqrt(periods_per_year)

    @staticmethod
    def calculate_skewness(returns: pd.Series) -> float:
        """Calculate skewness of returns."""
        return returns.skew()

    @staticmethod
    def calculate_kurtosis(returns: pd.Series) -> float:
        """Calculate kurtosis of returns."""
        return returns.kurtosis()

    @staticmethod
    def calculate_win_rate(returns: pd.Series) -> float:
        """Calculate percentage of positive returns."""
        if len(returns) == 0:
            return 0
        return (returns > 0).sum() / len(returns)

    @staticmethod
    def calculate_recovery_factor(total_return: float, max_drawdown: float) -> float:
        """
        Calculate recovery factor.

        Recovery Factor = Total Return / Max Drawdown
        Higher values indicate better risk-adjusted returns.
        """
        if max_drawdown == 0:
            return 0
        return total_return / abs(max_drawdown)

    @staticmethod
    def calculate_calmar_ratio(
        annualized_return: float, max_drawdown: float
    ) -> float:
        """
        Calculate Calmar Ratio.

        Calmar Ratio = Annualized Return / Max Drawdown
        """
        if max_drawdown == 0:
            return 0
        return annualized_return / abs(max_drawdown)

    @staticmethod
    def calculate_information_ratio(
        portfolio_returns: pd.Series,
        benchmark_returns: pd.Series,
        periods_per_year: int = 252,
    ) -> float:
        """
        Calculate Information Ratio.

        Information Ratio = (Portfolio Return - Benchmark Return) / Tracking Error
        """
        excess_returns = portfolio_returns - benchmark_returns
        tracking_error = excess_returns.std() * np.sqrt(periods_per_year)
        if tracking_error == 0:
            return 0
        mean_excess = excess_returns.mean() * periods_per_year
        return mean_excess / tracking_error

    @staticmethod
    def calculate_treynor_ratio(
        portfolio_return: float, beta: float, risk_free_rate: float
    ) -> float:
        """
        Calculate Treynor Ratio.

        Treynor Ratio = (Portfolio Return - Risk-Free Rate) / Beta
        """
        if beta == 0:
            return 0
        return (portfolio_return - risk_free_rate) / beta

    @staticmethod
    def calculate_monte_carlo_var(
        returns: pd.Series, confidence: float = 0.95, simulations: int = 10000
    ) -> Tuple[float, float]:
        """
        Calculate VaR and CVaR using Monte Carlo simulation.

        Args:
            returns: Series of returns
            confidence: Confidence level
            simulations: Number of simulations

        Returns:
            Tuple of (VaR, CVaR)
        """
        mean = returns.mean()
        std = returns.std()

        # Generate random returns
        simulated_returns = np.random.normal(mean, std, simulations)

        # Calculate VaR and CVaR
        var = np.percentile(simulated_returns, (1 - confidence) * 100)
        cvar = simulated_returns[simulated_returns <= var].mean()

        return var, cvar

    @staticmethod
    def calculate_rolling_metrics(
        returns: pd.Series, window: int = 252
    ) -> Dict[str, pd.Series]:
        """
        Calculate rolling metrics.

        Args:
            returns: Series of returns
            window: Window size in periods

        Returns:
            Dictionary of rolling metrics
        """
        return {
            "volatility": returns.rolling(window).std() * np.sqrt(252),
            "return": returns.rolling(window).mean() * 252,
            "skewness": returns.rolling(window).skew(),
            "kurtosis": returns.rolling(window).apply(
                lambda x: x.kurtosis() if len(x) > 0 else np.nan
            ),
        }

    @staticmethod
    def calculate_herfindahl_index(weights: pd.Series) -> float:
        """
        Calculate Herfindahl-Hirschman Index (HHI).

        HHI measures concentration of portfolio. Values closer to 1 indicate
        more concentrated portfolios.

        HHI = Sum of (weight_i)^2
        """
        return (weights ** 2).sum()

    @staticmethod
    def calculate_effective_n(weights: pd.Series) -> float:
        """
        Calculate effective number of positions.

        Effective N = 1 / HHI

        Shows diversification benefit.
        """
        hhi = (weights ** 2).sum()
        if hhi == 0:
            return 0
        return 1 / hhi

    @staticmethod
    def calculate_stress_test(
        returns: pd.Series, percentile: float = 1.0
    ) -> Dict[str, float]:
        """
        Calculate stress test metrics for extreme scenarios.

        Args:
            returns: Series of returns
            percentile: Percentile for stress scenario

        Returns:
            Dictionary of stress metrics
        """
        worst_returns = returns.nsmallest(int(len(returns) * percentile / 100))
        return {
            "worst_return": worst_returns.min(),
            "avg_worst_return": worst_returns.mean(),
            "worst_5_return": returns.nsmallest(5).mean(),
            "worst_10_return": returns.nsmallest(10).mean(),
        }
