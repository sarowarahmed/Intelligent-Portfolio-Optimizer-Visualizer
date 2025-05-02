import streamlit as st
import pandas as pd
import datetime
from data_fetch import fetch_price_data
from optimizer import get_optimized_weights
from utils import plot_portfolio_weights, calculate_cumulative_returns
