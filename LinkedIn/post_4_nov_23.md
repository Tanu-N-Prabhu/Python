# **The Day a Simple Bug Saved My Model**

I once spent hours tuning a model that refused to improve.  
Different settings, different ideas, nothing worked.

Then I finally found the real issue:

### **The data had repeated rows.**  
That tiny detail changed *everything.*


Your model’s performance is often hindered by small data issues, rather than advanced algorithms.


### **Example**

```python
import pandas as pd

data = pd.DataFrame({'Value': [5, 5, 10]})
print(data.drop_duplicates())
```

**Output:**  
Keeps one `5` and one `10`, all repeated rows are removed.


This small check can save hours in your workflow.

**Has this ever happened to you?**  
Share your version!

