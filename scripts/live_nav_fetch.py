import requests
import pandas as pd

print("Fetching Live NAV Data...")

url = "https://api.mfapi.in/mf/125497"

response = requests.get(url)

data = response.json()

nav_data = {
    "Scheme_Name": [data["meta"]["scheme_name"]],
    "NAV": [data["data"][0]["nav"]],
    "Date": [data["data"][0]["date"]]
}

df = pd.DataFrame(nav_data)

print(df)

df.to_csv("live_nav.csv", index=False)

print("Live NAV Data Saved Successfully")