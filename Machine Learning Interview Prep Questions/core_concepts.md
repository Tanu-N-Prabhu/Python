# Core Machine Learning Concepts

This section covers the foundational topics that every machine learning learner and interview candidate should understand. These are commonly asked in both technical interviews and screening rounds.

---

## 1. What is Machine Learning?

Machine Learning (ML) is a field of computer science that gives computers the ability to learn from data and improve their performance on a task without being explicitly programmed.

---

## 2. Types of Machine Learning

| Type | Description | Examples |
|------|-------------|----------|
| **Supervised Learning** | Learns from labeled data | Classification, Regression |
| **Unsupervised Learning** | Learns from unlabeled data | Clustering, Dimensionality Reduction |
| **Semi-Supervised Learning** | Learns from a mix of labeled and unlabeled data | Image Classification with few labeled samples |
| **Reinforcement Learning** | Learns by interacting with an environment and receiving feedback (rewards) | Game-playing agents, Robotics |

---

## 3. Difference Between AI, ML, and Deep Learning

- **Artificial Intelligence (AI):** Broad field aiming to create systems that simulate human intelligence.
- **Machine Learning (ML):** Subset of AI focused on learning from data.
- **Deep Learning (DL):** Subset of ML using multi-layered neural networks.

---

## 4. What is Overfitting and Underfitting?

- **Overfitting:** The model learns the training data too well (including noise), leading to poor generalization.
- **Underfitting:** The model is too simple to capture the patterns in the data.

| Type | Characteristics | Fixes |
|------|------------------|-------|
| Overfitting | High training accuracy, low test accuracy | Regularization, more data, simpler model |
| Underfitting | Low training and test accuracy | More complex model, better features |

---

## 5. Bias-Variance Tradeoff

- **Bias:** Error from wrong assumptions (e.g., underfitting).
- **Variance:** Error from sensitivity to small fluctuations in training data (e.g., overfitting).

A good model strikes a balance between bias and variance.

---

## 6. What is the Curse of Dimensionality?

As the number of features increases, the volume of the feature space grows exponentially. This makes it hard for models to generalize due to sparse data points in high-dimensional space.

**Fixes:**
- Feature selection
- Dimensionality reduction (e.g., PCA)

---

## 7. Parametric vs Non-Parametric Models

| Type | Description | Example |
|------|-------------|---------|
| **Parametric** | Assumes a fixed number of parameters | Linear Regression |
| **Non-Parametric** | No fixed number of parameters; more flexible | K-NN, Decision Trees |

---

## 8. What is a Feature?

A feature is an individual measurable property or characteristic of a phenomenon being observed. In ML, features are the input variables used to make predictions.

---

## 9. What is a Label?

A label is the target variable — the output you're trying to predict (e.g., in classification, it could be "spam" or "not spam").

---

## 10. What is the difference between Classification and Regression?

| Task | Output | Example |
|------|--------|---------|
| **Classification** | Discrete categories | Predict if an email is spam |
| **Regression** | Continuous value | Predict house prices |

---

**Next Steps:**  
Proceed to [`supervised_learning.md`](./supervised_learning.md) for questions on specific ML algorithms like Linear Regression, Decision Trees, and more.
