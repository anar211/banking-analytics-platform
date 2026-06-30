"""
Enterprise Banking Analytics Platform
Data Cleaning Pipeline
"""

import pandas as pd


def clean_bank_data(input_path, output_path):
    # Load data
    df = pd.read_csv(input_path, sep=";")

    # Remove duplicate records
    df = df.drop_duplicates()

    # Standardize column names
    df.columns = (
        df.columns
        .str.lower()
        .str.strip()
        .str.replace(" ", "_")
    )

    # Convert categorical values
    categorical_columns = [
        "job",
        "marital",
        "education",
        "default",
        "housing",
        "loan",
        "contact",
        "month",
        "poutcome",
        "y"
    ]

    for col in categorical_columns:
        df[col] = df[col].astype("category")

    # Save cleaned dataset
    df.to_csv(output_path, index=False)

    print("Cleaning completed.")
    print(f"Rows: {len(df)}")
    print(f"Columns: {len(df.columns)}")


if __name__ == "__main__":
    clean_bank_data(
        "data/raw/bank-full.csv",
        "data/processed/bank_clean.csv"
    )
