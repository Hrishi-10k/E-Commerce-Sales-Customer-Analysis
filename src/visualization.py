import matplotlib

matplotlib.use("Agg")  # Works without opening a GUI
import matplotlib.pyplot as plt
import seaborn as sns
from src.config import GRAPH_DIR

sns.set_theme(style="whitegrid")


def create_visualizations(df, summaries):
    GRAPH_DIR.mkdir(parents=True, exist_ok=True)
    # 1. Revenue by region
    plt.figure(figsize=(9, 5))
    sns.barplot(data=summaries["region_revenue"], x="region", y="revenue")
    plt.title("Revenue by Region")
    plt.xlabel("Region")
    plt.ylabel("Revenue")
    plt.tight_layout()
    plt.savefig(GRAPH_DIR / "revenue_by_region.png", dpi=150)
    plt.close()
    # 2. Revenue by category
    plt.figure(figsize=(9, 5))
    sns.barplot(data=summaries["category_revenue"], x="category", y="revenue")
    plt.title("Revenue by Category")
    plt.xticks(rotation=25, ha="right")
    plt.tight_layout()
    plt.savefig(GRAPH_DIR / "revenue_by_category.png", dpi=150)
    plt.close()
    # 3. Profit by category
    plt.figure(figsize=(9, 5))
    sns.barplot(data=summaries["category_profit"], x="category", y="profit")
    plt.title("Profit by Category")
    plt.xticks(rotation=25, ha="right")
    plt.tight_layout()
    plt.savefig(GRAPH_DIR / "profit_by_category.png", dpi=150)
    plt.close()
    # 4. Monthly revenue trend
    monthly = summaries["monthly_revenue"]
    plt.figure(figsize=(10, 5))
    sns.lineplot(data=monthly, x="year_month", y="revenue", marker="o")
    plt.title("Monthly Revenue Trend")
    plt.xlabel("Year-Month")
    plt.ylabel("Revenue")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.savefig(GRAPH_DIR / "monthly_revenue_trend.png", dpi=150)
    plt.close()
    # 5. Top 10 customers
    customers = summaries["top_customers"].copy()
    customers["customer_label"] = customers["customer_name"].astype(str)
    plt.figure(figsize=(10, 5))
    sns.barplot(data=customers, x="revenue", y="customer_label")
    plt.title("Top 10 Customers by Revenue")
    plt.tight_layout()
    plt.savefig(GRAPH_DIR / "top_customers.png", dpi=150)
    plt.close()
    # 6. Discount vs profit scatter
    plt.figure(figsize=(9, 5))
    sns.scatterplot(data=df, x="discount", y="profit", hue="category", alpha=0.7)
    plt.title("Discount vs Profit")
    plt.tight_layout()
    plt.savefig(GRAPH_DIR / "discount_vs_profit.png", dpi=150)
    plt.close()
    # 7. Sales distribution histogram
    plt.figure(figsize=(9, 5))
    sns.histplot(data=df, x="revenue", bins=30, kde=True)
    plt.title("Revenue Distribution")
    plt.tight_layout()
    plt.savefig(GRAPH_DIR / "revenue_distribution.png", dpi=150)
    plt.close()
    # 8. Profit margin by category boxplot
    plt.figure(figsize=(10, 5))
    sns.boxplot(data=df, x="category", y="profit_margin_pct")
    plt.title("Profit Margin Distribution by Category")
    plt.xticks(rotation=25, ha="right")
    plt.tight_layout()
    plt.savefig(GRAPH_DIR / "profit_margin_boxplot.png", dpi=150)
    plt.close()
    # 9. Correlation heatmap for numeric columns
    numeric = df[
        ["sales", "quantity", "discount", "profit", "revenue", "profit_margin_pct"]
    ].corr()
    plt.figure(figsize=(8, 6))
    sns.heatmap(numeric, annot=True, cmap="coolwarm", fmt=".2f")
    plt.title("Numeric Feature Correlation Heatmap")
    plt.tight_layout()
    plt.savefig(GRAPH_DIR / "correlation_heatmap.png", dpi=150)
    plt.close()
    # 10. Payment method usage
    plt.figure(figsize=(8, 5))
    sns.barplot(data=summaries["payment_method"], x="payment_method", y="order_rows")
    plt.title("Payment Method Usage")
    plt.xticks(rotation=25, ha="right")
    plt.tight_layout()
    plt.savefig(GRAPH_DIR / "payment_method_usage.png", dpi=150)
    plt.close()
    print(f"Graphs saved to: {GRAPH_DIR}")
