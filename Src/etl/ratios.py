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
def calculate_cagr(start, end, years):
    if years <= 0:
        return None

    # Normal Case
    if start > 0 and end > 0:
        return ((end / start) ** (1 / years) - 1) * 100

    # Edge Cases
    if start > 0 and end < 0:
        return None      # DECLINE_TO_LOSS

    if start < 0 and end > 0:
        return None      # TURNAROUND

    if start < 0 and end < 0:
        return None      # BOTH_NEGATIVE

    if start == 0:
        return None      # ZERO_BASE

    return None
print("CAGR Engine loaded successfully!")
def free_cash_flow(operating_activity, investing_activity):
    """Calculate Free Cash Flow."""
    return operating_activity + investing_activity


def cfo_quality_score(cfo, pat):
    """Calculate CFO Quality Score."""
    if pat == 0:
        return None
    return cfo / pat


def capex_intensity(investing_activity, sales):
    """Calculate CapEx Intensity."""
    if sales == 0:
        return None
    return abs(investing_activity) / sales * 100


def fcf_conversion_rate(fcf, operating_profit):
    """Calculate FCF Conversion Rate."""
    if operating_profit == 0:
        return None
    return (fcf / operating_profit) * 100


print("Cash Flow KPI module loaded successfully!")
def composite_quality_score(roe, cfo_quality, fcf_conversion):
    """Calculate Composite Quality Score."""
    values = [roe, cfo_quality, fcf_conversion]

    valid = [v for v in values if v is not None]

    if len(valid) == 0:
        return None

    return sum(valid) / len(valid)
print("Composite Quality Score module loaded successfully!")
def financial_health_score(
    roe,
    roce,
    roa,
    debt_to_equity,
    interest_coverage,
):
    """
    Calculate Financial Health Score.
    """

    scores = []

    if roe is not None:
        scores.append(roe)

    if roce is not None:
        scores.append(roce)

    if roa is not None:
        scores.append(roa)

    if debt_to_equity is not None:
        scores.append(max(0, 100 - debt_to_equity * 20))

    if interest_coverage is not None:
        scores.append(min(interest_coverage * 10, 100))

    if len(scores) == 0:
        return None

    return sum(scores) / len(scores)


print("Financial Health Score module loaded successfully!")
def valuation_score(pe, pb, roe):
    """
    Calculate Valuation Score.
    Lower PE/PB and higher ROE get better score.
    """

    scores = []

    if pe is not None and pe > 0:
        scores.append(max(0, 100 - pe))

    if pb is not None and pb > 0:
        scores.append(max(0, 100 - (pb * 10)))

    if roe is not None:
        scores.append(min(roe, 100))

    if len(scores) == 0:
        return None

    return sum(scores) / len(scores)


print("Valuation Score module loaded successfully!")
def investment_score(quality_score, health_score, valuation_score):
    """
    Calculate Overall Investment Score.
    """

    values = [quality_score, health_score, valuation_score]
    valid = [v for v in values if v is not None]

    if len(valid) == 0:
        return None

    return sum(valid) / len(valid)


print("Investment Score module loaded successfully!")
def rating_from_score(score):
    """
    Convert investment score into a rating.
    """

    if score is None:
        return "N/A"
    elif score >= 80:
        return "Strong Buy"
    elif score >= 60:
        return "Buy"
    elif score >= 40:
        return "Hold"
    elif score >= 20:
        return "Sell"
    else:
        return "Strong Sell"


print("Investment Rating module loaded successfully!")
def recommendation(score):
    """Return investment recommendation."""

    if score is None:
        return "No Data"

    if score >= 80:
        return "Strong Buy"
    elif score >= 60:
        return "Buy"
    elif score >= 40:
        return "Hold"
    elif score >= 20:
        return "Sell"
    else:
        return "Strong Sell"


print("Recommendation module loaded successfully!")




