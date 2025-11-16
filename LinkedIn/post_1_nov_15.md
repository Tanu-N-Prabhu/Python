# Clean Data Builds Smart Models

## Garbage in means garbage out

<p align = "right"><b><i>Written By: Tanu Nanda Prabhu</i></b></p>

## Introduction
Every great data project starts with clean data. Without it, even the best algorithms produce weak results.

## Problem Statement
Messy, missing, and duplicate data can destroy accuracy and make insights unreliable.

## Solution
Use simple Python steps to clean your dataset before analysis. A few lines of code can save hours of frustration

## Code

```python
import pandas as pd
data = pd.DataFrame({'Age':[25,None,30,25]})
data = data.drop_duplicates().fillna(data.mean())
print(data)
```

## Conclusion
Good models start with good data. Keep your data clean, and your insights will always be stronger
