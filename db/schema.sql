PRAGMA foreign_keys = ON;

CREATE TABLE companies (
    company_id INTEGER PRIMARY KEY,
    company_name TEXT NOT NULL
);

CREATE TABLE sectors (
    sector_id INTEGER PRIMARY KEY,
    sector_name TEXT NOT NULL
);

CREATE TABLE financial_ratios (
    ratio_id INTEGER PRIMARY KEY,
    company_id INTEGER,
    FOREIGN KEY (company_id) REFERENCES companies(company_id)
);

CREATE TABLE profitandloss (
    pnl_id INTEGER PRIMARY KEY,
    company_id INTEGER,
    FOREIGN KEY (company_id) REFERENCES companies(company_id)
);

CREATE TABLE balancesheet (
    bs_id INTEGER PRIMARY KEY,
    company_id INTEGER,
    FOREIGN KEY (company_id) REFERENCES companies(company_id)
);

CREATE TABLE cashflow (
    cf_id INTEGER PRIMARY KEY,
    company_id INTEGER,
    FOREIGN KEY (company_id) REFERENCES companies(company_id)
);

CREATE TABLE stock_prices (
    price_id INTEGER PRIMARY KEY,
    company_id INTEGER,
    FOREIGN KEY (company_id) REFERENCES companies(company_id)
);

CREATE TABLE peer_groups (
    peer_id INTEGER PRIMARY KEY,
    company_id INTEGER,
    FOREIGN KEY (company_id) REFERENCES companies(company_id)
);

CREATE TABLE market_cap (
    market_id INTEGER PRIMARY KEY,
    company_id INTEGER,
    FOREIGN KEY (company_id) REFERENCES companies(company_id)
);

CREATE TABLE documents (
    doc_id INTEGER PRIMARY KEY,
    company_id INTEGER,
    FOREIGN KEY (company_id) REFERENCES companies(company_id)
);