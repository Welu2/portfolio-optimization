# Portfolio-Optimization


## Project Overview

This project analyzes and forecasts financial assets:

- TSLA (Tesla)
- SPY (S&P 500 ETF)
- BND (Bond ETF)

It includes:
1. Exploratory Data Analysis (Task 1)
2. Time Series Forecasting (Task 2)

---

# Task 1: Data Analysis

### Key Steps
- Data collection via Yahoo Finance
- Cleaning & preprocessing
- Exploratory Data Analysis
- Volatility analysis
- Stationarity testing (ADF)
- Risk metrics (Sharpe Ratio, VaR)

---

# Task 2: Forecasting Models

### Models Implemented

#### 1. ARIMA Model
- Statistical time series model
- Tuned using (p,d,q)
- Suitable for linear dependencies

#### 2. LSTM Model
- Deep learning sequence model
- Uses 60-day sliding window
- Captures nonlinear patterns

---

# Evaluation Metrics

- MAE (Mean Absolute Error)
- RMSE (Root Mean Squared Error)
- MAPE (Mean Absolute Percentage Error)

---

# Results Summary

- ARIMA performs well for short-term linear trends
- LSTM performs better for complex nonlinear patterns
- LSTM requires more data and computation

---

# How to Run

```bash
pip install -r requirements.txt

python scripts/download_data.py

python scripts/train_arima.py
python scripts/train_lstm.py
