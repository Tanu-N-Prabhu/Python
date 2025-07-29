# Level 2: Exploration

_Understand the Data_

## Goal
Utilize Exploratory Data Analysis (EDA) techniques to gain a deeper understanding of datasets, identify patterns, detect anomalies, and formulate hypotheses.

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

### 3. GroupBy and Pivot Tables
- **GroupBy** lets you split the data, apply a function, and combine the result.
- **Pivot tables reshape** data for summary and comparison.

```
df.groupby('column_name')['value_column'].mean()
df.pivot_table(values='sales', index='region', columns='product')
```

> GroupBy helps reveal insights across categories.

---

### 4. Outlier Detection & Distributions
- Use boxplots, histograms, or Z-scores to detect **outliers**.
- Understand **data distribution shape**: Normal, skewed, etc.


```
import seaborn as sns
sns.boxplot(x='column', data=df)
sns.histplot(data=df['column'], kde=True)
```

> Outliers can skew your analysis or indicate anomalies worth investigating.

---

### 5. EDA Workflow
A typical workflow includes:

- Data overview - shape, info, head
- Missing values & data types
- Descriptive statistics
- Visualizations
- Hypothesis generation

> Always keep asking: What does the data tell me?

---

