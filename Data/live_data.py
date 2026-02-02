import yfinance as yf
import pandas as pd

def fetch_live_data(ticker, period="6mo", interval="1d"):
    df = yf.download(ticker, period=period, interval=interval)

    if isinstance(df.columns, pd.MultiIndex):
        df.columns = df.columns.get_level_values(0)

    df.dropna(inplace=True)
    return df
