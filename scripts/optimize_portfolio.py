import pandas as pd
import numpy as np

from pypfopt import risk_models

from models.portfolio import (
    optimize_portfolio,
    minimum_volatility,
    plot_frontier,
)

assets = {}

for ticker in ["TSLA", "SPY", "BND"]:

    df = pd.read_csv(
        f"data/raw/{ticker}.csv",
        parse_dates=["Date"],
        index_col="Date",
    )

    assets[ticker] = df["Close"]

prices = pd.DataFrame(assets)

returns = prices.pct_change().dropna()

covariance = risk_models.sample_cov(prices)

expected_returns = pd.Series({
    "TSLA": 0.18,
    "SPY": returns["SPY"].mean() * 252,
    "BND": returns["BND"].mean() * 252,
})

weights, performance = optimize_portfolio(
    expected_returns,
    covariance,
)

print("Maximum Sharpe Portfolio")
print(weights)

print(performance)

weights2, performance2 = minimum_volatility(
    expected_returns,
    covariance,
)

print("\nMinimum Volatility Portfolio")
print(weights2)

print(performance2)

plot_frontier(expected_returns, covariance)