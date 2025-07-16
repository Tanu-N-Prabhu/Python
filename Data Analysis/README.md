# Data Analysis Made Simple: 25 Real Questions With Clear Python Answers
_A beginner’s guide to mastering data analysis using Pandas and basic Python tools._

## Introduction

Welcome to this beginner-friendly guide to data analysis. If you're learning how to explore and understand data using Python, this file is for you. We focus on real-world questions using simple logic and easy-to-read code snippets. You’ll learn how to manipulate data using Pandas, calculate basic statistics, filter datasets, and visualize results—without diving into complex algorithms.

Each question is accompanied by a clear and direct Python solution, explained in plain English. Whether you're a student, aspiring analyst, or just curious about data, this collection will help you build a strong foundation.

---

## Table of Contents

1. Load and Preview Data  
2. Data Types and Info  
3. Summary Statistics  
4. Filtering Rows  
5. Handling Missing Values  
6. Sorting Data  
7. Grouping and Aggregation  
8. Creating New Columns  
9. Renaming Columns  
10. Dropping Columns or Rows  
11. Counting Unique Values  
12. Value Counts and Frequencies  
13. Conditional Filtering  
14. Combining DataFrames  
15. Working with Dates  
16. Pivot Tables  
17. String Operations  
18. Resetting and Setting Index  
19. Sampling Rows  
20. Applying Functions  
21. Exporting Data  
22. Correlation and Covariance  
23. Plotting Basics  
24. Detecting Outliers  
25. Most Common Mistakes

---

## 1. How do I load a CSV file and preview the first 5 rows?

```python
import pandas as pd

df = pd.read_csv('data.csv')
print(df.head())
```

**Explanation**:  
We use `pd.read_csv()` to read the file and `head()` to preview the first 5 rows of the DataFrame.

---

## 2. How do I check the number of rows and columns in my dataset?

```python
print(df.shape)
```

**Explanation**:  
Returns a tuple where the first number is rows and the second is columns.

---

## 3. How can I see all column names in the dataset?

```python
print(df.columns)
```

**Explanation**:  
`columns` gives a list of all column headers in the DataFrame.

---

## 4. How do I get a summary of my dataset including data types?

```python
print(df.info())
```

**Explanation**:  
`info()` shows non-null counts and data types of each column.

---

## 5. How do I get summary statistics for numeric columns?

```python
print(df.describe())
```

**Explanation**:  
`describe()` gives count, mean, std, min, max, and quartiles for numeric columns.

---

## 6. How do I filter rows where a column equals a certain value?

```python
filtered = df[df['column_name'] == 'value']
```

**Explanation**:  
This selects only rows where `'column_name'` has the value `'value'`.

---

## 7. How can I find missing values in the dataset?

```python
print(df.isnull().sum())
```

**Explanation**:  
`isnull()` creates a mask of missing values; `sum()` counts them per column.

---

## 8. How do I drop rows with missing values?

```python
df_clean = df.dropna()
```

**Explanation**:  
Removes all rows that contain at least one missing value.

---

## 9. How can I sort the data by a specific column?

```python
df_sorted = df.sort_values(by='column_name')
```

**Explanation**:  
Sorts the DataFrame in ascending order based on `'column_name'`.

---

## 10. How do I group data and calculate the average?

```python
df.groupby('group_column')['value_column'].mean()
```

**Explanation**:  
Groups by `'group_column'` and calculates the mean of `'value_column'`.

---

## 11. How can I create a new column based on existing data?

```python
df['new_column'] = df['column1'] + df['column2']
```

**Explanation**:  
This adds two columns together to form a new one.

---

## 12. How do I rename columns?

```python
df.rename(columns={'old_name': 'new_name'}, inplace=True)
```

**Explanation**:  
Use `rename()` to change column names; `inplace=True` applies changes directly.

---

## 13. How can I drop a column?

```python
df.drop(columns=['column_to_drop'], inplace=True)
```

**Explanation**:  
Removes the specified column from the DataFrame.

---

## 14. How can I count unique values in a column?

```python
print(df['column_name'].nunique())
```

**Explanation**:  
`nunique()` counts how many unique values exist in the column.

---

## 15. How do I get the frequency of each value?

```python
print(df['column_name'].value_counts())
```

**Explanation**:  
Shows how often each value appears in the column.

---

## 16. How can I filter rows based on multiple conditions?

```python
df[(df['age'] > 25) & (df['gender'] == 'Male')]
```

**Explanation**:  
Combines conditions using `&` (and), `|` (or), and parentheses.

---

## 17. How do I combine two DataFrames vertically?

```python
combined = pd.concat([df1, df2])
```

**Explanation**:  
`concat()` stacks rows of two DataFrames with the same columns.

---

## 18. How do I convert a column to datetime?

```python
df['date'] = pd.to_datetime(df['date'])
```

**Explanation**:  
`to_datetime()` parses strings into Python datetime objects.

---

## 19. How can I create a pivot table?

```python
df.pivot_table(index='category', values='sales', aggfunc='sum')
```

**Explanation**:  
Creates a summary table where values are aggregated by the chosen function.

---

## 20. How do I find rows that contain a string?

```python
df[df['column'].str.contains('keyword')]
```

**Explanation**:  
Checks each string in the column for the keyword.

---

## 21. How can I reset the index of a DataFrame?

```python
df.reset_index(drop=True, inplace=True)
```

**Explanation**:  
Resets the index back to the default integer values.

---

## 22. How do I randomly sample rows?

```python
df.sample(n=5)
```

**Explanation**:  
Selects 5 random rows from the DataFrame.

---

## 23. How do I apply a function to a column?

```python
df['new'] = df['old'].apply(lambda x: x * 2)
```

**Explanation**:  
`apply()` runs a function on every row in a column.

---

## 24. How do I find the correlation between columns?

```python
print(df.corr())
```

**Explanation**:  
`corr()` computes correlation coefficients between numeric columns.

---

## 25. What are the most common beginner mistakes in data analysis?

- Not checking for missing values  
- Forgetting to reset the index after filtering  
- Misinterpreting groupby results  
- Using inplace operations incorrectly  
- Assuming correlation means causation

---

## Conclusion

These 25 questions and answers cover the essential tools you’ll use in day-to-day data analysis. Practice them with your own datasets and try combining techniques to solve real-world problems. Keep it simple and consistent, and your skills will grow over time.
