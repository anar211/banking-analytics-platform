"""
Enterprise Banking Analytics Platform
ETL Pipeline

This script demonstrates a basic ETL process:
1. Extract raw banking data
2. Transform and clean datasets
3. Prepare processed data for analytics and BI dashboards
"""

import pandas as pd


def load_data(file_path: str) -> pd.DataFrame:
    """Load raw data from a CSV file."""
    return pd.read_csv(file_path)


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """Basic data cleaning."""
    df = df.drop_duplicates()
    df = df.dropna(how="all")
    return df


def save_processed_data(df: pd.DataFrame, output_path: str) -> None:
    """Save processed dataset."""
    df.to_csv(output_path, index=False)


if __name__ == "__main__":
    print("ETL pipeline template for banking analytics project.")
