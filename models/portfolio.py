import pandas as pd
from pypfopt import EfficientFrontier
from pypfopt import plotting
import matplotlib.pyplot as plt


def optimize_portfolio(expected_returns, covariance):
    ef = EfficientFrontier(expected_returns, covariance)

    weights = ef.max_sharpe()

    cleaned = ef.clean_weights()

    performance = ef.portfolio_performance(verbose=False)

    return cleaned, performance


def minimum_volatility(expected_returns, covariance):
    ef = EfficientFrontier(expected_returns, covariance)

    weights = ef.min_volatility()

    cleaned = ef.clean_weights()

    performance = ef.portfolio_performance(verbose=False)

    return cleaned, performance


def plot_frontier(expected_returns, covariance):
    ef = EfficientFrontier(expected_returns, covariance)

    fig, ax = plt.subplots(figsize=(8,6))

    plotting.plot_efficient_frontier(ef, ax=ax)

    ax.set_title("Efficient Frontier")

    plt.show()