import yfinance as yf
import pandas as pd
import os


def fetch_market_data(ticker, start_date, end_date):
    """
    Fetch historical market data for a given index or stock.
    """
    data = yf.download(ticker, start=start_date, end=end_date)

    if data.empty:
        raise ValueError("No data fetched. Check ticker or date range.")

    data = data[['Open', 'High', 'Low', 'Close', 'Volume']]
    data.dropna(inplace=True)

    return data


if __name__ == "__main__":
    # ---- CONFIG ----
    TICKER = "^GSPC"          # S&P 500
    START_DATE = "2015-01-01"
    END_DATE = "2024-12-31"

    # Fetch data
    df = fetch_market_data(TICKER, START_DATE, END_DATE)

    # Save CSV in SAME folder as this file
    output_path = os.path.join(os.path.dirname(__file__), "market_data.csv")
    df.to_csv(output_path)

    print(f" Market data saved at: {output_path}")
    print(df.head())
