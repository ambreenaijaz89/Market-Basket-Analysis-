retail-bigdata-project/
├── requirements.txt
├── config.yaml
├── data_raw/            # original uploads (Online Retail.xlsx or CSVs)
├── data/                # processed Parquet/CSV outputs
├── sqlite/              # small lookup dimension DB
├── notebooks/           # exploratory notebooks
│   └── New_Market_Basket_Analysis.ipynb
├── reports/             # saved reports & dashboards (html, csv, xlsx)
├── src/
│   ├── etl.py
│   ├── scale_simulation.py
│   ├── rfm.py
│   ├── basket_rules.py
│   ├── create_sqlite_dims.py
│   └── dashboard_app.py
├── scripts/
│   └── to_csv_from_excel.py
└── .gitignore
________________________________________
How to use
1.	Create a Python virtualenv and install dependencies in requirements.txt.
2.	Put the original Online Retail.xlsx in data_raw/.
3.	Run python scripts/to_csv_from_excel.py to export CSVs (or save CSVs manually).
4.	Run ETL: python src/etl.py --input data_raw/online_retail.csv --out data/fact_retail.parquet.
5.	Run New_Market_Basket_Analysis.ipynb
6.	Run the scaling simulation if you’d like to expand the dataset: python src/scale_simulation.py.
7.	Run RFM segmentation: python src/rfm.py --input data/fact_retail.parquet --out reports/rfm_summary.xlsx.
8.	Generate association rules: python src/basket_rules.py.
9.	Launch dashboard: python src/dashboard_app.py (runs Plotly Dash and saves an HTML snapshot to reports/).
