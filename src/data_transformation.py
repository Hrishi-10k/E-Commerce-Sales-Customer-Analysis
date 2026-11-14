import numpy as np


def transform_data(df):
    df = df.copy()
    df["year"] = df["order_date"].dt.year
    df["month"] = df["order_date"].dt.month
    df["month_name"] = df["order_date"].dt.strftime("%b")
    df["year_month"] = df["order_date"].dt.to_period("M").astype(str)
    # Business metrics
    df["revenue"] = df["sales"]
    df["profit_margin_pct"] = np.where(
        df["revenue"] != 0, (df["profit"] / df["revenue"]) * 100, 0
    )
    # Helpful discount grouping
    df["discount_category"] = pd_cut_discount(df["discount"])
    return df


def pd_cut_discount(discount):
    # Import locally to keep the function easy to read for learners
    import pandas as pd

    return pd.cut(
        discount,
        bins=[-0.001, 0, 0.10, 0.20, 1.001],
        labels=["No Discount", "Low (0-10%)", "Medium (10-20%)", "High (>20%)"],
        include_lowest=True,
    ).astype("string")
