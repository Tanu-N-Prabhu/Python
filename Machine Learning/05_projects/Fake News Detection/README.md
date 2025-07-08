# Fake News Detection using Machine Learning

Fake news has become one of the most pressing challenges in the information age. This project aims to build a machine learning model that can automatically classify news articles as **FAKE** or **REAL** based on their content.

---

## Project Overview

- **Goal**: Detect whether a news article is fake or real using NLP and ML.
- **Dataset**: [ISOT Fake and Real News Dataset](https://www.kaggle.com/datasets/clmentbisaillon/fake-and-real-news-dataset)
- **Approach**: Text cleaning → TF-IDF → Classification → Evaluation → Prediction

---

## Key Features

- Preprocess and clean raw news article content
- Transform text into TF-IDF features
- Train two ML classifiers:
  - Logistic Regression
  - Random Forest
- Evaluate model using:
  - Accuracy
  - Precision, Recall, F1-score
  - ROC-AUC
- Save model for deployment
- Predict new inputs using a custom prediction function

---

## Dataset Details

| Feature | Description |
|---------|-------------|
| `title` | Headline of the news article |
| `text`  | Full article content |
| `label` | Target variable (FAKE = 0, REAL = 1) |

- The dataset contains two files: `Fake.csv` and `True.csv`
- Total articles: ~20,000

---

## How to Run

1. **Clone this repository** or upload notebook to Google Colab.
2. **Download the dataset** from [Kaggle](https://www.kaggle.com/datasets/clmentbisaillon/fake-and-real-news-dataset).
3. Upload both `Fake.csv` and `True.csv` to your notebook environment.
4. Run the `fake_news_detection.ipynb` notebook step-by-step.

---

## Example Prediction

```python
sample = "Breaking: Scientists discover water on Mars!"
predict_news(sample)  # Output: REAL or FAKE
```

---

## Evaluation Metrics

| Model               | Accuracy | ROC AUC | Comments            |
| ------------------- | -------- | ------- | ------------------- |
| Logistic Regression | \~95%    | >0.98   | Fast, interpretable |
| Random Forest       | \~96%    | >0.98   | More robust, slower |

---

## Model Files
* `tfidf_vectorizer.pkl`: Trained TF-IDF vectorizer

* `fake_news_rf_model.pkl`: Trained Random Forest classifier

These can be loaded for use in a Streamlit app or Flask API.

---

## Improvements
* Use deep learning models like BERT or RoBERTa

* Include article source, metadata, author info

* Deploy as a web app using Streamlit

* Add a real-time fake news API

---

## Acknowledgments
Dataset inspired by UCI & Scikit-learn.
> This project is created for educational and demonstration purposes.

---

## Contact
Created by [Tanu Nanda Prabhu](https://github.com/Tanu-N-Prabhu) – feel free to reach out via GitHub or [tanunprabhu95@gmail.com](tanunprabhu95@gmail.com)
