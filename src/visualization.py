"""
Enterprise Banking Analytics Platform
Visualization Module
"""

import pandas as pd
import matplotlib.pyplot as plt


def plot_monthly_transactions(df: pd.DataFrame) -> None:
    """Plot monthly transaction volume."""
    monthly_data = (
        df.groupby("month")["transaction_amount"]
        .sum()
        .reset_index()
    )

    plt.figure(figsize=(10, 5))
    plt.plot(monthly_data["month"], monthly_data["transaction_amount"], marker="o")
    plt.title("Monthly Transaction Volume")
    plt.xlabel("Month")
    plt.ylabel("Transaction Volume")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


def plot_customer_segments(df: pd.DataFrame) -> None:
    """Plot customer segment distribution."""
    segment_data = df["customer_segment"].value_counts()

    plt.figure(figsize=(8, 5))
    segment_data.plot(kind="bar")
    plt.title("Customer Segment Distribution")
    plt.xlabel("Customer Segment")
    plt.ylabel("Number of Customers")
    plt.tight_layout()
    plt.show()
