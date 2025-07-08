# Disease Prediction from Symptoms using Machine Learning

This project uses a machine learning model to predict a disease based on the symptoms entered by a user. It is built using a supervised learning approach and trained on a publicly available dataset containing binary symptom indicators for common diseases.

---

## Dataset

- **Source**: [Disease Prediction Based on Symptoms - Kaggle](https://www.kaggle.com/datasets/pasindueranga/disease-prediction-based-on-symptoms)
- **Features**:
  - ~132 symptom columns (e.g., `fever`, `headache`, `nausea`) as binary flags (0 or 1)
  - `prognosis` column as the target disease
- **Format**: One-hot encoded CSV
- **Samples**: ~4,900 rows across 40+ disease types

---

## Objectives

- Clean and explore medical symptom data
- Train a machine learning model (Random Forest Classifier)
- Predict diseases from symptom inputs
- Evaluate performance with accuracy and confusion matrix
- Provide a simple Python function for prediction

---
## File Structure

```text
disease_prediction_project/
├── disease_prediction_from_symptoms.ipynb     # Jupyter Notebook with full ML workflow (Colab-ready)
├── Training.csv                               # Dataset with symptoms and disease labels
├── disease_model.pkl                          # Trained Random Forest model (serialized with joblib)
└── README.md                                  # Project overview and usage instructions
```


---
## Model Overview

- **Input**: Binary vector indicating presence/absence of each symptom
- **Output**: Predicted disease name (classification)
- **Model**: `RandomForestClassifier` (with `class_weight='balanced'`)
- **Accuracy**: ~97% on test data

---

## Model Evaluation

```text
Classifier: Random Forest
Accuracy: 0.97
Evaluation: Classification report + Confusion matrix
```
---

##  Sample Prediction Function

```python

def predict_disease(symptoms):
    input_data = {col: 1 if col in symptoms else 0 for col in X.columns}
    input_df = pd.DataFrame([input_data])
    prediction = model.predict(input_df)[0]
    return prediction
```

---


### Output

```text

# Example
predict_disease(['fever', 'nausea', 'headache'])
# Output: 'Typhoid' or another disease label
```

---

## How to Run (Google Colab)
* Upload the dataset (e.g., Training.csv) to Colab

* Run the notebook disease_prediction.ipynb step-by-step

* Use the `predict_disease()` function with custom symptom input

* Optionally export the model for API/web use

---

## Future Work
* Build a Streamlit web app for public input

* Add severity/weighting for symptoms

* Integrate with a chatbot or voice assistant

* Use deep learning or BERT for symptom extraction from text

---

## Acknowledgments
Dataset inspired by UCI & Scikit-learn.
> This project is created for educational and demonstration purposes.

---

## Contact
Created by [Tanu Nanda Prabhu](https://github.com/Tanu-N-Prabhu) – feel free to reach out via GitHub or [tanunprabhu95@gmail.com](tanunprabhu95@gmail.com)
