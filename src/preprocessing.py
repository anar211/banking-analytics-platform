"""
Enterprise Banking Analytics Platform
Data Preprocessing Module
"""

import pandas as pd


def standardize_columns(df: pd.DataFrame) -> pd.DataFrame:
    """Convert column names to lowercase and replace spaces with underscores."""
    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
    )
    return df


def handle_missing_values(df: pd.DataFrame) -> pd.DataFrame:
    """Fill missing numeric values with 0 and categorical values with 'Unknown'."""
    for column in df.columns:
        if pd.api.types.is_numeric_dtype(df[column]):
            df[column] = df[column].fillna(0)
        else:
            df[column] = df[column].fillna("Unknown")
    return df


def preprocess_data(df: pd.DataFrame) -> pd.DataFrame:
    """Run full preprocessing pipeline."""
    df = standardize_columns(df)
    df = handle_missing_values(df)
    return df
