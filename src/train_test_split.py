import pandas as pd

def time_split(df, train_end="2024-12-31"):
    train = df.loc[df.index <= train_end]
    test = df.loc[df.index > train_end]
    return train, test