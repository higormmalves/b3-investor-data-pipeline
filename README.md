# B3 Investors - ETL Data Pipeline

## Problem

B3 publishes historical data on individual investor demographics as a raw, row-oriented CSV file with inconsistent headers and no defined schema, not ready for direct analytical consumption.

Row-oriented formats like CSV also don't scale well for analytical workloads: every query has to scan full rows even when only a few columns are needed, and there's no compression or embedded schema to catch type errors early.

This project builds a small ETL pipeline that turns that raw file into a clean, typed, columnar dataset ready for analysis.

---

## Solution

I developed a Python-based ETL pipeline that extracts data from a CSV file, cleans and transforms the dataset, and persists the processed data in **Parquet** format for analytical use.

The pipeline follows this flow:

```text
CSV
 │
 ▼
Extract
 │
 ▼
Transform
 │
 ▼
Load as Parquet
 │
 ▼
Analysis
```

### Extract

The pipeline reads the original CSV dataset using **Pandas**.

### Transform

During the transformation stage, the data is cleaned and prepared for analysis, including:

* Data type conversion
* Handling missing and invalid values
* Column standardization
* Creation of derived metrics

### Load

The transformed dataset is persisted in **Parquet** format.

I chose Parquet to practice working with a **columnar storage format** commonly used in modern Data Engineering and analytical environments.

The resulting Parquet file is then used as the data source for the project's Jupyter Notebook.

### Configuration

Environment-specific file paths are stored in a `.env` file instead of being hardcoded in the Python code.

A `.env.example` file is provided as a template for the required environment variables.

---

## Results

The pipeline transforms an 11-row raw CSV (2016–2026) into a cleaned, typed, analysis-ready Parquet file with standardized column names.

| Metric                          | 2016    | 2026      |
|----------------------------------|---------|-----------|
| Total individual investors (B3)  | 564,529 | 6,573,856 |
| Female share                     | 23.10%  | 26.64%    |
| Male share                       | 76.90%  | 73.36%    |

Female participation grew from 23.10% to 26.64% over the period — a modest but consistent increase, even as the total number of individual investors grew more than 11x.

Full exploratory analysis available in `notebooks/exploratory_analysis.ipynb`.

This project allowed me to put several Data Engineering concepts into practice:

* Building an ETL pipeline with Python
* Working with CSV and Parquet
* Data cleaning and transformation
* Data type conversion
* Handling missing and invalid data
* Environment variable management
* Separating configuration from application code
* Structuring a Python Data Engineering project
* Using Git and GitHub for version control

### What I Learned

As my first ETL pipeline, this project was an opportunity to apply Data Engineering concepts in practice and understand the reasoning behind each stage of a data pipeline.

It helped me bridge the gap between my previous experience in **Data Analysis / BI** and the concepts required for **Data Engineering**.

The project also gave me hands-on experience transforming raw data into a processed, analysis-ready dataset while applying basic software engineering and version control practices.

---

## How to Run

### 1. Clone the repository

```bash
git clone https://github.com/higormmalves/b3-investors-etl-pipeline.git
cd b3-investors-etl-pipeline
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it:

**macOS/Linux**
```bash
source .venv/bin/activate
```

**Windows PowerShell**
```powershell
.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file based on the `.env.example` file.

**macOS/Linux**
```bash
cp .env.example .env
```

**Windows PowerShell**
```powershell
Copy-Item .env.example .env
```

Then update the variables in `.env` according to your local environment.

### 5. Run the ETL pipeline

```bash
python main.py
```

The pipeline will extract, transform, and save the processed dataset as a Parquet file.

### 6. Run the notebook

Start Jupyter Notebook:

```bash
jupyter notebook
```

Open `exploratory_analysis.ipynb` from the `notebooks/` directory and run the analysis using the generated Parquet file.

---

## Technologies

**Pipeline:** Python · Pandas · PyArrow · python-dotenv

**Analysis:** Jupyter Notebook · Matplotlib

**Tooling:** Git · GitHub

---

## Project Structure

```text
etl-data-pipeline/
│
├── data/
│   ├── raw/
│   │   └── b3_investors_data.csv
│   └── processed/
│       └── b3_investors_data.parquet
│
├── notebooks/
│   └── exploratory_analysis.ipynb
│
├── src/
│   ├── __init__.py
│   ├── extract.py
│   ├── transform.py
│   └── load.py
│
├── .env.example
├── .gitignore
├── main.py
├── requirements.txt
└── README.md
```

---

## Future Improvements

As I continue developing my Data Engineering skills, I plan to evolve this project by adding:

* Automated data quality/validation checks (schema, ranges, duplicates)
* Unit tests
* Docker
* Workflow orchestration
* Cloud storage
* CI/CD
* Pipeline monitoring

---

## About Me

I am a **Data / BI Analyst transitioning into Data Engineering**, and this project is part of my hands-on learning journey.

My goal is to continuously apply Data Engineering concepts through practical projects while building a stronger foundation in **Python, SQL, ETL, data pipelines, cloud technologies, and modern data platforms**.

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/higormmalves/)
