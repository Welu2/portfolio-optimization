import os
from datetime import datetime
import yfinance as yf

os.makedirs("data/raw", exist_ok=True)

tickers = ["TSLA", "SPY", "BND"]
end_date = datetime.today().strftime("%Y-%m-%d")

for ticker in tickers:
    print(f"Downloading {ticker}...")

    df = yf.download(
        ticker,
        start="2015-01-01",
        end=end_date,
        auto_adjust=True,
        progress=False
    )

    if df.empty:
        print(f"Failed to download {ticker}")
        continue

    if hasattr(df.columns, "levels"):
        df.columns = df.columns.get_level_values(0)

    df = df.reset_index()

    df.to_csv(f"data/raw/{ticker}.csv", index=False)

    print(f"{ticker}: {len(df)} rows saved")