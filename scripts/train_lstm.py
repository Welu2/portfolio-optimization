import numpy as np
import pandas as pd
from models.lstm_model import create_sequences, build_lstm, scale_data
from models.evaluation import mae, rmse

df = pd.read_csv("data/raw/TSLA.csv", index_col="Date", parse_dates=True)

data = df["Close"].values

scaled, scaler = scale_data(data)

X, y = create_sequences(scaled, window=60)

split = int(len(X) * 0.8)

X_train, X_test = X[:split], X[split:]
y_train, y_test = y[:split], y[split:]

model = build_lstm(60)

model.fit(X_train, y_train, epochs=10, batch_size=32, verbose=1)

pred = model.predict(X_test)

pred = scaler.inverse_transform(pred)
y_test = scaler.inverse_transform(y_test.reshape(-1,1))

print("MAE:", mae(y_test, pred))
print("RMSE:", rmse(y_test, pred))