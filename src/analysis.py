import pandas as pd
from src.config import INSIGHTS_FILE


def analyze_data(df):
    summaries = {}
    summaries["region_revenue"] = (
        df.groupby("region", dropna=False)["revenue"]
        .sum()
        .sort_values(ascending=False)
        .reset_index()
    )
    summaries["category_revenue"] = (
        df.groupby("category")["revenue"]
        .sum()
        .sort_values(ascending=False)
        .reset_index()
    )
    summaries["category_profit"] = (
        df.groupby("category")["profit"]
        .sum()
        .sort_values(ascending=False)
        .reset_index()
    )
    summaries["product_sales"] = (
        df.groupby("product")["revenue"]
        .sum()
        .sort_values(ascending=False)
        .reset_index()
    )
    summaries["top_customers"] = (
        df.groupby(["customer_id", "customer_name"])["revenue"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
        .reset_index()
    )
    summaries["monthly_revenue"] = (
        df.groupby("year_month")["revenue"].sum().sort_index().reset_index()
    )
    summaries["payment_method"] = (
        df["payment_method"]
        .value_counts()
        .rename_axis("payment_method")
        .reset_index(name="order_rows")
    )
    summaries["discount_profit"] = (
        df.groupby("discount_category", observed=False)["profit"]
        .mean()
        .reset_index(name="average_profit")
    )
    summaries["weak_products"] = (
        df.groupby("product")
        .agg(revenue=("revenue", "sum"), profit=("profit", "sum"))
        .sort_values("profit")
        .head(10)
        .reset_index()
    )
    summaries["status_counts"] = (
        df["order_status"]
        .value_counts()
        .rename_axis("order_status")
        .reset_index(name="count")
    )
    # AOV = total revenue / distinct orders (not transaction rows)
    total_revenue = df["revenue"].sum()
    order_count = df["order_id"].nunique()
    aov = total_revenue / order_count if order_count else 0
    cancelled = df["order_status"].str.contains("cancel", case=False, na=False).sum()
    returned = df["order_status"].str.contains("return", case=False, na=False).sum()
    INSIGHTS_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(INSIGHTS_FILE, "w", encoding="utf-8") as f:
        f.write("E-COMMERCE BUSINESS INSIGHTS\n")
        f.write("=" * 32 + "\n")
        f.write(f"Total revenue: {total_revenue:,.2f}\n")
        f.write(f"Unique orders: {order_count:,}\n")
        f.write(f"Average order value (AOV): {aov:,.2f}\n")
        f.write(f"Cancelled order rows: {cancelled:,}\n")
        f.write(f"Returned order rows: {returned:,}\n\n")
        if not summaries["region_revenue"].empty:
            row = summaries["region_revenue"].iloc[0]
            f.write(f"Top revenue region: {row['region']} ({row['revenue']:,.2f})\n")
        if not summaries["category_revenue"].empty:
            row = summaries["category_revenue"].iloc[0]
            f.write(
                f"Top revenue category: {row['category']} ({row['revenue']:,.2f})\n"
            )
        if not summaries["category_profit"].empty:
            row = summaries["category_profit"].iloc[0]
            f.write(f"Top profit category: {row['category']} ({row['profit']:,.2f})\n")
        if not summaries["product_sales"].empty:
            row = summaries["product_sales"].iloc[0]
            f.write(f"Top sales product: {row['product']} ({row['revenue']:,.2f})\n")
        if not summaries["payment_method"].empty:
            row = summaries["payment_method"].iloc[0]
            f.write(f"Most used payment method: {row['payment_method']}\n")
        f.write("\nLowest-profit products (review these):\n")
        f.write(summaries["weak_products"].to_string(index=False))
        f.write("\n\nMonthly revenue:\n")
        f.write(summaries["monthly_revenue"].to_string(index=False))
    summaries["kpis"] = {
        "total_revenue": total_revenue,
        "unique_orders": order_count,
        "aov": aov,
        "cancelled": int(cancelled),
        "returned": int(returned),
    }
    return summaries
