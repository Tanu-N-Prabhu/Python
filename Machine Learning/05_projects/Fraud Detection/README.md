# Credit Card Fraud Detection

This project builds a machine learning model to detect fraudulent transactions using the popular [Credit Card Fraud Detection dataset](https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud). It demonstrates the full ML workflow including EDA, preprocessing, model training, evaluation, and saving the model.

---

## Project Structure

```text
fraud_detection/
├── fraud_detection.ipynb # Main Colab-ready notebook
├── README.md # This file

```

---

## Requirements

Install via pip:

```bash
pip install pandas scikit-learn matplotlib seaborn joblib
```

---

## ML Pipeline Overview
1. Dataset
    * Source: [Kaggle - Credit Card Fraud Detection](https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud)
    * Classes:
        * `0` = Legitimate transaction
        * `1` = Fraudulent transaction (only 0.17% of the data)

2. Preprocessing
    * Scaled `Time` and `Amount` features using `StandardScaler`
    * Train-test split using `stratify` to preserve class distribution

3. Model
    * Algorithm: `RandomForestClassifier`
    * `class_weight='balanced'` to handle class imbalance
    * Evaluated using:
        * Classification report
        * Confusion matrix
        * ROC-AUC score and curve

4. Results
    * High precision and recall for the minority class (fraud)
    * ROC-AUC used for overall performance
    * Saved model using `joblib`
  
---

## How to Run on Colab
1. Open Colab
2. Upload `fraud_detection.ipynb`
3. Upload the `creditcard.csv` file using the Colab file upload cell
4. Run all cells

---

## Sample Prediction

```python
sample = X_test.iloc[0:1]
loaded_model.predict(sample)  # Output: [0] or [1]
```

---

### Next Steps
* Try SMOTE or undersampling techniques
* Experiment with XGBoost, LightGBM, or Logistic Regression
* Deploy as a web app using Streamlit or FastAPI

---

## Acknowledgments
Dataset inspired by UCI & Scikit-learn.
> This project is created for educational and demonstration purposes.

---

## Contact
Created by [Tanu Nanda Prabhu](https://github.com/Tanu-N-Prabhu) – feel free to reach out via GitHub or [tanunprabhu95@gmail.com](tanunprabhu95@gmail.com)
