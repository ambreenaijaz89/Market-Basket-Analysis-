# Retail Big Data Project – Repository Structure

The **retail-bigdata-project** is structured to support an end-to-end big data analytics workflow, from raw data ingestion to advanced analysis and reporting. Each directory and file has a specific role to ensure scalability, clarity, and maintainability.

## Root Configuration Files
- **requirements.txt**  
  Contains all Python library dependencies required to run the project.
- **config.yaml**  
  Stores configurable parameters such as file paths, thresholds, and analysis settings.
- **.gitignore**  
  Ensures unnecessary or sensitive files are excluded from version control.

## Data Directories
- **data_raw/**  
  Holds original, unmodified data files (e.g., *Online Retail.xlsx* or CSVs). This preserves the raw source data.
- **data/**  
  Contains cleaned and processed datasets, typically stored in CSV or Parquet format for efficient analysis.
- **sqlite/**  
  Includes a lightweight SQLite database used for lookup and dimension tables (e.g., products or customers).

## Notebooks
- **notebooks/**  
  Used for exploratory data analysis and experimentation.
  - **New_Market_Basket_Analysis.ipynb**: Performs EDA, market basket analysis, and preliminary insights generation.

## Reports
- **reports/**  
  Stores final outputs such as analytical reports, dashboards, and summary files in formats like HTML, CSV, or XLSX.

## Source Code
- **src/**  
  Contains the core logic and reusable modules of the project:
  - **etl.py** – Handles data extraction, cleaning, and transformation.
  - **scale_simulation.py** – Simulates data scaling for big data performance testing.
  - **rfm.py** – Performs customer segmentation using Recency, Frequency, and Monetary analysis.
  - **basket_rules.py** – Generates association rules for market basket analysis.
  - **create_sqlite_dims.py** – Builds and manages SQLite dimension tables.
  - **dashboard_app.py** – Supports dashboard creation and visualization.

## Scripts
- **scripts/**  
  Includes utility scripts for data preparation tasks.
  - **to_csv_from_excel.py**: Converts Excel files into CSV format.

---

This structured layout supports reproducible research, clear separation of responsibilities, and easy scaling from exploratory analysis to production-ready analytics.
