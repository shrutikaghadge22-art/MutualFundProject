import pandas as pd

df = pd.read_excel("Data/analysis.xlsx")

failures = []

# DQ-01: Null values
for col in df.columns:
    if df[col].isnull().sum() > 0:
        failures.append([col, "NULL VALUES"])

# DQ-02: Duplicate rows
if df.duplicated().sum() > 0:
    failures.append(["ALL", "DUPLICATE ROWS"])

# DQ-03: Empty dataframe
if len(df) == 0:
    failures.append(["ALL", "EMPTY FILE"])

# Save failures
failure_df = pd.DataFrame(
    failures,
    columns=["Column", "Issue"]
)

failure_df.to_csv(
    "output/validation_failures.csv",
    index=False
)

print("Validation completed")
print("Failures:", len(failures))