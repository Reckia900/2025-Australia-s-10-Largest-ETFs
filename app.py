"""
Streamlit dashboard for visualizing and analyzing ETF portfolios.

Run with: streamlit run app.py
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
from datetime import datetime, timedelta
from scipy import stats

from financial_modelling import (
    DataManager,
    FinancialModel,
    PortfolioModel,
    MetricsCalculator,
    PortfolioOptimizer,
)
from financial_modelling.config import DEFAULT_ETFS, RISK_FREE_RATE


def format_percentage(value):
    """Format value as percentage string."""
    return f"{value * 100:.2f}%"


def format_number(value, decimals=2):
    """Format number with specified decimal places."""
    return f"{value:,.{decimals}f}"


def setup_page():
    """Setup Streamlit page configuration."""
    st.set_page_config(
        page_title="ETF Financial Modelling System",
        page_icon="📊",
        layout="wide",
        initial_sidebar_state="expanded",
    )
    
    # Custom CSS styling
    st.markdown("""
    <style>
        .main {
            padding-top: 0rem;
        }
        .metric-card {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            padding: 20px;
            border-radius: 10px;
            color: white;
            text-align: center;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        }
        .metric-value {
            font-size: 28px;
            font-weight: bold;
            margin: 10px 0;
        }
        .metric-label {
            font-size: 12px;
            opacity: 0.9;
            text-transform: uppercase;
            letter-spacing: 1px;
        }
        .header-container {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            padding: 30px;
            border-radius: 10px;
            color: white;
            margin-bottom: 30px;
        }
        .section-header {
            border-bottom: 3px solid #667eea;
            padding-bottom: 10px;
            margin-top: 30px;
            margin-bottom: 20px;
        }
    </style>
    """, unsafe_allow_html=True)
    
    # Header
    col1, col2 = st.columns([4, 1])
    with col1:
        st.markdown("""
        <div class="header-container">
            <h1>📊 Australian ETF Financial Modelling System</h1>
            <p style="margin-bottom: 0; opacity: 0.9;">Professional Analysis & Portfolio Optimization</p>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("### v1.0.0")


def load_data(tickers, start_date, end_date):
    """Load and cache ETF data."""
    dm = DataManager()
    data = dm.fetch_data(tickers, start_date.strftime("%Y-%m-%d"), end_date.strftime("%Y-%m-%d"))
    return dm


def sidebar_controls():
    """Create sidebar controls."""
    st.sidebar.markdown("## ⚙️ Configuration")
    
    st.sidebar.markdown("### 📈 ETF Selection")
    tickers = st.sidebar.multiselect(
        "Select ETFs",
        DEFAULT_ETFS,
        default=DEFAULT_ETFS[:3],
        help="Choose ETFs to analyze"
    )
    
    st.sidebar.markdown("### 📅 Time Period")
    col1, col2 = st.sidebar.columns(2)
    with col1:
        start_date = st.date_input(
            "Start Date", 
            datetime.now() - timedelta(days=365 * 5),
            help="Analysis start date"
        )
    with col2:
        end_date = st.date_input(
            "End Date", 
            datetime.now(),
            help="Analysis end date"
        )

    st.sidebar.markdown("### 💰 Risk-Free Rate")
    risk_free_rate = st.sidebar.slider(
        "Annual Risk-Free Rate", 
        0.0, 0.10, RISK_FREE_RATE, 0.01,
        format="%.1f%%",
        help="Used for Sharpe ratio calculations"
    )
    
    st.sidebar.divider()
    st.sidebar.markdown("### 📚 About")
    st.sidebar.info("""
    **Financial Modelling System**
    
    Professional analysis and optimization for Australian ETFs.
    
    🔹 Data: Yahoo Finance
    🔹 Framework: Modern Portfolio Theory
    🔹 License: MIT
    """)

    return tickers, start_date, end_date, risk_free_rate


def display_performance_metrics(dm, tickers, risk_free_rate):
    """Display individual ETF performance metrics."""
    st.markdown("<h2 class='section-header'>📈 Individual ETF Performance</h2>", unsafe_allow_html=True)

    cols = st.columns(min(3, max(1, len([t for t in tickers if t in dm.data]))))
    col_idx = 0
    
    for ticker in tickers:
        if ticker not in dm.data or dm.data[ticker].empty:
            continue

        prices = dm.data[ticker][ticker]
        model = FinancialModel(prices, risk_free_rate)
        metrics = model.calculate_metrics()

        with cols[col_idx % len(cols)]:
            st.metric(
                label=ticker,
                value=f"{metrics.annualized_return * 100:.2f}%",
                delta=f"Vol: {metrics.annualized_volatility * 100:.2f}%"
            )
            
            col_a, col_b = st.columns(2)
            with col_a:
                st.metric("Sharpe Ratio", f"{metrics.sharpe_ratio:.2f}")
            with col_b:
                st.metric("Max Drawdown", f"{metrics.max_drawdown * 100:.2f}%")
        
        col_idx += 1


