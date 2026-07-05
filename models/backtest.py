import pandas as pd
import numpy as np


def portfolio_returns(returns, weights):
    """
    Calculate daily portfolio returns.
    """
    w = np.array(weights)
    return returns.dot(w)


def cumulative_returns(daily_returns):
    return (1 + daily_returns).cumprod()


def annual_return(daily_returns):
    return (1 + daily_returns.mean()) ** 252 - 1


def sharpe_ratio(daily_returns, rf=0):
    excess = daily_returns - rf / 252
    return np.sqrt(252) * excess.mean() / excess.std()


def max_drawdown(cumulative):
    running_max = cumulative.cummax()
    drawdown = cumulative / running_max - 1
    return drawdown.min()