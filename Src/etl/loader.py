import pandas as pd

def normalize_year(year):
    year = str(year).strip()
    return year.upper()

def normalize_ticker(ticker):
    ticker = str(ticker).strip()
    return ticker.upper()

print("Pandas version:", pd.__version__)
print("Excel Loader Ready")

print(normalize_year("Mar 2021"))
print(normalize_ticker("tcs"))

df = pd.read_excel("Data/analysis.xlsx")
print(df.head())