# Using Public Financial Datasets
# import yfinance as yf
# data = yf.download("SPY", start="2020-01-01", end="2024-01-01")

# forecasting.py

import numpy as np
import pandas as pd
import os

def generate_liquidity_data(output_path='data/liquidity_data.csv'):
    np.random.seed(42)
    dates = pd.date_range("2020-01-01", periods=1000)
    liquidity = 100 + np.cumsum(np.random.randn(1000)) + 0.05 * np.arange(1000)
    events = [0]*500 + [1]*500  # Event starts halfway

    df = pd.DataFrame({'date': dates, 'liquidity': liquidity, 'event': events})
    
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df.to_csv(output_path, index=False)
    print(f"✅ Sample data saved to {output_path}")

# Optional: call the function when the script is run directly
if __name__ == "__main__":
    generate_liquidity_data()


