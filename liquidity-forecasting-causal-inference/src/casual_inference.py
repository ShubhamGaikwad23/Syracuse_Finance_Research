import statsmodels.api as sm
import matplotlib.pyplot as plt

def run_did(df):
    df['post'] = df['event']
    df['treated'] = 1  # Assume entire group is treated; customize as needed
    df['interaction'] = df['post'] * df['treated']
    X = df[['post', 'treated', 'interaction']]
    X = sm.add_constant(X)
    model = sm.OLS(df['liquidity'], X).fit()
    print(model.summary())
    return model

def plot_did_effect(df):
    df.groupby('event')['liquidity'].mean().plot(kind='bar')
    plt.title("Liquidity Before vs After Event")
    plt.savefig('visuals/did_effect.png')
