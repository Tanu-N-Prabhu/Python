# The Power of Simple Data Checks  

## Catch issues early, stay confident later  

### Introduction
Strong data work begins with checking for missing values. This step is simple, yet it protects your analysis from hidden errors  

### Problem Statement
Many projects fail because missing values are ignored. This creates weak patterns and confusing results  

### Solution
Do a quick check for empty entries before any model work. A tiny script can keep your dataset clean and reliable  

### Code  
```python
import pandas as pd
data = pd.DataFrame({'Age':[21,None,30]})
print(data.isna().sum())
```

### Conclusion
A clean start leads to a strong finish. Always check for missing values, and your data science workflow will stay smooth
