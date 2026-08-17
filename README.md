# B3 Investors - ETL Data Pipeline

## Problem

As part of my journey toward becoming a **Data Engineer**, I wanted to build my first end-to-end ETL pipeline to apply Data Engineering concepts beyond data analysis.

The goal was to work with a real-world dataset and practice fundamental Data Engineering concepts such as data extraction, transformation, validation, file format optimization, environment configuration, and data analysis.

A particular challenge was working with the original CSV dataset. CSV is a row-oriented text format that is less efficient for analytical workloads compared to columnar formats such as Parquet.

---

## Solution

I developed a Python-based ETL pipeline that extracts data from a CSV file, transforms and validates the dataset, and persists the processed data in **Parquet** format for analytical use.

The pipeline follows this flow:

```text
CSV
 │
 ▼
Extract
 │
 ▼
Transform & Validate
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
* Data validation
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

The pipeline successfully produces a cleaned and transformed dataset in Parquet format, which is then consumed by the analysis notebook.

This project allowed me to put several Data Engineering concepts into practice:

* Building an ETL pipeline with Python
* Working with CSV and Parquet
* Data cleaning and transformation
* Data type validation
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
git clone <repository-url>
cd <repository-folder>
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it:

**PowerShell**

```powershell
.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file based on the `.env.example` file.

**Windows PowerShell:**

```powershell
Copy-Item .env.example .env
```

Then update the variables in `.env` according to your local environment.

### 5. Run the ETL pipeline

```bash
python main.py
```

The pipeline will extract, transform, validate, and save the processed dataset as a Parquet file.

### 6. Run the notebook

Start Jupyter Notebook:

```bash
jupyter notebook
```

Open `exploratory_analysis.ipynb` from the `notebooks/` directory and run the analysis using the generated Parquet file.

---

## Technologies

* Python
* Pandas
* PyArrow
* Python-dotenv
* Matplotlib
* Jupyter Notebook
* Parquet
* Git
* GitHub

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

* Automated data quality checks
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

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge\&logo=linkedin\&logoColor=white)](https://www.linkedin.com/in/higormmalves/)
