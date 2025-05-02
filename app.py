import streamlit as st
import pandas as pd
import datetime
from data_fetch import fetch_price_data
from optimizer import get_optimized_weights
from utils import plot_portfolio_weights, calculate_cumulative_returns
import plotly.express as px

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

# --- Main Content ---
st.title("📈 Intelligent Portfolio Optimizer")
st.info("Optimize your investments intelligently with Modern Portfolio Theory (MPT)")

if optimize_btn:
    with st.spinner("Fetching data and optimizing... ⏳"):
        price_data = fetch_price_data(tickers, start_date, end_date)

        weights, ef = get_optimized_weights(price_data, method=method)
        cum_returns = calculate_cumulative_returns(price_data, weights)
    st.success("Optimization Complete! 🎯")

    # --- TABS ---
    tab1, tab2, tab3 = st.tabs(["📄 Data View", "📊 Portfolio Optimization", "📈 Performance"])

    # --- Tab 1: Data View ---
    with tab1:
        st.header("Historical Stock Prices")
        st.dataframe(price_data.tail(10))  

        st.subheader("Basic statistics")
        st.write(price_data.describe()) 

    # --- Tab 2: Portfolio Optimization ---
    with tab2:
        st.header("Optimized Portfolio Allocation")  
        st.write(weights)

        col1,col2 =st.columns(2)
        with col1:
            fig1 = plot_portfolio_weights(weights)  
            st.pyplot(fig1) 

        with col2:
            st.subheader("Expected Performance Matrices")
            performance = ef.portfolio_performance(verbose=True)
            st.write(f"Annual Return: {performance[0]:.2%}")
            st.write(f"Annual Volatility: {performance[1]:.2%}")
            st.write(f"Sharpe Ratio: {performance[2]:.2f}") 

    # --- Tab 3: Performance Visualization ---
    with tab3:
        st.header("Portfolio Performance Over Time")

        fig2 = px.line(cum_returns,
                       title="📈 Cumulative Returns",
                       labels={"value": "Cumulative Return", "index": "Date"},
                       template="plotly_white"   
        )
        st.plotly_chart(fig2, use_container_width=True)

        st.subheader("Return Distribution")
        returns = cum_returns.pct_change().dropna()
        fig3 = px.histogram(returns, nbins=50, title="Histogram of Daily Returns")
        st.plotly_chart(fig3, use_container_width=True)
