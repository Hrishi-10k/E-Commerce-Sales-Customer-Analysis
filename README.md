# E-Commerce Sales Data Analysis

## 📌 Project Overview

This project focuses on analyzing historical e-commerce sales data using Python to uncover meaningful business insights and trends. It involves data loading, cleaning, transformation, Exploratory Data Analysis (EDA), and visualization to understand sales performance, profitability, and customer behavior.

## 🎯 Project Objectives

- Load and inspect raw e-commerce CSV data.
- Handle missing values, duplicates, and invalid records.
- Clean and transform data for analysis.
- Perform Exploratory Data Analysis (EDA).
- Analyze sales, profit, discounts, and customer behavior.
- Identify top-performing products, categories, and regions.
- Generate meaningful visualizations and business insights.
- Export cleaned datasets, graphs, and PDF reports.

## 🛠️ Technologies Used

- **Python** – Core programming language
- **Pandas** – Data manipulation and analysis
- **NumPy** – Numerical computations
- **Matplotlib** – Data visualization
- **Seaborn** – Statistical visualization
- **Jupyter Notebook** – Data exploration and analysis

## 📁 Project Structure

```text
E-Commerce-Sales-Analysis/
│
├── data/
│   ├── raw/                 # Original dataset
│   └── processed/           # Cleaned and transformed dataset
│
├── notebooks/               # Jupyter notebooks for EDA
│
├── src/
│   ├── __init__.py
│   ├── config.py             # Project configurations
│   ├── data_loader.py       # Load raw datasets
│   ├── data_cleaning.py     # Handle missing and invalid data
│   ├── data_transformation.py # Data preprocessing
│   ├── analysis.py          # Exploratory data analysis
│   ├── visualization.py     # Generate graphs and charts
│   └── report.py            # Generate PDF reports
│
├── outputs/
│   ├── graphs/              # Generated visualizations
│   ├── reports/             # PDF analysis reports
│   └── analysis/            # Analysis results and insights
│
├── main.py                  # Main execution file
├── requirements.txt         # Project dependencies
└── README.md                # Project documentation
```

## ⚙️ Installation & Setup

**1. Clone the repository**

```bash
git clone https://github.com/Hrishi-10k/E-Commerce-Sales-Customer-Analysis.git
cd E-Commerce-Sales-Analysis
```

**2. Create a virtual environment**

```bash
python -m venv venv
```

**3. Activate the virtual environment**

Windows:

```bash
venv\Scripts\activate
```

**4. Install dependencies**

```bash
pip install -r requirements.txt
```

**5. Add the dataset**

Place the original CSV dataset inside:

```text
data/raw/
```

**6. Run the project**

```bash
python main.py
```

## 📊 Expected Analysis

The project aims to explore:

- Overall sales and profit performance.
- Monthly and yearly sales trends.
- Category-wise and product-wise performance.
- Region-wise sales and profitability.
- Customer purchasing behavior.
- Impact of discounts on profitability.
- Payment method distribution.
- Order status analysis.

## 📈 Project Outputs

All generated files will be organized inside the `outputs/` directory:

- **Graphs:** Sales trends, profit comparisons, category analysis, and more.
- **Analysis:** Key findings and business insights.
- **Reports:** Comprehensive PDF report containing analysis and visualizations.

## 💡 Expected Outcome

Transform raw e-commerce data into meaningful business insights through Python-based data analysis and visualization, helping businesses understand performance, identify opportunities, and make data-driven decisions.

## 👨‍💻 Author

**Hrishi Dahake**

GitHub: [Hrishi-10k](https://github.com/Hrishi-10k)