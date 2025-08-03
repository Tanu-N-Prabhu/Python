# Level 2: Exploration

_Understand the Data_

## Goal
Utilize Exploratory Data Analysis (EDA) techniques to gain a deeper understanding of datasets, identify patterns, detect anomalies, and formulate hypotheses.

---

## What to Learn

### 1. [Descriptive Statistics](https://github.com/Tanu-N-Prabhu/Python/blob/master/Data%20Analysis/Level%202/descriptive_statistics.ipynb)
Understand key summary metrics:
- **Mean** – The average value.
- **Median** – The middle value in sorted data.
- **Mode** – The most frequent value.
- **Standard Deviation** – How spread out the values are from the mean.
- **Min/Max/Count** – Basic range and size.

> Use `.describe()` in Pandas to get a quick summary.

---

### 2. [Correlation & Covariance](https://github.com/Tanu-N-Prabhu/Python/blob/master/Data%20Analysis/Level%202/correlation_covariance.ipynb)
- **Correlation** measures the strength and direction of a linear relationship between two variables.
- **Covariance** shows how two variables change together.

```python
df.corr()        # Correlation matrix
df.cov()         # Covariance matrix
```

> Use heatmaps (e.g., in Seaborn) to visualize correlation matrices.

---

### [3. GroupBy and Pivot Tables](https://github.com/Tanu-N-Prabhu/Python/blob/master/Data%20Analysis/Level%202/groupby_and_pivot_tables.ipynb)

- **GroupBy** lets you split the data, apply a function, and combine the result.
- **Pivot tables reshape** data for summary and comparison.

```python
df.groupby('column_name')['value_column'].mean()
df.pivot_table(values='sales', index='region', columns='product')
```

> GroupBy helps reveal insights across categories.

---

### 4. Outlier Detection & Distributions
- Use boxplots, histograms, or Z-scores to detect **outliers**.
- Understand **data distribution shape**: Normal, skewed, etc.


```python
import seaborn as sns
sns.boxplot(x='column', data=df)
sns.histplot(data=df['column'], kde=True)
```

> Outliers can skew your analysis or indicate anomalies worth further investigation.

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

## Tools
### 1. Pandas Profiling
Quick automated EDA report:

```python
from pandas_profiling import ProfileReport
report = ProfileReport(df)
report.to_notebook_iframe()
```

### 2. Matplotlib
Base Python plotting library. Use for:

- Bar charts
- Line charts
- Histograms

```python
import matplotlib.pyplot as plt
plt.hist(df['column'])
```


### 3. Seaborn
Statistical plotting built on Matplotlib:

- Boxplots
- Violin plots
- Pair plots
- Heatmaps

```python
import seaborn as sns
sns.boxplot(data=df, x='column')
sns.heatmap(df.corr(), annot=True)
```

### 4. Plotly (Optional)
Interactive visualizations:

- Zoomable plots
- Dashboards
- 3D plots

```python
import plotly.express as px
fig = px.scatter(df, x='feature1', y='feature2', color='label')
fig.show()
```

---


## Output
By the end of this level, you should:

- Be able to perform EDA on new datasets.
- Create meaningful charts and summary stats.
- Build a notebook analyzing a public dataset.

> Suggested mini-project: Perform EDA on the Titanic or Iris dataset and document your insights in a notebook.
