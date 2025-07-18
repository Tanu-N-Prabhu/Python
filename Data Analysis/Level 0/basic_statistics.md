# Basic Statistics with Python
_Learn to Compute and Understand Mean, Median, and Standard Deviation_

---

## Overview

This section covers fundamental statistical measures used in data analysis — **mean**, **median**, and **standard deviation** — using pure Python and `pandas`. These concepts help summarize and describe data effectively and are crucial for anyone working with data.

---

## 1. Mean (Average)

The **mean** is the average of all numbers. It gives a central value for a dataset.

### Formula:
Mean = (Sum of all values) / (Number of values)

### Python Example:
```python
import pandas as pd

# Sample data
data = [10, 20, 30, 40, 50]

# Using plain Python
mean_val = sum(data) / len(data)
print("Mean (Python):", mean_val)

# Using pandas
df = pd.DataFrame(data, columns=["Score"])
print("Mean (pandas):", df["Score"].mean())
```

---

## 2. Median

The **median** is the middle value in a sorted list. It is less affected by outliers than the mean.

### How it works:
- If odd number of elements → middle value
- If even number of elements → average of two middle values

### Python Example:
```python
# Odd number of elements
data = [10, 20, 30, 40, 50]
median_val = sorted(data)[len(data)//2]
print("Median (manual):", median_val)

# Even number of elements
data_even = [10, 20, 30, 40]
mid1 = data_even[len(data_even)//2 - 1]
mid2 = data_even[len(data_even)//2]
median_even = (mid1 + mid2) / 2
print("Median (even):", median_even)

# Using pandas
df = pd.DataFrame(data, columns=["Score"])
print("Median (pandas):", df["Score"].median())
```

---

## 3. Standard Deviation

The **standard deviation** measures how spread out numbers are from the mean. A higher value indicates more variability in the data.

### Python Example:
```python
import math

# Manual standard deviation
data = [10, 20, 30, 40, 50]
mean_val = sum(data) / len(data)
squared_diffs = [(x - mean_val) ** 2 for x in data]
std_dev = math.sqrt(sum(squared_diffs) / len(data))
print("Standard Deviation (manual):", std_dev)

# Using pandas
df = pd.DataFrame(data, columns=["Score"])
print("Standard Deviation (pandas):", df["Score"].std(ddof=0))  # population std
```

---

## Summary Table

| Metric              | Description                                | Python Function        |
|---------------------|--------------------------------------------|------------------------|
| Mean                | Average value                              | `mean()`               |
| Median              | Middle value in sorted data                | `median()`             |
| Standard Deviation  | Spread of data from the mean               | `std()`                |

---

## Next Steps

- Try calculating these metrics on your dataset.
- Learn how these metrics influence machine learning models.
- Explore data visualization techniques to complement statistics.

