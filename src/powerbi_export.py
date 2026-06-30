"""
Enterprise Banking Analytics Platform
Power BI Export Preparation
"""

import pandas as pd


def prepare_powerbi_dataset(input_path: str, output_path: str) -> None:
    df = pd.read_csv(input_path, sep=";")

    df["subscribed"] = df["y"].map({"yes": 1, "no": 0})
    df["has_housing_loan"] = df["housing"].map({"yes": 1, "no": 0})
    df["has_personal_loan"] = df["loan"].map({"yes": 1, "no": 0})
    df["has_credit_default"] = df["default"].map({"yes": 1, "no": 0})

    df.to_csv(output_path, index=False)

    print("Power BI dataset prepared successfully.")
    print(f"Output file: {output_path}")


if __name__ == "__main__":
    prepare_powerbi_dataset(
        "data/raw/bank-full.csv",
        "data/processed/powerbi_bank_dataset.csv"
    )
