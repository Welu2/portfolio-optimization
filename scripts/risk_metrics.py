import numpy as np

def sharpe_ratio(returns):

    rf = 0

    return np.sqrt(252) * (returns.mean() - rf) / returns.std()


def value_at_risk(returns, confidence=0.95):

    return np.percentile(returns, (1-confidence)*100)