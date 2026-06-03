CREATE TABLE dim_fund (
    amfi_code TEXT PRIMARY KEY,
    fund_house TEXT,
    scheme_name TEXT,
    category TEXT
);

CREATE TABLE fact_nav (
    amfi_code TEXT,
    nav_date DATE,
    nav REAL,
    daily_return REAL,
    FOREIGN KEY (amfi_code) REFERENCES dim_fund(amfi_code)
);

CREATE TABLE fact_transactions (
    transaction_id INTEGER PRIMARY KEY,
    amfi_code TEXT,
    transaction_date DATE,
    amount REAL
);

CREATE TABLE fact_performance (
    amfi_code TEXT,
    returns_1y REAL,
    returns_3y REAL,
    sharpe_ratio REAL
);