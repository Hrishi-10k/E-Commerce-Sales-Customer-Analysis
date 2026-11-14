from src.data_loader import load_data
from src.data_cleaning import clean_data
from src.data_transformation import transform_data
from src.analysis import analyze_data
from src.visualization import create_visualizations
from src.report import generate_pdf_report
from src.config import CLEAN_FILE


def main():
    print("1/6 Loading raw data...")
    df = load_data()
    print("\n2/6 Cleaning data...")
    clean_df = clean_data(df)
    print("\n3/6 Transforming data...")
    transformed_df = transform_data(clean_df)
    print("\n4/6 Running analysis...")
    summaries = analyze_data(transformed_df)
    print("\n5/6 Creating charts...")
    create_visualizations(transformed_df, summaries)
    print("\n6/6 Saving clean data and PDF report...")
    CLEAN_FILE.parent.mkdir(parents=True, exist_ok=True)
    transformed_df.to_csv(CLEAN_FILE, index=False)
    generate_pdf_report(transformed_df, summaries)
    print("\nPROJECT COMPLETED!")
    print("Clean CSV:", CLEAN_FILE)


if __name__ == "__main__":
    main()
