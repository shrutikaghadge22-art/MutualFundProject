def net_profit_margin(net_profit, sales):
    if sales == 0:
        return None
    return (net_profit / sales) * 100


def operating_profit_margin(operating_profit, sales):
    if sales == 0:
        return None
    return (operating_profit / sales) * 100


def return_on_equity(net_profit, equity, reserves):
    capital = equity + reserves
    if capital <= 0:
        return None
    return (net_profit / capital) * 100


def return_on_capital_employed(ebit, equity, reserves, borrowings):
    capital = equity + reserves + borrowings
    if capital <= 0:
        return None
    return (ebit / capital) * 100


def return_on_assets(net_profit, total_assets):
    if total_assets == 0:
        return None
    return (net_profit / total_assets) * 100


print("Profitability ratios module loaded successfully!")
# -----------------------------
# Day 9 - Leverage & Efficiency Ratios
# -----------------------------

def debt_to_equity(borrowings, equity, reserves):
    capital = equity + reserves
    if borrowings == 0:
        return 0
    if capital <= 0:
        return None
    return borrowings / capital


def interest_coverage(operating_profit, other_income, interest):
    if interest == 0:
        return None
    return (operating_profit + other_income) / interest


def net_debt(borrowings, investments):
    return borrowings - investments


def asset_turnover(sales, total_assets):
    if total_assets == 0:
        return None
    return sales / total_assets


print("Leverage & Efficiency ratios loaded successfully!")