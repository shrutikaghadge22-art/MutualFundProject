def normalize_year(year):
    year = str(year).strip()
    return year.upper()

def normalize_ticker(ticker):
    ticker = str(ticker).strip()
    return ticker.upper()

assert normalize_year("Mar 2021") == "MAR 2021"
assert normalize_ticker("tcs") == "TCS"

print("All tests passed!")