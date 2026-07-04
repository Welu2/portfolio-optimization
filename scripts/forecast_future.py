import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from models.lstm_model import create_sequences, build_lstm, scale_data
from models.forecast import forecast_lstm, confidence_interval

df = pd.read_csv(
    "data/raw/TSLA.csv",
    parse_dates=["Date"],
    index_col="Date"
)

close = df["Close"].values

scaled, scaler = scale_data(close)

window = 60

X, y = create_sequences(scaled, window)

model = build_lstm(window)

model.fit(X, y, epochs=10, batch_size=32, verbose=1)

last_sequence = scaled[-window:]

future = forecast_lstm(
    model,
    last_sequence,
    scaler,
    steps=180
)

pred = model.predict(X, verbose=0)

pred = scaler.inverse_transform(pred)

actual = scaler.inverse_transform(y.reshape(-1, 1))

residual_std = np.std(actual - pred)

lower, upper = confidence_interval(future, residual_std)

future_dates = pd.date_range(
    start=df.index[-1] + pd.Timedelta(days=1),
    periods=180,
    freq="B"
)

plt.figure(figsize=(14,6))

plt.plot(df.index, df["Close"], label="Historical")

plt.plot(
    future_dates,
    future,
    label="Future Forecast",
    color="red"
)

plt.fill_between(
    future_dates,
    lower,
    upper,
    alpha=0.25,
    label="95% Confidence Interval"
)

plt.title("Tesla Future Forecast")
plt.xlabel("Date")
plt.ylabel("Close Price")

plt.legend()

plt.show()