import pandas as pd
from src.config import RAW_FILE, COLUMN_ALIASES
def load_data():
    if not RAW_FILE.exists():
        raise FileNotFoundError(
            f"Raw CSV not found: {RAW_FILE}. Add ecommerce_raw.csv to data/raw."
        )
    df = pd.read_csv(RAW_FILE, encoding="utf-8-sig")
    # Normalize header names: trim, lowercase, replace underscores for matching
    normalized = {}
    for col in df.columns:
        key = str(col).strip().lower().replace("_", " ")
        normalized[col] = COLUMN_ALIASES.get(key, key.replace(" ", "_"))
    df = df.rename(columns=normalized)
    print("\n--- DATA OVERVIEW ---")
    print("Shape:", df.shape)
    print("\nColumns:", df.columns.tolist())
    print("\nData types:\n", df.dtypes)
    print("\nFirst 5 rows:\n", df.head())
    print("\nMissing values:\n", df.isnull().sum())
    print("\nDuplicate rows:", df.duplicated().sum())
    return df