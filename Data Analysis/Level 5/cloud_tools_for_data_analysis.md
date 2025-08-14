# Cloud Tools for Data Analysis  
_Integrating Google Sheets, BigQuery, and Other Cloud Platforms into Your Workflow_

## Overview
This section introduces cloud-based tools that extend your data analysis capabilities beyond your local machine.  
Cloud tools enable **collaboration, scalability, and real-time access** to data—making them essential for modern analysts.

We’ll focus on:
- **Google Sheets** – Lightweight, collaborative spreadsheet tool
- **BigQuery** – Google’s fully-managed, serverless data warehouse
- **Other Cloud Options** – AWS Athena, Snowflake, etc. (optional exploration)

---

## Why Use Cloud Tools?
- **Collaboration** – Multiple users can view & edit data in real time.
- **Scalability** – Handle datasets much larger than your computer’s memory.
- **Integration** – Direct connections to APIs, databases, and BI tools.
- **Version Control** – Track changes and restore earlier versions.

---

## 1. Google Sheets for Data Analysis
Google Sheets is perfect for **quick data entry, lightweight analysis, and sharing results**.

**Common Uses:**
- Upload CSVs for quick collaboration
- Use built-in formulas for quick calculations
- Connect with Python via the `gspread` library

**Example: Connect Python to Google Sheets**
```python
import gspread
from google.oauth2.service_account import Credentials

# Authenticate
creds = Credentials.from_service_account_file("service_account.json")
client = gspread.authorize(creds)

# Open Sheet
sheet = client.open("SalesData").sheet1

# Read Data
data = sheet.get_all_records()
print(data)
```

---

## 2. BigQuery for Large-Scale Analysis
BigQuery is ideal when:
- Your dataset is **too large** for Pandas
- You need **SQL-based** analysis
- You require **fast querying at scale**

**Workflow:**
1. Upload your dataset to Google Cloud Storage
2. Import into BigQuery
3. Run SQL queries directly in the console or via Python’s `google-cloud-bigquery` library

**Example: Query BigQuery in Python**
```python
from google.cloud import bigquery

client = bigquery.Client()
query = """
SELECT region, SUM(sales) as total_sales
FROM `project_id.dataset.sales`
GROUP BY region
ORDER BY total_sales DESC
"""
results = client.query(query).to_dataframe()
print(results)
```

---

## 3. Other Cloud Data Tools
While Google Sheets and BigQuery are common starting points, you can also explore:
- **AWS Athena** – Serverless SQL queries on S3
- **Snowflake** – Cloud data warehouse with high performance
- **Microsoft Fabric / Azure Synapse** – Enterprise-scale analytics

---

## Best Practices
- Always **use service accounts** for secure authentication
- Avoid storing credentials in code—use environment variables or secret managers
- Test queries locally with small datasets before running on full data
- Keep backups in CSV/Parquet formats

---

## Tools Required
- Python 3.x  
- Google Cloud SDK  
- Libraries:  
```bash
pip install gspread google-auth google-cloud-bigquery pandas
```

---

## Output
By the end of this module, you’ll be able to:
- Read and write to Google Sheets programmatically
- Run scalable SQL queries on BigQuery
- Integrate cloud tools into your end-to-end data workflows

---

## License
Open-source under the MIT License
