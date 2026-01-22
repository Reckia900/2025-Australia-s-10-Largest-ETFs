"""
Financial Modelling System for Australia's 10 Largest ETFs

This package provides tools for:
- Data collection and management
- Financial metrics calculation
- Portfolio optimization
- Risk analysis
- Performance visualization
"""

__version__ = "1.0.0"
__author__ = "Financial Analytics Team"

from .data_manager import DataManager
from .models import FinancialModel, PortfolioModel
from .metrics import MetricsCalculator
from .optimization import PortfolioOptimizer

__all__ = [
    "DataManager",
    "FinancialModel",
    "PortfolioModel",
    "MetricsCalculator",
    "PortfolioOptimizer",
]
