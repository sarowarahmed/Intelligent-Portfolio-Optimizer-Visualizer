# 📈 Intelligent Portfolio Optimizer
An interactive app to optimize to optimize stock portfolios based on MOdern Portfolio Theory Principles. 

## Features
- Fetch live stock price data
- Optimize portfolio for max sharp ratio
- Vizualize asset allocation and performance
- Dynamic easy-to-use stremlit interface

## requirements.txt
streamlit: For quickly turning data scripts into shareable web apps with minimal code.

pandas: For providing powerful data structures (DataFrame) and tools for data manipulation and analysis.

numpy: To Enable efficient numerical operations and array computing in Python.

matplotlib: A versatile library for creating static, interactive, and animated visualizations.

seaborn: Built on matplotlib, it simplifies statistical data visualization with high-level interfaces.

yfinance: For fetching historical market data (stocks, ETFs, etc.) from Yahoo Finance.

PyPortfolioOpt: To implement portfolio optimization techniques for maximizing returns and minimizing risk.

plotly: To create interactive, publication-quality graphs and dashboards for web-based visualizations.

## data_fetch.py
This function fetch_price_data uses the yfinance library to download historical stock price data and returns the adjusted closing prices for the given tickers and date range.

1. Input Parameters:
   - tickers (str/list): Stock symbol(s) (e.g; "AAPL" or ["AAPL", "MSFT"]).
   - start_date (str/datetime): Start date for data (e.g; "2020-01-01").
   - end_date (str/datetime): End date for data (e.g; "2024-12-31").  

2. yf.download():
   - download historical market data from Yahoo Finance.
   - returns a DataFrame with columns like 'Open', 'High', 'Low', 'Close', 'Adj_Close', 'Volume'.

3. ['Close'] Selection:
   - Extracts only the closing prices.(Yahoo Finance (via yfinance) didn't return the 'Adj Close' column)
   - auto_adjust=True to get prices already adjusted for splits/dividends

4. Return: returns a DataFrame where -
   - Rows = Dates(index)
   - Columns = Tickers (if multiple) or a single column (if one ticker)
   - If multiple tickers are passed (e.g., ["AAPL", "MSFT"]), the output will have a column for each.

5. Example Usage:

   import yfinance as yf
   
   price_data = fetch_price_data("AAPL", "2020-01-01", "2024-12-31")
   
   print(price_data.head())
   - Output:

       Date
       
    2020-01-02    74.06
    
    2020-01-03    73.43
    
    2020-01-06    74.15
    
    ...
    
    2023-12-29    193.58

## optimizer.py
This function get_optimized_weights uses PyPortfolioOpt to compute optimal portfolio weights by either maximizing the Sharpe ratio (risk-adjusted return) or minimizing volatility
    
1. Input Parameters:
   - data (pd.DataFrame): Historical adjusted closing prices (rows = dates, columns = assets)
   - method (str): Optimization strategy ("max_sharpe" or "min_volatility"). 

2. Calculate Expected Returns (mu):
   - Computes the average historical returns for each asset.

3. Calculate Covariance Matrix (S):
   - Estimates the covarinece matrix(risk) of asset returns.

4. Initialize Efficient Frontier (ef):
   - sets up the optimization problem using 'mu'(retirns) and 'S'(risk).

5. Optimize Weights:
   - If method="max_sharpe": Finds the portfolio with the highest Sharpe ratio (best risk-adjusted return).
   - If method="min_volatility": Finds the portfolio with the lowest possible volatility.

6. Cleaned_weights:
   - Rounds tiny weights to zero and noramlize the rest tos sum to 1.

7. Returns: 
   - cleaned_weights (dict): Optimal asset weights (e.g; {"AAPL": 0.6}, "MSFT": 0.4).
   - ef(efficientFrontier object): For further analysis (e.g., plotting the frontier).

8. Notes:
   - Sharpe ratio optimization balances high returns with low risk.
   - Min volatility optimization focuses on reducing risk (suitable for conservative investors.)         
   
   
   
   
   
   
   - Returns:
    dict: Dictionary with tickers as keys and optimized weights as values.
