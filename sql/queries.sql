-- Query 1
SELECT * FROM fact_nav LIMIT 5;

-- Query 2
SELECT AVG(nav) AS average_nav
FROM fact_nav;

-- Query 3
SELECT MAX(nav) AS highest_nav
FROM fact_nav;

-- Query 4
SELECT MIN(nav) AS lowest_nav
FROM fact_nav;

-- Query 5
SELECT COUNT(*) AS total_transactions
FROM fact_transactions;

-- Query 6
SELECT SUM(amount_inr) AS total_amount
FROM fact_transactions;

-- Query 7
SELECT AVG(return_1yr_pct) AS avg_return_1yr
FROM fact_performance;

-- Query 8
SELECT AVG(return_3yr_pct) AS avg_return_3yr
FROM fact_performance;

-- Query 9
SELECT AVG(return_5yr_pct) AS avg_return_5yr
FROM fact_performance;

-- Query 10
SELECT amfi_code, return_1yr_pct
FROM fact_performance
ORDER BY return_1yr_pct DESC
LIMIT 5;