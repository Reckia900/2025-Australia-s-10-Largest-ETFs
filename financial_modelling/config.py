"""
Configuration and constants for the financial modelling system.
"""

from typing import Dict, List

# Australia's 10 Largest ETFs (as of 2025)
DEFAULT_ETFS: List[str] = [
    "VAS.AX",  # Vanguard Australian Shares
    "VGS.AX",  # Vanguard Global Shares
    "VGAD.AX",  # Vanguard Global Shares Hedged
    "VAP.AX",  # Vanguard Developed Markets Index
    "VAS.AX",  # Vanguard Australian Shares
    "IVV.AX",  # iShares Core S&P 500 ETF
    "IVE.AX",  # iShares Global Ex-Australia ETF
    "VAS.AX",  # Vanguard Australian Shares
    "DHHF.AX",  # Diversified High Yield Fund
    "VDHG.AX",  # Vanguard Diversified High Growth ETF
]

# Risk-free rate (Australian Government bonds)
RISK_FREE_RATE: float = 0.04  # 4% annually

# Annualization factor
TRADING_DAYS_PER_YEAR: int = 252

# Default date range
DEFAULT_LOOKBACK_YEARS: int = 5

# Performance periods (in days)
PERFORMANCE_PERIODS: Dict[str, int] = {
    "1_day": 1,
    "1_week": 5,
    "1_month": 21,
    "3_months": 63,
    "6_months": 126,
    "1_year": 252,
    "3_years": 756,
    "5_years": 1260,
}

# Risk metrics
VOLATILITY_WINDOW: int = 30  # 30-day rolling window
CORRELATION_WINDOW: int = 252  # Annual rolling window

# Portfolio constraints
MIN_ALLOCATION: float = 0.0  # Minimum allocation percentage
MAX_ALLOCATION: float = 1.0  # Maximum allocation percentage (100%)
