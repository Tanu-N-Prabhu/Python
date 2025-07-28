# Level 2: Exploration – Understand the Data

## Goal
Use Exploratory Data Analysis (EDA) techniques to better understand datasets, identify patterns, detect anomalies, and generate hypotheses.

---

## What to Learn

### 1. Descriptive Statistics
Understand key summary metrics:
- **Mean** – The average value.
- **Median** – The middle value in sorted data.
- **Mode** – The most frequent value.
- **Standard Deviation** – How spread out the values are from the mean.
- **Min/Max/Count** – Basic range and size.

> Use `.describe()` in Pandas to get a quick summary.

---

### 2. Correlation & Covariance
- **Correlation** measures the strength and direction of a linear relationship between two variables.
- **Covariance** shows how two variables change together.

```python
df.corr()        # Correlation matrix
df.cov()         # Covariance matrix
```

> Use heatmaps (e.g., in Seaborn) to visualize correlation matrices.

---

