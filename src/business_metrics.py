"""
Enterprise Banking Analytics Platform
Business Metrics Calculation
"""

import pandas as pd


def load_data(path: str) -> pd.DataFrame:
    return pd.read_csv(path)


def calculate_conversion_rate(df: pd.DataFrame) -> float:
    total_clients = len(df)
    subscribed_clients = len(df[df["y"] == "yes"])
    return round((subscribed_clients / total_clients) * 100, 2)


def conversion_by_job(df: pd.DataFrame) -> pd.DataFrame:
    return (
        df.groupby("job")["y"]
        .apply(lambda x: (x == "yes").mean() * 100)
        .reset_index(name="conversion_rate")
        .sort_values(by="conversion_rate", ascending=False)
    )


def conversion_by_education(df: pd.DataFrame) -> pd.DataFrame:
    return (
        df.groupby("education")["y"]
        .apply(lambda x: (x == "yes").mean() * 100)
        .reset_index(name="conversion_rate")
        .sort_values(by="conversion_rate", ascending=False)
    )


def average_balance_by_subscription(df: pd.DataFrame) -> pd.DataFrame:
    return (
        df.groupby("y")["balance"]
        .mean()
        .reset_index(name="average_balance")
    )


if __name__ == "__main__":
    df = load_data("data/raw/bank-full.csv")

    print("Overall Conversion Rate:")
    print(calculate_conversion_rate(df), "%")

    print("\nConversion by Job:")
    print(conversion_by_job(df))

    print("\nConversion by Education:")
    print(conversion_by_education(df))

    print("\nAverage Balance by Subscription:")
    print(average_balance_by_subscription(df))
