import pandas as pd

def compute_volatility(df, window=14):
    """
    Rolling volatility of returns
    """
    df["returns"] = pd.to_numeric(df["returns"], errors="coerce")
    df["volatility"] = df["returns"].rolling(window).std()
    return df
