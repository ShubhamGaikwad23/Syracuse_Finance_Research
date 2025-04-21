from statsmodels.tsa.statespace.sarimax import SARIMAX
import matplotlib.pyplot as plt

def train_sarima(train_series, order=(1,1,1), seasonal_order=(1,1,1,12)):
    model = SARIMAX(train_series, order=order, seasonal_order=seasonal_order)
    results = model.fit()
    return results

def forecast_plot(train_series, results, steps=30):
    forecast = results.get_forecast(steps=steps)
    conf_int = forecast.conf_int()
    forecast_values = forecast.predicted_mean
    
    plt.plot(train_series, label='Train')
    forecast_values.plot(label='Forecast')
    plt.fill_between(conf_int.index, conf_int.iloc[:, 0], conf_int.iloc[:, 1], alpha=0.3)
    plt.legend()
    plt.title("SARIMA Forecast")
    plt.savefig('visuals/sarima_forecast.png')
