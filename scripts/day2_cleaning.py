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
