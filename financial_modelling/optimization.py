"""
Portfolio optimization module using various algorithms.
"""

import numpy as np
import pandas as pd
from scipy.optimize import minimize
from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass


@dataclass
class OptimizationResult:
    """Container for optimization results."""
    weights: pd.Series
    expected_return: float
    volatility: float
    sharpe_ratio: float


class PortfolioOptimizer:
    """Optimize portfolio allocations."""

    def __init__(
        self,
        returns: pd.DataFrame,
        risk_free_rate: float = 0.04,
        min_weight: float = 0.0,
        max_weight: float = 1.0,
    ):
        """
        Initialize PortfolioOptimizer.

        Args:
            returns: DataFrame of returns for assets
            risk_free_rate: Risk-free rate
            min_weight: Minimum weight per asset
            max_weight: Maximum weight per asset
        """
        self.returns = returns
        self.risk_free_rate = risk_free_rate
        self.min_weight = min_weight
        self.max_weight = max_weight
        self.expected_returns = returns.mean() * 252
        self.cov_matrix = returns.cov() * 252
        self.assets = returns.columns.tolist()

    def _calculate_portfolio_metrics(
        self, weights: np.ndarray
    ) -> Tuple[float, float, float]:
        """
        Calculate portfolio return, volatility, and Sharpe ratio.

        Returns:
            Tuple of (return, volatility, sharpe_ratio)
        """
        portfolio_return = np.sum(self.expected_returns.values * weights)
        portfolio_variance = np.dot(weights, np.dot(self.cov_matrix.values, weights))
        portfolio_volatility = np.sqrt(portfolio_variance)
        sharpe_ratio = (portfolio_return - self.risk_free_rate) / portfolio_volatility
        return portfolio_return, portfolio_volatility, sharpe_ratio

    def _negative_sharpe(self, weights: np.ndarray) -> float:
        """Objective function: negative Sharpe ratio (for minimization)."""
        _, _, sharpe = self._calculate_portfolio_metrics(weights)
        return -sharpe

    def _portfolio_volatility(self, weights: np.ndarray) -> float:
        """Objective function: portfolio volatility."""
        _, volatility, _ = self._calculate_portfolio_metrics(weights)
        return volatility

    def _negative_return(self, weights: np.ndarray) -> float:
        """Objective function: negative return (for minimization)."""
        return_val, _, _ = self._calculate_portfolio_metrics(weights)
        return -return_val

    def optimize_max_sharpe(self) -> OptimizationResult:
        """
        Find portfolio with maximum Sharpe ratio.

        Returns:
            OptimizationResult with optimal weights
        """
        n_assets = len(self.assets)
        initial_weights = np.array([1 / n_assets] * n_assets)

        bounds = tuple((self.min_weight, self.max_weight) for _ in range(n_assets))
        constraints = {"type": "eq", "fun": lambda x: np.sum(x) - 1}

        result = minimize(
            self._negative_sharpe,
            initial_weights,
            method="SLSQP",
            bounds=bounds,
            constraints=constraints,
            options={"ftol": 1e-9},
        )

        weights = pd.Series(result.x, index=self.assets)
        ret, vol, sharpe = self._calculate_portfolio_metrics(result.x)

        return OptimizationResult(weights=weights, expected_return=ret, volatility=vol, sharpe_ratio=sharpe)

    def optimize_min_volatility(self) -> OptimizationResult:
        """
        Find portfolio with minimum volatility (efficient frontier).

        Returns:
            OptimizationResult with optimal weights
        """
        n_assets = len(self.assets)
        initial_weights = np.array([1 / n_assets] * n_assets)

        bounds = tuple((self.min_weight, self.max_weight) for _ in range(n_assets))
        constraints = {"type": "eq", "fun": lambda x: np.sum(x) - 1}

        result = minimize(
            self._portfolio_volatility,
            initial_weights,
            method="SLSQP",
            bounds=bounds,
            constraints=constraints,
            options={"ftol": 1e-9},
        )

        weights = pd.Series(result.x, index=self.assets)
        ret, vol, sharpe = self._calculate_portfolio_metrics(result.x)

        return OptimizationResult(weights=weights, expected_return=ret, volatility=vol, sharpe_ratio=sharpe)

    def optimize_max_return(self) -> OptimizationResult:
        """
        Find portfolio with maximum expected return.

        Returns:
            OptimizationResult with optimal weights
        """
        n_assets = len(self.assets)
        initial_weights = np.array([1 / n_assets] * n_assets)

        bounds = tuple((self.min_weight, self.max_weight) for _ in range(n_assets))
        constraints = {"type": "eq", "fun": lambda x: np.sum(x) - 1}

        result = minimize(
            self._negative_return,
            initial_weights,
            method="SLSQP",
            bounds=bounds,
            constraints=constraints,
            options={"ftol": 1e-9},
        )

        weights = pd.Series(result.x, index=self.assets)
        ret, vol, sharpe = self._calculate_portfolio_metrics(result.x)

        return OptimizationResult(weights=weights, expected_return=ret, volatility=vol, sharpe_ratio=sharpe)

    def optimize_target_return(self, target_return: float) -> OptimizationResult:
        """
        Find minimum volatility portfolio for target return.

        Args:
            target_return: Target annual return

        Returns:
            OptimizationResult with optimal weights
        """
        n_assets = len(self.assets)
        initial_weights = np.array([1 / n_assets] * n_assets)

        bounds = tuple((self.min_weight, self.max_weight) for _ in range(n_assets))
        constraints = [
            {"type": "eq", "fun": lambda x: np.sum(x) - 1},
            {
                "type": "eq",
                "fun": lambda x: np.sum(self.expected_returns.values * x) - target_return,
            },
        ]

        result = minimize(
            self._portfolio_volatility,
            initial_weights,
            method="SLSQP",
            bounds=bounds,
            constraints=constraints,
            options={"ftol": 1e-9},
        )

        weights = pd.Series(result.x, index=self.assets)
        ret, vol, sharpe = self._calculate_portfolio_metrics(result.x)

        return OptimizationResult(weights=weights, expected_return=ret, volatility=vol, sharpe_ratio=sharpe)

    def generate_efficient_frontier(self, num_portfolios: int = 100) -> Dict[str, np.ndarray]:
        """
        Generate efficient frontier by optimizing for different target returns.

        Args:
            num_portfolios: Number of portfolios to generate

        Returns:
            Dictionary with volatilities, returns, and Sharpe ratios
        """
        # Generate target returns from min to max possible
        min_ret = self.optimize_min_volatility().expected_return
        max_ret = self.optimize_max_return().expected_return

        target_returns = np.linspace(min_ret, max_ret, num_portfolios)
        volatilities = []
        returns = []
        sharpes = []

        for target_ret in target_returns:
            try:
                result = self.optimize_target_return(target_ret)
                volatilities.append(result.volatility)
                returns.append(result.expected_return)
                sharpes.append(result.sharpe_ratio)
            except:
                continue

        return {
            "volatilities": np.array(volatilities),
            "returns": np.array(returns),
            "sharpe_ratios": np.array(sharpes),
        }

    def equal_weight(self) -> OptimizationResult:
        """Get equal-weight portfolio."""
        n_assets = len(self.assets)
        weights = np.array([1 / n_assets] * n_assets)
        weights_series = pd.Series(weights, index=self.assets)
        ret, vol, sharpe = self._calculate_portfolio_metrics(weights)

        return OptimizationResult(weights=weights_series, expected_return=ret, volatility=vol, sharpe_ratio=sharpe)

    def cap_weight(self, market_caps: Dict[str, float]) -> OptimizationResult:
        """
        Get market-cap weighted portfolio.

        Args:
            market_caps: Dictionary of asset -> market cap

        Returns:
            OptimizationResult with cap-weighted allocation
        """
        caps = np.array([market_caps.get(asset, 1.0) for asset in self.assets])
        weights = caps / caps.sum()
        weights_series = pd.Series(weights, index=self.assets)
        ret, vol, sharpe = self._calculate_portfolio_metrics(weights)

        return OptimizationResult(weights=weights_series, expected_return=ret, volatility=vol, sharpe_ratio=sharpe)