def plot_price_history(dm, tickers):
    """Plot price history of selected ETFs."""
    st.markdown("<h2 class='section-header'>💹 Price History</h2>", unsafe_allow_html=True)

    combined_data = dm.get_combined_data()
    if combined_data.empty:
        st.warning("No data available")
        return

    # Create figure
    fig = go.Figure()
    colors = px.colors.qualitative.Set2
    
    for idx, ticker in enumerate(tickers):
        if ticker in combined_data.columns:
            normalized = combined_data[ticker] / combined_data[ticker].iloc[0] * 100
            fig.add_trace(
                go.Scatter(
                    x=combined_data.index,
                    y=normalized,
                    name=ticker,
                    mode="lines",
                    line=dict(width=2.5, color=colors[idx % len(colors)]),
                    hovertemplate=f"<b>{ticker}</b><br>Date: %{{x|%Y-%m-%d}}<br>Value: %{{y:.2f}}<extra></extra>"
                )
            )

    fig.update_layout(
        title="Normalized Price Performance (Base = 100)",
        xaxis_title="Date",
        yaxis_title="Normalized Value",
        hovermode="x unified",
        height=450,
        template="plotly_white",
        font=dict(size=11),
    )
    st.plotly_chart(fig, use_container_width=True)


def plot_returns_distribution(dm, tickers):
    """Plot distribution of returns."""
    st.markdown("<h2 class='section-header'>📊 Returns Distribution Analysis</h2>", unsafe_allow_html=True)

    returns = dm.get_returns()
    if returns.empty:
        st.warning("No returns data available")
        return

    cols = st.columns(min(2, len(tickers)))
    for idx, ticker in enumerate(tickers):
        if ticker not in returns.columns:
            continue

        with cols[idx % 2]:
            fig = go.Figure()
            fig.add_trace(
                go.Histogram(
                    x=returns[ticker],
                    nbinsx=50,
                    name=ticker,
                    marker_color='rgba(102, 126, 234, 0.7)',
                    opacity=0.75,
                    hovertemplate="<b>Return Range</b><br>Count: %{y}<extra></extra>"
                )
            )
            
            # Add normal distribution overlay
            mean = returns[ticker].mean()
            std = returns[ticker].std()
            x_range = np.linspace(returns[ticker].min(), returns[ticker].max(), 100)
            normal_dist = stats.norm.pdf(x_range, mean, std) * len(returns[ticker]) * (returns[ticker].max() - returns[ticker].min()) / 50
            
            fig.add_trace(
                go.Scatter(
                    x=x_range,
                    y=normal_dist,
                    name='Normal Distribution',
                    line=dict(color='red', width=2),
                    opacity=0.7,
                )
            )
            
            fig.update_layout(
                title=f"{ticker} Returns Distribution",
                xaxis_title="Daily Return",
                yaxis_title="Frequency",
                height=350,
                template="plotly_white",
                showlegend=True,
            )
            st.plotly_chart(fig, use_container_width=True)


def plot_correlation_heatmap(dm, tickers):
    """Plot correlation matrix heatmap."""
    st.markdown("<h2 class='section-header'>🔗 Correlation Matrix</h2>", unsafe_allow_html=True)

    returns = dm.get_returns()
    if returns.empty or len(returns.columns) < 2:
        st.warning("Need at least 2 ETFs for correlation analysis")
        return

    corr_matrix = returns.corr()

    fig = go.Figure(
        data=go.Heatmap(
            z=corr_matrix.values,
            x=corr_matrix.columns,
            y=corr_matrix.columns,
            colorscale="RdBu",
            zmid=0,
            zmin=-1,
            zmax=1,
            text=np.round(corr_matrix.values, 2),
            texttemplate="%{text}",
            textfont={"size": 11},
            hovertemplate="<b>%{x} vs %{y}</b><br>Correlation: %{z:.3f}<extra></extra>"
        )
    )
    fig.update_layout(
        title="Correlation Matrix - ETF Return Relationships",
        height=450,
        template="plotly_white",
    )
    st.plotly_chart(fig, use_container_width=True)
    
    # Correlation statistics
    st.markdown("### Correlation Statistics")
    col1, col2, col3 = st.columns(3)
    
    # Get upper triangle to avoid duplicates
    corr_values = corr_matrix.values[np.triu_indices_from(corr_matrix.values, k=1)]
    
    with col1:
        st.metric("Average Correlation", f"{corr_values.mean():.3f}")
    with col2:
        st.metric("Max Correlation", f"{corr_values.max():.3f}")
    with col3:
        st.metric("Min Correlation", f"{corr_values.min():.3f}")


