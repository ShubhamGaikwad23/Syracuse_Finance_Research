import pandas as pd
from xgboost import XGBRegressor
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt

def prepare_features(df, lags=5):
    for i in range(1, lags+1):
        df[f'lag_{i}'] = df['liquidity'].shift(i)
    df.dropna(inplace=True)
    return df

def train_xgb(df):
    X = df[[f'lag_{i}' for i in range(1,6)]]
    y = df['liquidity']
    model = XGBRegressor()
    model.fit(X, y)
    return model

def plot_xgb_predictions(df, model):
    X = df[[f'lag_{i}' for i in range(1,6)]]
    preds = model.predict(X)
    plt.plot(df.index, df['liquidity'], label='Actual')
    plt.plot(df.index, preds, label='Predicted')
    plt.legend()
    plt.title('XGBoost Forecast')
    plt.savefig('visuals/xgb_forecast.png')
