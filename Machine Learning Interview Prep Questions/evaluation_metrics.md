# Model Evaluation Metrics

Evaluating machine learning models is critical to understanding how well they perform — especially in real-world settings where accuracy alone is often misleading.

This guide covers the most important classification metrics used in interviews and practice.

---

## 1. Confusion Matrix

A confusion matrix summarizes prediction results:

|                      | Predicted Positive | Predicted Negative |
|----------------------|--------------------|--------------------|
| **Actual Positive**  | True Positive (TP) | False Negative (FN) |
| **Actual Negative**  | False Positive (FP)| True Negative (TN)  |

---

## 2. Accuracy

**Formula:**  
`Accuracy = (TP + TN) / (TP + FP + FN + TN)`

**Use Case:**  
Good when class distribution is balanced.

**Limitation:**  
Misleading when data is imbalanced.

---

## 3. Precision

**Formula:**  
`Precision = TP / (TP + FP)`

**Use Case:**  
Used when **false positives** are more costly.  
> Example: Classifying a genuine email as spam.

---

## 4. Recall (Sensitivity / True Positive Rate)

**Formula:**  
`Recall = TP / (TP + FN)`

**Use Case:**  
Used when **false negatives** are more costly.  
> Example: Failing to detect a cancer case.

---

## 5. F1-Score

**Formula:**  
`F1 = 2 * (Precision * Recall) / (Precision + Recall)`

**Use Case:**  
Best when you need a **balance** between precision and recall.

---

## 6. Specificity (True Negative Rate)

**Formula:**  
`Specificity = TN / (TN + FP)`

**Use Case:**  
Helpful when combined with sensitivity for binary classification.

---

## 7. ROC Curve and AUC

- **ROC Curve**: Plots **True Positive Rate (Recall)** against **False Positive Rate**.
- **AUC (Area Under Curve)**: A value between 0 and 1 that summarizes the overall ability of the model to discriminate between classes.

**Use Case:**  
Best for comparing different classifiers and thresholds.

---

## 8. Log Loss (Cross-Entropy Loss)

**Formula (conceptual):**  
`Log Loss = -1/N * Σ [y * log(p) + (1 - y) * log(1 - p)]`

Where:
- `y` = true label (0 or 1)
- `p` = predicted probability

**Use Case:**  
Used in probabilistic classifiers. Penalizes confident but wrong predictions heavily.

---

## When to Use What?

| Scenario | Best Metric |
|----------|-------------|
| Balanced dataset | Accuracy |
| Cost of false positives is high | Precision |
| Cost of false negatives is high | Recall |
| Need balance between precision and recall | F1-Score |
| Comparing model performance at different thresholds | ROC-AUC |

---

## Interview Questions

- What is the difference between precision and recall?
- Why is accuracy not enough for model evaluation?
- What is ROC-AUC and when should you use it?
- Explain F1-Score and when it's more appropriate than accuracy.
- How do you handle class imbalance in evaluation?

---

>  **Next Steps:**  
Move on to [`feature_engineering.md`](./feature_engineering.md) to learn how to prepare and transform raw data for modeling.
