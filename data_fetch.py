import yfinance as yf
import pandas as pd

import yfinance as yf
import pandas as pd

def fetch_price_data(tickers, start_date, end_date):
    data = yf.download(tickers, start=start_date, end=end_date, auto_adjust=True)
    
    if isinstance(tickers, str):
        return data[['Close']]  # always return a DataFrame
    else:
        return data['Close']