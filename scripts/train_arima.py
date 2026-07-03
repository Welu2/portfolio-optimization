import pandas as pd
from src.train_test_split import time_split
from models.arima_model import train_arima
from models.evaluation import mae, rmse

print("Loading data...")

df = pd.read_csv("data/raw/TSLA.csv", parse_dates=["Date"])
df = df.set_index("Date")

# IMPORTANT FIX: enforce daily frequency
df = df.asfreq("B")  # business days

df = df.fillna(method="ffill")

train, test = time_split(df["Close"])

print("Training ARIMA model...")

model = train_arima(train, order=(5,1,0))

print("Forecasting...")

forecast = model.forecast(steps=len(test))

# FIX alignment
forecast = pd.Series(forecast, index=test.index)

print("Evaluating...")

print("ARIMA RESULTS")
print("MAE:", mae(test.values, forecast.values))
print("RMSE:", rmse(test.values, forecast.values))
