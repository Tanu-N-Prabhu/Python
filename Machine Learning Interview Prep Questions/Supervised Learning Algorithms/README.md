# Supervised Learning Algorithms

This repository contains clean, beginner-friendly, and fully-documented **Supervised Machine Learning algorithms**, implemented from scratch using only **NumPy and Python**. 

It is perfect for:

- Students preparing for interviews
- Educators and mentors
- Anyone curious to understand what happens under the hood of ML models, without relying on `scikit-learn` or black-box tools.

---

## What is Supervised Learning?

Supervised learning is a type of machine learning where the algorithm learns from **labeled data**, meaning each input (`X`) comes with a known output (`y`).

The goal is to learn a function that maps inputs to correct outputs:

$$[
f(x) \approx y
]$$

Supervised learning includes both:
- **Classification**: predicting categories
- **Regression**: predicting continuous values

---

## Repository Structure

### Supervised Learning Algorithms Overview

| Algorithm                | Description                                              | Purpose                                           | Best Use-Cases                                                |
|:--------------------------|:----------------------------------------------------------|:---------------------------------------------------|:----------------------------------------------------------------|
| **[Linear Regression](https://github.com/Tanu-N-Prabhu/Python/tree/master/Machine%20Learning%20Interview%20Prep%20Questions/Supervised%20Learning%20Algorithms/Linear%20Regression)**    | Models the relationship between input features and a continuous output. | Make numeric predictions from known features.     | Predicting house prices, estimating sales, or revenue.         |
| **[Logistic Regression](https://github.com/Tanu-N-Prabhu/Python/tree/master/Machine%20Learning%20Interview%20Prep%20Questions/Supervised%20Learning%20Algorithms/Logistic%20Regression)**  | Estimates the probability of data belonging to a class.  | Classify binary outcomes (yes/no, true/false).    | Spam detection, predicting customer churn, or purchase.        |
| **[Decision Trees](https://github.com/Tanu-N-Prabhu/Python/tree/master/Machine%20Learning%20Interview%20Prep%20Questions/Supervised%20Learning%20Algorithms/Decision%20Trees)**       | Splits data based on feature values to make decisions.   | Build simple, rule-based prediction models.       | Customer segmentation, diagnosing diseases.                   |
| **[Random Forest](https://github.com/Tanu-N-Prabhu/Python/tree/master/Machine%20Learning%20Interview%20Prep%20Questions/Supervised%20Learning%20Algorithms/Random%20Forest)**        | Combines multiple decision trees (bagging).              | Increase accuracy and reduce overfitting.         | Credit scoring, predicting loan defaults, or stock trends.     |
| **[Support Vector Machines (SVM)](https://github.com/Tanu-N-Prabhu/Python/tree/master/Machine%20Learning%20Interview%20Prep%20Questions/Supervised%20Learning%20Algorithms/Support%20Vector%20Machines)** | Finds the best boundary to separate classes.        | Maximize separation between classes.              | Image classification, handwriting, and face recognition.       |
| **[k-Nearest Neighbors (k-NN)](https://github.com/Tanu-N-Prabhu/Python/tree/master/Machine%20Learning%20Interview%20Prep%20Questions/Supervised%20Learning%20Algorithms/K-Nearest%20Neighbors)** | Classifies based on the labels of nearby points.      | Make predictions based on similarity.             | Recommender systems, anomaly/intrusion detection.             |
| **[Naive Bayes](https://github.com/Tanu-N-Prabhu/Python/tree/master/Machine%20Learning%20Interview%20Prep%20Questions/Supervised%20Learning%20Algorithms/Naive%20Bayes)**          | Uses probabilities and Bayes' Theorem to classify data. | Handle classification problems with simplicity.   | Spam filtering, sentiment analysis, and  text classification.      |
| **[Ensemble Learning](https://github.com/Tanu-N-Prabhu/Python/tree/master/Machine%20Learning%20Interview%20Prep%20Questions/Supervised%20Learning%20Algorithms/Ensemble%20Learning)**    | Combines multiple models (e.g., trees) to boost performance. | Build stronger models by combining weak ones.     | Fraud detection, large-scale predictions, model competitions. |

---

## How to Use This Repo

1. **Clone the repository:**

   ```bash
   git clone https://github.com/your-username/supervised-ml-algorithms.git
   cd supervised-ml-algorithms
   ```

2. Open the notebooks:

    * You can use [Jupyter Notebook](https://jupyter.org/) or [Google Colab](https://colab.research.google.com/)
    * Each .ipynb file is self-contained with step-by-step explanations

3. Run cells step-by-step to learn and see the model in action.

---

## Requirements
All notebooks use just:
* Python 3.x
* NumPy
* Matplotlib (for some visualizations)

To install the required packages:

```python
pip install numpy matplotlib
```

---

## Algorithms Covered

###  Regression

| Model                   | Description                                               |
| ----------------------- | --------------------------------------------------------- |
| **Linear Regression**   | Fit a straight line using gradient descent or closed-form |
| **Logistic Regression** | Classify data using sigmoid and binary cross-entropy      |

---

### Tree-Based Models

| Model             | Description                                                |
| ----------------- | ---------------------------------------------------------- |
| **Decision Tree** | Recursively splits data based on Gini impurity             |
| **Random Forest** | Ensemble of decision trees trained on bootstrapped subsets |

---

### Distance-Based & Margins

| Model                            | Description                                           |
| -------------------------------- | ----------------------------------------------------- |
| **K-Nearest Neighbors (KNN)**    | Classifies based on K closest training points         |
| **Support Vector Machine (SVM)** | Maximizes the margin between classes using hinge loss |

---

### Probabilistic

| Model           | Description                                                         |
| --------------- | ------------------------------------------------------------------- |
| **Naive Bayes** | Uses Bayes' Theorem with Gaussian likelihoods and log probabilities |


---

### Ensemble Methods

| Model        | Description                                                 |
| ------------ | ----------------------------------------------------------- |
| **Bagging**  | Trains multiple models independently and averages results   |
| **Boosting** | Trains models sequentially, focusing on mistakes (AdaBoost) |


---

## Why This Project Matters

* **Interview Prep**: These implementations help you explain core ML logic during technical interviews
* **No Black Boxes**: Learn exactly how algorithms work, line by line
* **Hands-On Learning**: Apply math concepts to real code
* **Modular Design**: Easy to extend to real-world datasets

---

## Suggested Exercises
* Turn binary classifiers into multiclass
* Use real datasets like Iris or Titanic
* Visualize decision boundaries
* Add metrics like Precision, Recall, and F1

---

## Contribute
If you find a bug, want to refactor, or add new models (e.g., Gradient Boosting, Perceptron), feel free to open a PR or issue.

> Let’s make machine learning accessible for everyone.

---


## License
This project is licensed under the MIT License.
