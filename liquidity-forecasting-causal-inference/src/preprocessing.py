# Data Preprocessing
import pandas as pd

def load_data(path):
    df = pd.read_csv(path, parse_dates=['date'])
    df.set_index('date', inplace=True)
    df['liquidity_diff'] = df['liquidity'].diff()
    df['rolling_mean'] = df['liquidity'].rolling(7).mean()
    df.dropna(inplace=True)
    return df