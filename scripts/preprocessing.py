import pandas as pd

def preprocess(df):

    df = df.copy()

    df = df.sort_index()

    df = df.ffill()

    df = df.bfill()

    return df