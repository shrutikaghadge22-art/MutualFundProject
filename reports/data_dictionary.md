# Data Dictionary

## dim_fund

| Column | Description |
|----------|-------------|
| amfi_code | Unique fund identifier |
| fund_house | Fund house name |
| scheme_name | Scheme name |
| category | Fund category |

## fact_nav

| Column | Description |
|----------|-------------|
| amfi_code | Fund identifier |
| nav_date | NAV date |
| nav | Net Asset Value |
| daily_return | Daily return |

## fact_transactions

| Column | Description |
|----------|-------------|
| transaction_id | Transaction ID |
| amfi_code | Fund identifier |
| transaction_date | Transaction date |
| amount_inr | Transaction amount |

## fact_performance

| Column | Description |
|----------|-------------|
| amfi_code | Fund identifier |
| return_1yr_pct | 1 year return |
| return_3yr_pct | 3 year return |
| return_5yr_pct | 5 year return |