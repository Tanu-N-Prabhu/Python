  # Loan Approval Prediction

This machine learning project predicts whether a loan application will be approved, using real-world financial and demographic data.

---

## Dataset

- **Source:** [Loan Prediction Dataset – Kaggle](https://www.kaggle.com/datasets/altruistdelhite04/loan-prediction-problem-dataset)
- **File:** `train.csv`
- **Target column:** `Loan_Status` (Y = Approved, N = Rejected)

---

## Project Structure

```text
loan_approval_prediction/
├── loan_approval_prediction.ipynb # Main notebook (Google Colab-ready)
├── loan_data.csv # Dataset file (uploaded manually)
├── loan_approval_model.pkl # Saved Random Forest model
├── README.md # Documentation and instructions
```

---



## Model Pipeline

### Preprocessing
- Handle missing values
- Encode categorical variables
- Normalize numerical values

### Algorithms Used
- Logistic Regression
- Random Forest Classifier

### Evaluation Metrics
- Classification report
- ROC AUC Score
- Confusion Matrix

---

## How to Run

1. Open `loan_approval_prediction.ipynb` in Google Colab
2. Upload `loan_data.csv` (renamed from `train.csv`)
3. Run each cell step-by-step
4. Use saved `.pkl` model to make predictions on new data

---

## Example Output

```python
Prediction: Approved ✅
```

---

## Acknowledgments
Dataset inspired by UCI & Scikit-learn.
> This project is created for educational and demonstration purposes.

---

## Contact
Created by [Tanu Nanda Prabhu](https://github.com/Tanu-N-Prabhu) – feel free to reach out via GitHub or [tanunprabhu95@gmail.com](tanunprabhu95@gmail.com)
