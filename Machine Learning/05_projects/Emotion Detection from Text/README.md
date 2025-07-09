# Emotion Detection from Text

This project builds a machine learning pipeline to detect **emotions** from English text (tweets or phrases). It uses a TF-IDF-based feature extraction and a Logistic Regression model trained on a Kaggle dataset of 40,000 labeled samples.

---

## Dataset

- **Name**: Emotion Detection from Text
- **Source**: [Kaggle Dataset](https://www.kaggle.com/datasets/pashupatigupta/emotion-detection-from-text)
- **Size**: ~40,000 samples
- **Columns**:
  - `tweet_id`: Unique tweet ID
  - `sentiment`: Target emotion label (e.g., happiness, anger, neutral, etc.)
  - `content`: The tweet text to be classified

---

## Project Structure

```text

Emotion Detection from Text/
├── emotion_detection_from_text.ipynb # Complete Google Colab-ready notebook
├── emotion_detection.csv # Dataset (uploaded manually in Colab)
├── README.md # Project documentation

```

---

## Objectives

- Clean and preprocess raw text data
- Convert text to numeric features using TF-IDF
- Train a Logistic Regression model with class balancing
- Evaluate the model using classification metrics
- Predict the emotion for any new custom input

---

## Model Overview

- **Vectorizer**: `TfidfVectorizer(stop_words='english', max_df=0.7)`
- **Classifier**: `LogisticRegression(max_iter=1000, class_weight='balanced')`
- **Handling imbalance**: Class weighting + stratified split

---

## Performance

The model is evaluated using:
- **Accuracy**
- **Precision, Recall, F1-score (macro avg)**
- **Confusion Matrix**
- **Prediction probabilities for each class**

The model performs well across a wide range of emotions, despite the imbalanced class distribution.

---

## Example Output

Input:
```python
predict_emotion("I'm feeling amazing and full of joy today!")
```
---

### Output

```text
Prediction Probabilities:
happiness: 0.34
relief: 0.159
love: 0.154
...
Predicted Emotion: happiness
```
---

## Requirements

```python
pandas
numpy
scikit-learn
matplotlib
seaborn
```

Install Using

```
pip install -r requirements.txt
```

---

## How to Use (Google Colab)
* Upload your dataset (`emotion_dataset.csv`) to Colab
* Copy and run the notebook
* Call `predict_emotion("your sentence here")` to get predictions

---

## Future Improvements
* Upgrade to transformer models like BERT for better semantic understanding
* Build a web UI using Streamlit
* Add interactive dashboard for visualizing real-time emotions

---

## Acknowledgments
Dataset inspired by UCI & Scikit-learn.
> This project is created for educational and demonstration purposes.

---

## Contact
Created by [Tanu Nanda Prabhu](https://github.com/Tanu-N-Prabhu) – feel free to reach out via GitHub or [tanunprabhu95@gmail.com](tanunprabhu95@gmail.com)
