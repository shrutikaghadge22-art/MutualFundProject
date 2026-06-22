import pandas as pd

files = [
    "companies.xlsx",
    "profitandloss.xlsx",
    "balancesheet.xlsx",
    "cashflow (1).xlsx",
    "stock_prices (1).xlsx",
    "financial_ratios.xlsx",
    "sectors.xlsx",
    "Copy of documents.xlsx",
    "Copy of market_cap.xlsx",
    "Copy of peer_groups.xlsx"
]

for file in files:
    try:
        df = pd.read_excel(f"Data/{file}")
        print(file, "->", len(df), "rows")
    except Exception as e:
        print(file, "-> ERROR:", e)

print("Data load completed!")