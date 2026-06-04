import pandas as pd

# Load NAV History
df = pd.read_csv("data/raw/02_nav_history.csv")

# Convert date column
df["date"] = pd.to_datetime(df["date"])

# Sort values
df = df.sort_values(["amfi_code", "date"])

# Remove duplicates
df = df.drop_duplicates()

# Keep valid NAV values
df = df[df["nav"] > 0]

# Save cleaned file
df.to_csv("data/processed/nav_history_cleaned.csv", index=False)

print("NAV History cleaned successfully!")
import pandas as pd

print("Task 2 Started...")

# Read investor transactions file
transactions = pd.read_csv(
    "data/raw/08_investor_transactions.csv"
)

# Remove duplicates
transactions = transactions.drop_duplicates()

# Convert amount_inr to numeric
transactions["amount_inr"] = pd.to_numeric(
    transactions["amount_inr"],
    errors="coerce"
)

# Keep only valid amounts
transactions = transactions[
    transactions["amount_inr"] > 0
]

# Standardize transaction type
transactions["transaction_type"] = (
    transactions["transaction_type"]
    .astype(str)
    .str.strip()
    .str.title()
)

# Fix date format
transactions["transaction_date"] = pd.to_datetime(
    transactions["transaction_date"],
    errors="coerce"
)

# Remove invalid dates
transactions = transactions.dropna(
    subset=["transaction_date"]
)

# Save cleaned file
transactions.to_csv(
    "data/processed/clean_transactions.csv",
    index=False
)

print("Investor Transactions cleaned successfully!")
# -----------------------------
# TASK 3 - Clean Scheme Performance
# -----------------------------

performance = pd.read_csv(
    "data/raw/07_scheme_performance.csv"
)

performance = performance.drop_duplicates()

performance["return_1yr_pct"] = pd.to_numeric(
    performance["return_1yr_pct"],
    errors="coerce"
)

performance["return_3yr_pct"] = pd.to_numeric(
    performance["return_3yr_pct"],
    errors="coerce"
)

performance["return_5yr_pct"] = pd.to_numeric(
    performance["return_5yr_pct"],
    errors="coerce"
)

performance.to_csv(
    "data/processed/clean_performance.csv",
    index=False
)

print("Scheme Performance cleaned successfully!")