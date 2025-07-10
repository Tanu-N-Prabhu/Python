# Feature Engineering Interview Questions

Feature engineering is the process of transforming raw data into features that better represent the underlying problem to the predictive models. It is often the difference between a good model and a great one.

---

## 1. What is Feature Engineering?

Feature engineering involves selecting, transforming, or creating features that help machine learning models perform better. It includes tasks like handling missing values, encoding categorical data, scaling, and creating interaction terms.

---

## 2. Handling Missing Values

### Techniques:
- **Remove rows/columns** with too many missing values.
- **Impute missing values**:
  - Mean/Median/Mode imputation
  - K-Nearest Neighbors imputation
  - Model-based imputation

### Interview Questions:
- When should you drop missing values vs. impute them?
- How does mean imputation affect variance?

### Mini Case Study:
**Problem:** A housing dataset has missing values in the "LotFrontage" column.  
**Solution:** Impute using the median grouped by neighborhood for better accuracy.

---

## 3. Encoding Categorical Variables

### Techniques:
- **Label Encoding**: Converts categories to integers.
- **One-Hot Encoding**: Creates binary columns for each category.
- **Ordinal Encoding**: Keeps the order of categories.

### Interview Questions:
- What’s the difference between label encoding and one-hot encoding?
- When is label encoding inappropriate?
- How do you handle high-cardinality categorical features?

### Mini Case Study:
**Problem:** Encode the "Education Level" feature with values like ["High School", "Bachelors", "Masters"].  
**Solution:** Use ordinal encoding, as there is a logical order.

---

## 4. Feature Scaling

### Techniques:
- **Standardization (Z-score)**: `(x - mean) / std`
- **Min-Max Scaling**: `(x - min) / (max - min)`
- **Robust Scaling**: Uses median and IQR (for outlier resistance)

### Interview Questions:
- Why is feature scaling important for algorithms like KNN or SVM?
- What’s the difference between normalization and standardization?
- When should you use robust scaling?

### Mini Case Study:
**Problem:** In a health dataset, features like "Age" and "Cholesterol Level" vary greatly in scale.  
**Solution:** Apply Min-Max scaling to normalize input for logistic regression.

---

## 5. Feature Selection

### Techniques:
- **Filter Methods**: Correlation, Chi-Square
- **Wrapper Methods**: Recursive Feature Elimination (RFE)
- **Embedded Methods**: Lasso (L1) Regularization

### Interview Questions:
- What is multicollinearity and how do you detect it?
- How does Lasso help in feature selection?
- What’s the difference between filter, wrapper, and embedded methods?

### Mini Case Study:
**Problem:** Reduce redundancy in a dataset with 100+ features.  
**Solution:** Use Lasso to shrink irrelevant features’ weights to zero.

---

## 6. Creating New Features

### Techniques:
- Interaction terms (e.g., `feature1 * feature2`)
- Aggregations (mean, count, sum per group)
- Date/time decomposition (day, month, weekday, hour)

### Interview Questions:
- How do you generate domain-specific features?
- Can you give an example where feature creation significantly improved model performance?

---

## Summary Table

| Task                  | Technique Examples                     |
|-----------------------|----------------------------------------|
| Missing Values        | Drop, Mean/Median Imputation, KNN      |
| Categorical Encoding  | Label, One-Hot, Ordinal                |
| Feature Scaling       | StandardScaler, MinMaxScaler, Robust  |
| Feature Selection     | RFE, Lasso, Correlation Filter         |
| New Feature Creation  | Ratios, Aggregates, Text/Date Features |

---

## Common Interview Questions

- What are the key steps in preprocessing a dataset?
- How would you handle a dataset with 70% missing values?
- What’s your approach to encoding 100+ unique categories?
- Why is it important to scale features before PCA or SVM?
- How do you detect and handle outliers?

---

> **Next Steps:**  
Now you're ready to dive into deeper ML topics. Continue to [`advanced_topics.md`](./advanced_topics.md) to explore neural networks, transfer learning, model deployment, and more.
