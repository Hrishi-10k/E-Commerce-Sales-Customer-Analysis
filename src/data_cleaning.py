import pandas as pd
import numpy as np
from src.config import REQUIRED_COLUMNS


def clean_data(df):
    df = df.copy()
    # Remove exact duplicate records
    df = df.drop_duplicates()
    # Ensure all expected columns exist before cleaning
    missing_columns = [c for c in REQUIRED_COLUMNS if c not in df.columns]
    if missing_columns:
        raise ValueError(
            "Required columns missing: "
            + ", ".join(missing_columns)
            + ". Check your CSV headers or update COLUMN_ALIASES in config.py."
        )
    # Standardize text fields
    text_cols = [
        "order_id",
        "customer_id",
        "customer_name",
        "product",
        "category",
        "region",
        "payment_method",
        "order_status",
    ]
    for col in text_cols:
        df[col] = df[col].astype("string").str.strip()
        df[col] = df[col].replace({"": pd.NA, "nan": pd.NA, "None": pd.NA})
    
    # Parse order date and numeric values
    df["order_date"] = pd.to_datetime(
    df["order_date"],
    format="%d-%m-%Y",
    errors="coerce"
    )
    
    for col in ["sales", "quantity", "discount", "profit"]:
        df[col] = pd.to_numeric(df[col], errors="coerce")
    # Remove rows missing essential identifiers or invalid transaction values
    df = df.dropna(subset=["order_id", "order_date", "product", "sales", "quantity"])
    df = df[(df["sales"] >= 0) & (df["quantity"] > 0)]
    # Categorical missing values
    for col in [
        "customer_id",
        "customer_name",
        "category",
        "region",
        "payment_method",
        "order_status",
    ]:
        df[col] = df[col].fillna("Unknown")
    # Missing discount/profit assumptions (state these in the report)
    df["discount"] = df["discount"].fillna(0)
    df["profit"] = df["profit"].fillna(0)
    
    # Convert discount to float
    df["discount"] = df["discount"].astype(float)
    
    # Standardize discount: 10 means 10%, 0.10 means 10%
    df.loc[df["discount"] > 1, "discount"] = df.loc[df["discount"] > 1, "discount"] / 100
    df["discount"] = df["discount"].clip(lower=0, upper=1)
    
    # Normalize category/status labels
    for col in ["category", "region", "payment_method", "order_status"]:
        df[col] = df[col].str.title()

    # Remove any duplicates created by normalized rows
    df = df.drop_duplicates()

    print("\n--- CLEANING SUMMARY ---")
    print("Rows after cleaning:", len(df))
    print("Missing values after cleaning:\n", df.isnull().sum())
    return df
