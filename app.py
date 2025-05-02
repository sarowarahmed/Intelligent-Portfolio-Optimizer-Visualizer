import streamlit as st
import pandas as pd
import datetime
from data_fetch import fetch_price_data
from optimizer import get_optimized_weights
from utils import plot_portfolio_weights, calculate_cumulative_returns

# --- Page Configuration ---
st.set_page_config(page_title="Portfolio Optimizer", layout="wide")

# --- Sidebar ---
st.sidebar.header("User Input 📥")
tickers_input = st.sidebar.text_input("Enter Stock Tickers (comma separated)", value="AAPL, MSFT, GOOGL, AMZN, META")
tickers = [ticker.strip().upper() for ticker in tickers_input.split(",")]

start_date = st.sidebar.date_input("Start Date", value=datetime.date(2020, 1, 1), min_value=datetime.date(2000, 1, 1))
end_date = st.sidebar.date_input("End Date", value=datetime.date.today(), min_value=start_date)

method = st.sidebar.selectbox("Optimiation Method", ("max_sharpe", "min_volatility"))
optimize_btn = st.sidebar.button("🚀 Optimize Portfolio")