def portfolio_optimization_section(dm, tickers, risk_free_rate):
    """Display portfolio optimization section."""
    st.markdown("<h2 class='section-header'>🎯 Portfolio Optimization</h2>", unsafe_allow_html=True)

    returns = dm.get_returns()
    if returns.empty or len(returns.columns) < 2:
        st.warning("Need at least 2 ETFs for optimization")
        return

    optimizer = PortfolioOptimizer(returns, risk_free_rate)

    # Strategy selection
    col1, col2, col3 = st.columns([2, 2, 2])
    with col1:
        strategy = st.selectbox(
            "Select Optimization Strategy:",
            ["Max Sharpe Ratio", "Min Volatility", "Equal Weight"],
            help="Choose portfolio optimization approach"
        )
    with col2:
        st.write("")  # Spacer
    with col3:
        st.write("")  # Spacer

    # Get optimized weights
    if strategy == "Max Sharpe Ratio":
        result = optimizer.optimize_max_sharpe()
        description = "Maximizes risk-adjusted returns (Sharpe ratio)"
    elif strategy == "Min Volatility":
        result = optimizer.optimize_min_volatility()
        description = "Minimizes portfolio volatility/risk"
    else:
        result = optimizer.equal_weight()
        description = "Equal allocation across all ETFs"

    st.info(f"**Strategy**: {description}")

    # Display weights and metrics side by side
    col_weights, col_metrics = st.columns([1, 1])

    with col_weights:
        st.markdown("#### Portfolio Allocation")
        weights_df = pd.DataFrame(
            {
                "ETF": result.weights.index,
                "Weight": result.weights.values,
                "Allocation %": (result.weights.values * 100),
            }
        )
        weights_df = weights_df[weights_df["Weight"] > 0.001].sort_values("Allocation %", ascending=False)
        
        # Display as formatted table
        display_df = weights_df.copy()
        display_df["Allocation %"] = display_df["Allocation %"].apply(lambda x: f"{x:.2f}%")
        st.dataframe(display_df, use_container_width=True, hide_index=True)

    with col_metrics:
        st.markdown("#### Performance Metrics")
        metric_col1, metric_col2 = st.columns(2)
        
        with metric_col1:
            st.metric("Expected Return", f"{result.expected_return * 100:.2f}%")
            st.metric("Volatility", f"{result.volatility * 100:.2f}%")
        with metric_col2:
            st.metric("Sharpe Ratio", f"{result.sharpe_ratio:.3f}")
            effective_n = 1 / (result.weights ** 2).sum()
            st.metric("Diversification", f"{effective_n:.2f} assets")

    # Allocation pie chart
    st.markdown("#### Visual Allocation")
    fig = go.Figure(
        data=[
            go.Pie(
                labels=weights_df["ETF"],
                values=weights_df["Allocation %"],
                hole=0.3,
                textinfo="label+percent",
                marker=dict(line=dict(color="white", width=2)),
                hovertemplate="<b>%{label}</b><br>%{value:.2f}%<br>Allocation: %{percent}<extra></extra>"
            )
        ]
    )
    fig.update_layout(
        title="Portfolio Allocation",
        height=400,
        template="plotly_white",
    )
    st.plotly_chart(fig, use_container_width=True)

    # Efficient frontier
    st.markdown("#### Efficient Frontier Analysis")
    
    try:
        with st.spinner("🔄 Generating efficient frontier..."):
            frontier = optimizer.generate_efficient_frontier(num_portfolios=100)

        fig = go.Figure()
        fig.add_trace(
            go.Scatter(
                x=frontier["volatilities"] * 100,
                y=frontier["returns"] * 100,
                mode="markers",
                marker=dict(
                    size=8,
                    color=frontier["sharpe_ratios"],
                    colorscale="Viridis",
                    showscale=True,
                    colorbar=dict(
                        title="Sharpe<br>Ratio",
                        thickness=15,
                        len=0.7,
                    ),
                    line=dict(width=0.5, color="white"),
                ),
                text=[f"Sharpe: {sr:.2f}" for sr in frontier["sharpe_ratios"]],
                hovertemplate="<b>Efficient Portfolio</b><br>Risk: %{x:.2f}%<br>Return: %{y:.2f}%<br>%{text}<extra></extra>",
            )
        )
        fig.add_trace(
            go.Scatter(
                x=[result.volatility * 100],
                y=[result.expected_return * 100],
                mode="markers+text",
                marker=dict(size=20, color="red", symbol="star", line=dict(width=2, color="white")),
                text=["Selected"],
                textposition="top center",
                name="Selected Portfolio",
                hovertemplate="<b>Your Portfolio</b><br>Risk: %{x:.2f}%<br>Return: %{y:.2f}%<extra></extra>",
            )
        )
        fig.update_layout(
            title="Efficient Frontier - Risk vs Return",
            xaxis_title="Volatility (Risk) %",
            yaxis_title="Expected Return %",
            height=450,
            hovermode="closest",
            template="plotly_white",
        )
        st.plotly_chart(fig, use_container_width=True)
    except Exception as e:
        st.error(f"Could not generate efficient frontier: {e}")


