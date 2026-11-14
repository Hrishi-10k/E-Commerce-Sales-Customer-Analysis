from pathlib import Path

# Project root is the parent folder of src/
ROOT_DIR = Path(__file__).resolve().parents[1]
RAW_FILE = ROOT_DIR / "data" / "raw" / "ecommerce_raw.csv"
CLEAN_FILE = ROOT_DIR / "data" / "processed" / "ecommerce_cleaned.csv"
GRAPH_DIR = ROOT_DIR / "outputs" / "graphs"
REPORT_DIR = ROOT_DIR / "outputs" / "reports"
INSIGHTS_FILE = ROOT_DIR / "outputs" / "analysis" / "business_insights.txt"
PDF_FILE = REPORT_DIR / "ecommerce_eda_report.pdf"
# Standard names used by the remaining modules
REQUIRED_COLUMNS = [
    "order_id",
    "order_date",
    "customer_id",
    "customer_name",
    "product",
    "category",
    "region",
    "sales",
    "quantity",
    "discount",
    "profit",
    "payment_method",
    "order_status",
]
# Input aliases: common source headers -> standard column names
COLUMN_ALIASES = {
    "order id": "order_id",
    "order_id": "order_id",
    "orderid": "order_id",
    "order date": "order_date",
    "order_date": "order_date",
    "date": "order_date",
    "customer id": "customer_id",
    "customer_id": "customer_id",
    "customer name": "customer_name",
    "customer_name": "customer_name",
    "product": "product",
    "product name": "product",
    "category": "category",
    "region": "region",
    "sales": "sales",
    "revenue": "sales",
    "amount": "sales",
    "quantity": "quantity",
    "qty": "quantity",
    "discount": "discount",
    "profit": "profit",
    "payment method": "payment_method",
    "payment_method": "payment_method",
    "order status": "order_status",
    "status": "order_status",
}
