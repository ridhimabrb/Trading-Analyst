import pandas as pd

def compute_returns(df):
    """
    Compute daily returns from Close prices
    """

    # Ensure Close is numeric
    df["Close"] = pd.to_numeric(df["Close"], errors="coerce")

    # Compute returns
    df["returns"] = df["Close"].pct_change(fill_method=None)

    return df
