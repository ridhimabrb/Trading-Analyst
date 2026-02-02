import pandas as pd
import numpy as np


def compute_rsi(df, window=14):
    delta = df["Close"].diff()

    gain = delta.clip(lower=0)
    loss = -delta.clip(upper=0)

    avg_gain = gain.rolling(window).mean()
    avg_loss = loss.rolling(window).mean()

    rs = avg_gain / avg_loss
    df["rsi"] = 100 - (100 / (1 + rs))
    return df


def compute_ma_trend(df, short=20, long=50):
    df["ma_short"] = df["Close"].rolling(short).mean()
    df["ma_long"] = df["Close"].rolling(long).mean()

    df["ma_trend"] = (df["ma_short"] > df["ma_long"]).astype(int)
    return df
