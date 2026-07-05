import pandas as pd
import matplotlib.pyplot as plt

from models.backtest import (
    portfolio_returns,
    cumulative_returns,
    annual_return,
    sharpe_ratio,
    max_drawdown,
)

# Load data
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

# Backtesting period
returns = returns.loc["2025-01-01":"2026-01-01"]

# Replace with your Task 4 optimized weights
strategy_weights = [0.30, 0.20, 0.50]

# Benchmark: 60% SPY / 40% BND
benchmark_weights = [0.00, 0.60, 0.40]

strategy = portfolio_returns(returns, strategy_weights)
benchmark = portfolio_returns(returns, benchmark_weights)

cum_strategy = cumulative_returns(strategy)
cum_benchmark = cumulative_returns(benchmark)

plt.figure(figsize=(12, 6))

plt.plot(cum_strategy, label="Strategy")
plt.plot(cum_benchmark, label="Benchmark")

plt.title("Portfolio Backtest")
plt.xlabel("Date")
plt.ylabel("Cumulative Return")

plt.legend()
plt.show()

print("\nStrategy")
print("Total Return:", cum_strategy.iloc[-1] - 1)
print("Annual Return:", annual_return(strategy))
print("Sharpe:", sharpe_ratio(strategy))
print("Max Drawdown:", max_drawdown(cum_strategy))

print("\nBenchmark")
print("Total Return:", cum_benchmark.iloc[-1] - 1)
print("Annual Return:", annual_return(benchmark))
print("Sharpe:", sharpe_ratio(benchmark))
print("Max Drawdown:", max_drawdown(cum_benchmark))