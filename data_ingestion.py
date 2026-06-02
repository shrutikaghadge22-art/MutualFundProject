import pandas as pd

print("Data Ingestion Started")

sample_data = {
    "Scheme_Code": [125497, 119551, 120503],
    "Fund_Name": ["HDFC Top 100", "SBI Bluechip", "ICICI Bluechip"]
}

df = pd.DataFrame(sample_data)

print(df)
print(df.shape)
print(df.dtypes)

print("Data Ingestion Completed")