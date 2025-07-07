# Customer Churn Prediction

This project uses machine learning to predict whether a customer is likely to stop using a service (churn) based on their demographic and account behavior data. It's a common real-world problem in telecom, SaaS, and banking industries.

---

## Project Structure

```text

customer_churn_prediction/
├── customer_churn_prediction.ipynb # Complete Google Colab-ready notebook
├── churn.csv # Dataset (uploaded manually in Colab)
├── churn_model.pkl # Saved Random Forest model
├── README.md # Project documentation

```

---

## Requirements

Install the required packages with:

```bash
pip install pandas scikit-learn matplotlib seaborn joblib
```

---

## Dataset Overview

* Dataset contains customer-level information including:

  * Gender, Internet Service, Contract Type, Tenure, Total Charges
  * Target variable: `Churn` (Yes/No)

* Source: Kaggle or IBM Sample Telecom Dataset

---

## Workflow Overview

1. Data Preprocessing
  * Convert `TotalCharges` to numeric
  * Handle missing values
  * One-hot encode categorical variables
  * Normalize numerical values
  * Map target `Churn` from Yes/No → 1/0

2. Model Training
  * Algorithms used:
    * Logistic Regression
    * Random Forest Classifier (with class_weight='balanced')

  * Evaluation Metrics:
    * Confusion Matrix
    * Precision, Recall, F1-score
    * ROC AUC Score
   

3. Results
  * Random Forest performed better with higher ROC AUC
  * Churn detection worked well despite class imbalance

---

## How to Use
1. Open the notebook in [Google Colab](https://colab.research.google.com/)
2. Upload the dataset using the upload cell:
   ```python
   from google.colab import files
   uploaded = files.upload()
   ```
3. Run each cell to process data, train, evaluate, and save the model

---

## Sample Prediction

```python
sample = X_test.iloc[0:1]
prediction = loaded_model.predict(sample)
print("Prediction:", "Churn" if prediction[0] == 1 else "No Churn")
```
---

## Suggested Experiments
* Try using SMOTE to balance classes
* Train a Gradient Boosting or XGBoost model
* Deploy the model using Streamlit

---

## Acknowledgments
Dataset inspired by UCI & Scikit-learn.
> This project is created for educational and demonstration purposes.

---

## Contact
Created by [Tanu Nanda Prabhu](https://github.com/Tanu-N-Prabhu) – feel free to reach out via GitHub or [tanunprabhu95@gmail.com](tanunprabhu95@gmail.com)
