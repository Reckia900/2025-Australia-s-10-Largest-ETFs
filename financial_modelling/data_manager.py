"""
Data management module for fetching and managing ETF data.
"""

import pandas as pd
import yfinance as yf
from datetime import datetime, timedelta
from typing import Optional, List, Dict
import os
import json


class DataManager:
    """Manages ETF data collection, storage, and retrieval."""

    def __init__(self, cache_dir: str = "data/cache"):
        """
        Initialize DataManager.

        Args:
            cache_dir: Directory to cache downloaded data
        """
        self.cache_dir = cache_dir
        self.data: Dict[str, pd.DataFrame] = {}
        self._ensure_cache_dir()

    def _ensure_cache_dir(self) -> None:
        """Ensure cache directory exists."""
        os.makedirs(self.cache_dir, exist_ok=True)

    def _get_cache_path(self, ticker: str, start_date: str, end_date: str) -> str:
        """Generate cache file path for ticker."""
        filename = f"{ticker}_{start_date}_{end_date}.parquet"
        return os.path.join(self.cache_dir, filename)

    def fetch_data(
        self,
        tickers: List[str],
        start_date: Optional[str] = None,
        end_date: Optional[str] = None,
        use_cache: bool = True,
    ) -> Dict[str, pd.DataFrame]:
        """
        Fetch historical data for ETFs.

        Args:
            tickers: List of ticker symbols
            start_date: Start date (YYYY-MM-DD)
            end_date: End date (YYYY-MM-DD)
            use_cache: Whether to use cached data

        Returns:
            Dictionary of ticker -> DataFrame with price data
        """
        if end_date is None:
            end_date = datetime.now().strftime("%Y-%m-%d")
        if start_date is None:
            start_date = (datetime.now() - timedelta(days=365*5)).strftime("%Y-%m-%d")

        results = {}
        for ticker in tickers:
            cache_path = self._get_cache_path(ticker, start_date, end_date)

            # Check cache
            if use_cache and os.path.exists(cache_path):
                results[ticker] = pd.read_parquet(cache_path)
                continue

            # Download data
            try:
                df = yf.download(ticker, start=start_date, end=end_date, progress=False)
                if df.empty:
                    print(f"Warning: No data found for {ticker}")
                    continue

                df = df[["Close"]].rename(columns={"Close": ticker})
                results[ticker] = df

                # Cache the data
                df.to_parquet(cache_path)
            except Exception as e:
                print(f"Error fetching {ticker}: {e}")

        self.data.update(results)
        return results

    def get_combined_data(self) -> pd.DataFrame:
        """Get all loaded data as a combined DataFrame."""
        if not self.data:
            return pd.DataFrame()
        return pd.concat(self.data.values(), axis=1)

    def get_returns(self, method: str = "log") -> pd.DataFrame:
        """
        Calculate returns from price data.

        Args:
            method: "log" for logarithmic or "simple" for simple returns

        Returns:
            DataFrame of returns
        """
        combined = self.get_combined_data()
        if combined.empty:
            return pd.DataFrame()

        if method == "log":
            returns = combined.pct_change().apply(lambda x: (1 + x).apply(__import__('numpy').log))
        else:
            returns = combined.pct_change()

        return returns.dropna()

    def get_info(self, ticker: str) -> Dict:
        """Get ETF information."""
        try:
            info = yf.Ticker(ticker).info
            return {
                "name": info.get("longName", "N/A"),
                "sector": info.get("sector", "N/A"),
                "market_cap": info.get("marketCap", "N/A"),
                "pe_ratio": info.get("trailingPE", "N/A"),
            }
        except Exception as e:
            print(f"Error fetching info for {ticker}: {e}")
            return {}

    def clear_cache(self) -> None:
        """Clear all cached data."""
        import shutil
        if os.path.exists(self.cache_dir):
            shutil.rmtree(self.cache_dir)
        self._ensure_cache_dir()

    def export_data(self, filepath: str) -> None:
        """Export combined data to CSV."""
        combined = self.get_combined_data()
        combined.to_csv(filepath)
        print(f"Data exported to {filepath}")

    def import_data(self, filepath: str) -> pd.DataFrame:
        """Import data from CSV."""
        df = pd.read_csv(filepath, index_col=0, parse_dates=True)
        return df
