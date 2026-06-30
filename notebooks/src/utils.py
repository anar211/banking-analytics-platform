"""
Enterprise Banking Analytics Platform
Utility Functions
"""

import pandas as pd


def load_csv(path: str) -> pd.DataFrame:
    """Load CSV file."""
    return pd.read_csv(path)


def save_csv(df: pd.DataFrame, path: str) -> None:
    """Save DataFrame to CSV."""
    df.to_csv(path, index=False)


def print_dataset_info(df: pd.DataFrame) -> None:
    """Display basic dataset information."""
    print("=" * 50)
    print("Dataset Information")
    print("=" * 50)
    print(df.info())
    print()
    print(df.describe(include="all"))
