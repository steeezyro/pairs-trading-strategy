import numpy as np
import pandas as pd
import yfinance as yf
from statsmodels.tsa.stattools import coint

# -------------------------------------------
# 1. Data Import
# -------------------------------------------
def get_data(tickers, start, end):
    df = yf.download(tickers, start=start, end=end)["Close"]
    df.columns = tickers
    return df

# -------------------------------------------
# 2. Cointegration Test
# -------------------------------------------
def test_cointegration(series1, series2):
    score, pvalue, _ = coint(series1, series2)
    return pvalue

# -------------------------------------------
# 3. Spread + Rolling Z-score
# -------------------------------------------
def calculate_spread(df, asset1, asset2):
    return df[asset1] - df[asset2]

def compute_rolling_zscore(spread, window):
    mean = spread.rolling(window=window).mean()
    std = spread.rolling(window=window).std()
    return (spread - mean) / std

# -------------------------------------------
# 4. Signal Generator
# -------------------------------------------
def generate_signals(zscore, upper=1, lower=-1):
    signals = pd.Series(index=zscore.index, dtype='float64')
    signals[zscore > upper] = -1  # Short spread
    signals[zscore < lower] = 1   # Long spread
    signals[(zscore >= lower) & (zscore <= upper)] = 0  # Neutral
    return signals

# -------------------------------------------
# 5. Backtest Engine
# -------------------------------------------
def backtest_strategy(signals, returns):
    return signals.shift(1) * (returns.iloc[:, 0] - returns.iloc[:, 1])

# -------------------------------------------
# 6. Performance Evaluation
# -------------------------------------------
def evaluate_performance(strategy_returns, cumulative_returns, rf_annual=0.045):
    rf_daily = rf_annual / 252
    excess_returns = strategy_returns - rf_daily
    sharpe = np.sqrt(252) * excess_returns.mean() / excess_returns.std()
    total_return = cumulative_returns.iloc[-1] - 1
    rolling_max = cumulative_returns.cummax()
    drawdown = cumulative_returns / rolling_max - 1
    max_drawdown = drawdown.min()
    n_days = len(strategy_returns.dropna())
    cagr = (1 + total_return) ** (252 / n_days) - 1

    return {
        "Sharpe Ratio": round(sharpe, 2),
        "Total Return": f"{total_return:.2%}",
        "Max Drawdown": f"{max_drawdown:.2%}",
        "CAGR": f"{cagr:.2%}"
    }

