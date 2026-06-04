import pandas as pd
from sqlalchemy import create_engine

print("Data Ingestion Started")

# SQLite database connection
engine = create_engine("sqlite:///data/db/bluestock_mf.db")

# Load cleaned files
nav_df = pd.read_csv("data/processed/nav_history_cleaned.csv")
trans_df = pd.read_csv("data/processed/clean_transactions.csv")
perf_df = pd.read_csv("data/processed/clean_performance.csv")

# Load into SQLite
nav_df.to_sql(
    "fact_nav",
    con=engine,
    if_exists="replace",
    index=False
)

trans_df.to_sql(
    "fact_transactions",
    con=engine,
    if_exists="replace",
    index=False
)

perf_df.to_sql(
    "fact_performance",
    con=engine,
    if_exists="replace",
    index=False
)

print("Data loaded successfully into SQLite database")