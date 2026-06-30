import pandas as pd

# Load dataset
df = pd.read_csv("data/raw/bank-full.csv", sep=";")

print("=" * 50)
print("Dataset Shape")
print("=" * 50)
print(df.shape)

print("\nColumns:")
print(df.columns.tolist())

print("\nFirst 5 rows:")
print(df.head())

print("\nMissing values:")
print(df.isnull().sum())

print("\nData types:")
print(df.dtypes)

print("\nTarget distribution:")
print(df["y"].value_counts())
