# Portfolio Optimization 

## Project Overview

This project develops a data-driven investment strategy by combining financial time series forecasting with Modern Portfolio Theory (MPT). Historical market data is collected from Yahoo Finance for three representative assets:

- **TSLA** – Tesla Inc. (High-risk, high-growth equity)
- **SPY** – SPDR S&P 500 ETF Trust (Broad U.S. market exposure)
- **BND** – Vanguard Total Bond Market ETF (Low-risk bond market exposure)

The project consists of five tasks:

1. Data Extraction, Cleaning, and Exploratory Data Analysis
2. Time Series Forecasting (ARIMA & LSTM)
3. Future Market Trend Forecasting
4. Portfolio Optimization using Modern Portfolio Theory
5. Strategy Backtesting Against a Benchmark Portfolio

---

# Project Structure

```
portfolio-optimization/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── notebooks/
│   ├── Task1_EDA.ipynb
│   ├── Task2_Forecasting.ipynb
│   ├── Task3_FutureForecast.ipynb
│   ├── Task4_PortfolioOptimization.ipynb
│   └── Task5_Backtesting.ipynb
│
├── models/
│   ├── arima_model.py
│   ├── lstm_model.py
│   └── backtest.py
│
├── scripts/
│   ├── download_data.py
│   ├── train_arima.py
│   ├── train_lstm.py
│   └── backtest_strategy.py
│
├── src/
├── tests/
├── requirements.txt
└── README.md
```

---

# Task 1 – Data Collection and Exploratory Data Analysis

## Objectives

- Download historical financial data using Yahoo Finance
- Clean and preprocess the datasets
- Explore statistical properties
- Analyze volatility and risk
- Perform stationarity testing

## Analysis Performed

- Historical price visualization
- Daily percentage returns
- Rolling mean and rolling standard deviation
- Outlier detection
- Augmented Dickey-Fuller (ADF) Stationarity Test
- Value at Risk (VaR)
- Sharpe Ratio

## Deliverables

- Clean financial datasets
- Exploratory visualizations
- Risk analysis
- Stationarity interpretation

---

# Task 2 – Time Series Forecasting

Two forecasting approaches were implemented and compared.

## ARIMA Model

- Classical statistical forecasting model
- Chronological train/test split
- Forecast generation
- Hyperparameter selection

## LSTM Model

- Deep learning forecasting model
- 60-day sliding window sequences
- TensorFlow/Keras implementation
- Multi-layer LSTM architecture

## Evaluation Metrics

- MAE
- RMSE
- MAPE

## Model Comparison

| Model | MAE | RMSE | MAPE |
|------|------:|------:|------:|
| ARIMA | 53.50 | 69.14 | 16.84% |
| LSTM | 13.05 | 16.85 | 4.21% |

### Conclusion

The LSTM model outperformed the ARIMA model across all evaluation metrics, demonstrating a stronger ability to capture nonlinear relationships present in Tesla's historical stock prices.

---

# Task 3 – Future Market Forecasting

Using the best-performing forecasting model (LSTM), future Tesla prices were predicted for the next 6–12 months.

## Analysis Included

- Future price prediction
- Historical vs forecast visualization
- Confidence interval visualization
- Trend analysis
- Forecast uncertainty discussion
- Market opportunity assessment
- Risk assessment

## Key Findings

- Long-term trend direction
- Forecast uncertainty increases over time
- Wider confidence intervals indicate reduced certainty for long-term predictions

---

# Task 4 – Portfolio Optimization

Modern Portfolio Theory (MPT) was applied to construct an optimal investment portfolio.

## Assets

- TSLA
- SPY
- BND

## Analysis Performed

- Expected return estimation
- Historical covariance matrix
- Efficient Frontier generation
- Maximum Sharpe Ratio portfolio
- Minimum Volatility portfolio

## Visualizations

- Covariance heatmap
- Efficient Frontier
- Optimal portfolio identification

## Final Deliverables

- Portfolio weights
- Expected annual return
- Expected volatility
- Sharpe Ratio
- Portfolio recommendation

---

# Task 5 – Strategy Backtesting

The optimized portfolio was evaluated using historical data not used during model training.

## Benchmark Portfolio

- 60% SPY
- 40% BND

## Performance Evaluation

The following metrics were computed for both portfolios:

- Total Return
- Annualized Return
- Sharpe Ratio
- Maximum Drawdown

## Visualizations

- Strategy cumulative returns
- Benchmark cumulative returns
- Strategy vs Benchmark comparison

## Conclusion

The backtesting framework provides an initial evaluation of whether forecast-informed portfolio optimization can outperform a passive investment strategy. Results should be interpreted alongside practical considerations such as transaction costs, taxes, and changing market conditions.

---

# Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- yfinance
- Statsmodels
- TensorFlow / Keras
- Scikit-learn
- PyPortfolioOpt

---

# Installation

```bash
git clone <repository-url>

cd portfolio-optimization

python -m venv venv

source venv/bin/activate

pip install -r requirements.txt
```

---

# Running the Project

## Download Data

```bash
python scripts/download_data.py
```

## Train ARIMA

```bash
python -m scripts.train_arima
```

## Train LSTM

```bash
python -m scripts.train_lstm
```

## Run Portfolio Backtest

```bash
python -m scripts.backtest_strategy
```

## Launch Jupyter Notebook

```bash
jupyter notebook
```

---

# Key Business Insights

- Tesla provides high expected returns but exhibits significantly higher volatility than SPY and BND.
- LSTM achieved substantially better forecasting accuracy than ARIMA.
- Combining forecast-based expected returns with Modern Portfolio Theory enables more informed portfolio allocation.
- Portfolio diversification using SPY and BND helps reduce overall portfolio risk.
- Backtesting allows the optimized strategy to be objectively compared against a passive benchmark before practical deployment.

