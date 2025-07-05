# Twitter Sentiment Analysis – NLP with Logistic Regression

This project demonstrates a comprehensive NLP pipeline for classifying tweets as **positive** or **negative** using a labeled Twitter dataset. It includes text preprocessing, vectorization using TF-IDF, model training, evaluation, and saving the model for reuse.

---

## Project Objectives

- Clean and preprocess the tweet text data
- Convert text to numerical features using TF-IDF
- Build a binary classification model with Logistic Regression
- Evaluate using accuracy and a confusion matrix
- Save and reuse the model for predictions

---

## What You'll Learn

- How to build an NLP pipeline using Scikit-learn
- Using `TfidfVectorizer` to transform text
- Splitting data into training/testing sets
- Evaluating model performance with metrics
- Saving models with `joblib`

---

## Project Structure

```text
twitter_sentiment_analysis/
├── sentiment_analysis.ipynb # Complete Google Colab-ready notebook
├── twitter_sentiment_model.pkl # Saved trained model (optional)
├── README.md # Project overview and guide
```


---

## 📥 Dataset

We use a publicly available labeled tweet dataset hosted on GitHub:

📄 [Twitter Sentiment Dataset (CSV)](https://raw.githubusercontent.com/dD2405/Twitter_Sentiment_Analysis/master/train.csv)

- Columns:
  - `tweet` – the text of the tweet
  - `label` – sentiment label (0 = negative, 1 = positive)

---

## How to Run

### 📌 Option 1: Run on Google Colab
- Upload the notebook `sentiment_analysis.ipynb`
- Run all cells in order
- No local setup needed!

### 📌 Option 2: Run Locally
```bash
git clone https://github.com/your-username/twitter-sentiment-analysis.git
cd twitter-sentiment-analysis
pip install -r requirements.txt
jupyter notebook sentiment_analysis.ipynb

```

---

## Sample Output

```python
Accuracy: 0.83
Classification Report:
               precision  recall  f1-score  support
     Negative       0.81     0.84     0.82     296
     Positive       0.84     0.82     0.83     304

Confusion Matrix:
[[248  48]
 [ 55 249]]


```

---

## Next Steps
* Add text preprocessing (e.g., stemming, emoji removal)

* Try other models: Naive Bayes, SVM, or even BERT

* Deploy using Streamlit or FastAPI

* Perform hyperparameter tuning with GridSearchCV

---

## Acknowledgments
Dataset sourced from a Kaggle-hosted GitHub mirror
> Inspired by standard sentiment analysis NLP tutorials

---



## Contact
Created by [Tanu Nanda Prabhu](https://github.com/Tanu-N-Prabhu) – feel free to reach out via GitHub or [tanunprabhu95@gmail.com](tanunprabhu95@gmail.com)

