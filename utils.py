import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def plot_portfolio_weights(weights):
    labels = list(weights.keys())
    sizes = list(weights.values())

    fig, ax = plt.subplots()
    ax.pie(sizes, labels = labels, autopct='%1.1f%%', startangle=140)
    ax.axis('equal')
    return fig

def calculate_cumulative_returns(price_data, weights):
    returns = price_data.pct_change().dropna()
    portfolio_returns = returns.dot(pd.series(weights))
    cumulative_returns = (1+portfolio_returns).cumprod()
    return cumulative_returns