import pandas as pd

performance = pd.read_csv("../processed/clean_performance.csv")

performance["risk_grade"] = performance["category"].apply(
    lambda x: "Low" if "Large Cap" in str(x)
    else ("Moderate" if "Mid Cap" in str(x)
    else "High")
)

performance["score"] = (
    performance["return_1yr_pct"] +
    performance["return_3yr_pct"] +
    performance["return_5yr_pct"]
) / 3

risk_appetite = "Moderate"

recommended = performance[
    performance["risk_grade"] == risk_appetite
].sort_values(
    by="score",
    ascending=False
).head(3)

print(recommended[
    ["scheme_name", "category", "risk_grade", "score"]
])