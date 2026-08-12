"""
Quantitative Finance Utilities
This module provides essential functions for financial calculations and analysis.
"""

import numpy as np
import math

def present_value(future_value: float, rate: float, periods: int) -> float:
    """
    Calculate the present value of a future sum of money.
    
    Args:
        future_value: The future sum of money
        rate: The interest rate (as a decimal)
        periods: Number of time periods
    
    Returns:
        The present value
    """
    return future_value / (1 + rate) ** periods

def future_value(present_value: float, rate: float, periods: int) -> float:
    """
    Calculate the future value of a current sum of money.
    
    Args:
        present_value: The current sum of money
        rate: The interest rate (as a decimal)
        periods: Number of time periods
    
    Returns:
        The future value
    """
    return present_value * (1 + rate) ** periods

def calculate_returns(prices: list[float]) -> list[float]:
    """
    Calculate the periodic returns from a series of prices.
    
    Args:
        prices: List of asset prices
    
    Returns:
        List of periodic returns
    """
    returns = []
    for i in range(1, len(prices)):
        periodic_return = (prices[i] - prices[i-1]) / prices[i-1]
        returns.append(periodic_return)
    return returns

def sharpe_ratio(returns: list[float], risk_free_rate: float) -> float:
    """
    Calculate the Sharpe ratio for a series of returns.
    
    Args:
        returns: List of periodic returns
        risk_free_rate: The risk-free rate (as a decimal)
    
    Returns:
        The Sharpe ratio
    """
    returns_array = np.array(returns)
    excess_returns = returns_array - risk_free_rate
    return np.mean(excess_returns) / np.std(excess_returns) if len(returns) > 1 else 0

def beta(asset_returns: list[float], market_returns: list[float]) -> float:
    """
    Calculate the beta of an asset relative to the market.
    
    Args:
        asset_returns: List of asset returns
        market_returns: List of market returns
    
    Returns:
        The beta value
    """
    if len(asset_returns) != len(market_returns):
        raise ValueError("Asset and market returns must have the same length")
    
    covariance = np.cov(asset_returns, market_returns)[0][1]
    market_variance = np.var(market_returns)
    return covariance / market_variance if market_variance != 0 else 0

def black_scholes(S: float, K: float, T: float, r: float, sigma: float, option_type: str = 'call') -> float:
    """
    Calculate option price using Black-Scholes formula.
    
    Args:
        S: Current stock price
        K: Strike price
        T: Time to expiration (in years)
        r: Risk-free interest rate
        sigma: Volatility of the underlying asset
        option_type: Type of option ('call' or 'put')
    
    Returns:
        Option price
    """
    d1 = (math.log(S/K) + (r + sigma**2/2)*T) / (sigma*math.sqrt(T))
    d2 = d1 - sigma*math.sqrt(T)
    
    if option_type.lower() == 'call':
        return S*norm_cdf(d1) - K*math.exp(-r*T)*norm_cdf(d2)
    else:  # put option
        return K*math.exp(-r*T)*norm_cdf(-d2) - S*norm_cdf(-d1)

def norm_cdf(x: float) -> float:
    """
    Calculate the cumulative distribution function of the standard normal distribution.
    
    Args:
        x: Input value
    
    Returns:
        Probability
    """
    return (1 + math.erf(x/math.sqrt(2))) / 2

# Example usage:
if __name__ == "__main__":
    # Present Value example
    print(f"Present value of $1000 in 5 years at 5% interest: ${present_value(1000, 0.05, 5):.2f}")
    
    # Returns calculation example
    stock_prices = [100, 102, 99, 105, 103]
    returns = calculate_returns(stock_prices)
    print(f"Stock returns: {[f'{r:.2%}' for r in returns]}")
    
    # Sharpe ratio example
    print(f"Sharpe ratio: {sharpe_ratio(returns, 0.02):.2f}")