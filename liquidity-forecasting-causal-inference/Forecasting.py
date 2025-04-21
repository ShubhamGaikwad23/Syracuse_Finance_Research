# Using Public Financial Datasets
import yfinance as yf
data = yf.download("SPY", start="2020-01-01", end="2024-01-01")

# Or Simulate Data
# import numpy as np
# import pandas as pd

# np.random.seed(42)
# dates = pd.date_range("2020-01-01", periods=1000)
# liquidity = 100 + np.cumsum(np.random.randn(1000)) + 0.05*np.arange(1000)
# events = [0]*500 + [1]*500  # market event starts halfway

# df = pd.DataFrame({'date': dates, 'liquidity': liquidity, 'event': events})
# df.to_csv('data/liquidity_data.csv', index=False)



