# Income-Demographics-Pipeline-Airflow-S3-Snowflake-Tableau-

A complete **Data Engineering to BI** workflow built with modern tools:  
from raw CSVs ➜ cloud storage ➜ warehouse ➜ business dashboard.

---

## 💼 Overview
This end-to-end project demonstrates:
1. 🧹 **Exploratory Data Analysis (EDA)** with Python & Pandas  
2. 🔄 **ETL Automation** using **Apache Airflow**, **Amazon S3**, and **Snowflake**  
3. 📊 **Interactive Visualizations** in Tableau for strategic insights

---

## 📊 Dataset Summary
- **Source:** UCI Adult Census Income Dataset
- **Total Final Records:** `26,516`
- **High Income Records (`>50K`):** ~`6,300` (~24%)
- **Features After Cleaning:** 12
- **Categorical Columns Encoded:**  
  `marital_status`, `education`, `workclass`, `sex`, `occupation`, etc.
- **Threshold Column:** Added (`0 = ≤50K`, `1 = >50K`)

---

## ⚙️ Tech Stack
| Tool       | Purpose                      |
|------------|------------------------------|
| **Python** | EDA and preprocessing         |
| **Apache Airflow** | DAGs to automate S3 ➜ Snowflake |
| **Amazon S3** | Store cleaned CSV file      |
| **Snowflake** | Load and query data warehouse |
| **Tableau** | Build professional dashboards |

---

## 🚀 Pipeline Flow

1. ✅ **Cleaned CSV file** uploaded to S3 Bucket  
2. ✅ **Airflow DAG** (`s3_to_snowflake_pipeline`) scheduled & triggered  
3. ✅ **Snowflake** uses COPY INTO to load data from S3 stage  
4. ✅ **Tableau Dashboard** connects live to Snowflake  

---

## 🏢 Snowflake Table Info
```sql
CREATE OR REPLACE TABLE ADULT_DATA (
    age INT,
    workclass INT,
    education INT,
    marital_status INT,
    occupation INT,
    relationship INT,
    race INT,
    sex INT,
    capital_gain INT,
    capital_loss INT,
    hours_per_week INT,
    threshold FLOAT
);