def main():
    """Main application logic."""
    setup_page()

    # Sidebar controls
    tickers, start_date, end_date, risk_free_rate = sidebar_controls()

    if not tickers:
        st.info("👈 **Please select at least one ETF from the sidebar to begin analysis**")
        
        # Show info about the system
        st.markdown("""
        ## 📖 About This System
        
        This financial modelling platform provides:
        
        - **📊 Performance Analysis**: Analyze individual ETF metrics
        - **📈 Price Tracking**: Monitor price movements over time
        - **🔗 Correlation Study**: Understand asset relationships
        - **🎯 Portfolio Optimization**: Build optimized portfolios
        - **💡 Risk Analysis**: Calculate VaR, Sharpe ratios, and more
        
        ### Getting Started:
        1. Select ETFs from the sidebar
        2. Choose your analysis period
        3. Navigate through the tabs to explore data
        4. Use the Optimization tab to build portfolios
        
        **Disclaimer**: This is for educational purposes. Not financial advice.
        """)
        return

    # Load data
    try:
        with st.spinner("📥 Loading ETF data from Yahoo Finance..."):
            dm = load_data(tickers, start_date, end_date)
    except Exception as e:
        st.error(f"❌ Error loading data: {e}")
        st.info("Please check your internet connection and try again.")
        return

    # Main content tabs
    tab1, tab2, tab3, tab4, tab5 = st.tabs(
        ["📊 Overview", "📈 Technical Analysis", "🔗 Correlation", "🎯 Optimization", "📋 Summary"]
    )

    with tab1:
        display_performance_metrics(dm, tickers, risk_free_rate)
        st.divider()
        plot_price_history(dm, tickers)

    with tab2:
        plot_returns_distribution(dm, tickers)
        
        # Additional statistics
        st.markdown("<h2 class='section-header'>📉 Return Statistics</h2>", unsafe_allow_html=True)
        returns = dm.get_returns()
        
        stats_cols = st.columns(len([t for t in tickers if t in returns.columns]))
        for idx, ticker in enumerate([t for t in tickers if t in returns.columns]):
            with stats_cols[idx]:
                st.markdown(f"### {ticker}")
                ret = returns[ticker]
                st.metric("Avg Daily Return", f"{ret.mean() * 100:.4f}%")
                st.metric("Daily Volatility", f"{ret.std() * 100:.4f}%")
                st.metric("Skewness", f"{ret.skew():.3f}")
                st.metric("Kurtosis", f"{ret.kurtosis():.3f}")

    with tab3:
        plot_correlation_heatmap(dm, tickers)

    with tab4:
        portfolio_optimization_section(dm, tickers, risk_free_rate)

    with tab5:
        st.markdown("<h2 class='section-header'>📋 Analysis Summary</h2>", unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("#### 📅 Analysis Period")
            st.write(f"**Start Date**: {start_date.strftime('%Y-%m-%d')}")
            st.write(f"**End Date**: {end_date.strftime('%Y-%m-%d')}")
            trading_days = len(dm.get_returns())
            st.write(f"**Trading Days**: {trading_days}")
        
        with col2:
            st.markdown("#### 📊 Selected ETFs")
            for ticker in tickers:
                if ticker in dm.data:
                    st.write(f"✓ {ticker}")
        
        st.divider()
        
        # Export data option
        st.markdown("#### 💾 Export Data")
        if st.button("📥 Download Analysis Data (CSV)"):
            csv = dm.get_combined_data().to_csv()
            st.download_button(
                label="Click to Download",
                data=csv,
                file_name=f"etf_analysis_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv",
                mime="text/csv"
            )

    # Footer
    st.divider()
    col1, col2, col3 = st.columns(3)
    with col1:
        st.caption("📊 Australian ETF Financial Modelling System v1.0.0")
    with col2:
        st.caption("Data from Yahoo Finance")
    with col3:
        st.caption("© 2025 Financial Analytics Team")


if __name__ == "__main__":
    main()
