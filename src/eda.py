"""
Enterprise Banking Analytics Platform
Exploratory Data Analysis
"""

import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("data/raw/bank-full.csv", sep=";")

print("=" * 60)
print("DATASET OVERVIEW")
print("=" * 60)

print(f"Rows: {df.shape[0]}")
print(f"Columns: {df.shape[1]}")

print("\nColumns:")
print(df.columns.tolist())

print("\nMissing Values:")
print(df.isnull().sum())

print("\nData Types:")
print(df.dtypes)

print("\nSummary Statistics:")
print(df.describe())

print("\nTarget Distribution:")
print(df["y"].value_counts())

# ----------------------------
# Age Distribution
# ----------------------------

plt.figure(figsize=(10,5))
plt.hist(df["age"], bins=30)
plt.title("Customer Age Distribution")
plt.xlabel("Age")
plt.ylabel("Number of Customers")
plt.grid(True)
plt.show()

# ----------------------------
# Account Balance
# ----------------------------

plt.figure(figsize=(10,5))
plt.hist(df["balance"], bins=50)
plt.title("Account Balance Distribution")
plt.xlabel("Balance")
plt.ylabel("Customers")
plt.grid(True)
plt.show()

# ----------------------------
# Job Distribution
# ----------------------------

plt.figure(figsize=(12,6))
df["job"].value_counts().plot(kind="bar")
plt.title("Customers by Job")
plt.ylabel("Count")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# ----------------------------
# Subscription Distribution
# ----------------------------

plt.figure(figsize=(6,6))
df["y"].value_counts().plot(kind="pie", autopct="%1.1f%%")
plt.ylabel("")
plt.title("Deposit Subscription")
plt.show()
