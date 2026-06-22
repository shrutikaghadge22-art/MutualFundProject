import pandas as pd
import random

df = pd.read_excel("Data/companies.xlsx")

sample = df.sample(min(5, len(df)))

print("Random Companies:")
print(sample)

print("\nTotal Companies:", len(df))
print("Sprint Review Completed")