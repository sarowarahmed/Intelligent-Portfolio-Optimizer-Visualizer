import numpy as np
from pypfopt import EfficientFrontier, risk_models, expected_returns
def get_optimized_weights(data, method="max_sharpe"):
    
    # Calculate expected returns and sample covariance matrix
    mu = expected_returns.mean_historical_return(data)
    S = risk_models.sample_cov(data)

    # Initialize Efficient Frontier object
    ef = EfficientFrontier(mu, S)

    # Optimize for maximum Sharpe ratio or minimum volatility
    if method == "max_sharpe":
        weights = ef.max_sharpe()
    elif method == "min_volatility":
        weights = ef.min_volatility()
    else:
        raise ValueError("Invalid optimization method. Use 'max_sharpe' or 'min_volatility'.")

    # Clean the weights to remove any NaN values and convert to dictionary
    cleaned_weights = {k: v for k, v in weights.items() if not np.isnan(v) and v > 0}
    #or cleaned_weights = ef.clean_weights()
    return cleaned_weights, ef