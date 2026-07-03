import matplotlib.pyplot as plt

def plot_close(df, ticker):

    plt.figure(figsize=(12,5))

    plt.plot(df.index, df["Close"])

    plt.title(f"{ticker} Closing Price")

    plt.grid()

    plt.show()


def daily_returns(df):

    return df["Close"].pct_change()


def rolling_volatility(df):

    returns = daily_returns(df)

    rolling_std = returns.rolling(30).std()

    plt.figure(figsize=(12,5))

    plt.plot(rolling_std)

    plt.title("30-Day Rolling Volatility")

    plt.show()