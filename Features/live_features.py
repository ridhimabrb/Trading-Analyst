import pandas as pd
from Features.returns import compute_returns
from Features.volatility import compute_volatility
from Features.indicators import compute_rsi, compute_ma_trend

# MUST MATCH TRAINING FEATURES EXACTLY
FEATURE_COLUMNS = [
    "returns",
    "volatility",
    "rsi",
    "ma_short",
    "ma_long"
]

def build_live_features(df):
    df = compute_returns(df)
    df = compute_volatility(df)
    df = compute_rsi(df)
    df = compute_ma_trend(df)

    df.dropna(inplace=True)
    return df[FEATURE_COLUMNS]
