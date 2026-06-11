"""
Data Ingestion Script

This script loads cleaned mutual fund data
into the SQLite database.
"""
import pandas as pd
from sqlalchemy import create_engine

# Create SQLite database
engine = create_engine("sqlite:///data/db/bluestock_mf.db")

# Read cleaned CSV file
df = pd.read_csv("data/processed/nav_history_cleaned.csv")

# Load data into SQLite table
df.to_sql(
    "fact_nav",
    con=engine,
    if_exists="replace",
    index=False
)

print("Data loaded successfully into SQLite database")
