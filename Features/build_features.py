import pandas as pd
from Features.returns import compute_returns
from Features.volatility import compute_volatility
from Features.indicators import compute_rsi, compute_ma_trend


def build_features(csv_path):
    df = pd.read_csv(csv_path, index_col=0, parse_dates=True)

    df = compute_returns(df)
    df = compute_volatility(df)
    df = compute_rsi(df)
    df = compute_ma_trend(df)

    df.dropna(inplace=True)
    return df


if __name__ == "__main__":
    df = build_features("Data/market_data.csv")
    df.to_csv("Data/features.csv")
    print(" Features saved to Data/features.csv")
