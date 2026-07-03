import pandas as pd

def daily_returns(df):

    return df["Close"].pct_change()