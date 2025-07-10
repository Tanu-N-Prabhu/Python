# Supervised Learning Interview Questions

Supervised learning uses labeled data to train models that make predictions. Below are common algorithms, interview questions, and mini case studies to understand how they work in the real world.

---

## 1. Linear Regression

### Key Concepts:
- Predicts continuous values based on linear relationships between features.
- Uses least squares to minimize error between predicted and actual values.

### Interview Questions:
- What is the cost function used in Linear Regression?
- How do you interpret the coefficients?
- What are the assumptions of Linear Regression?

### Mini Case Study:
**Problem:** Predict house prices based on features like square footage, number of bedrooms, and location.  
**Model:** A linear regression model can be trained on historical housing data to estimate price as a continuous variable.

---

## 2. Logistic Regression

### Key Concepts:
- Used for binary classification problems.
- Outputs probabilities using the sigmoid function.

### Interview Questions:
- How is Logistic Regression different from Linear Regression?
- What’s the role of the sigmoid function?

### Mini Case Study:
**Problem:** Classify whether a given email is spam or not.  
**Model:** Logistic regression assigns a probability to the email being spam based on features like keyword frequency and sender reputation.

---

## 3. Decision Trees

### Key Concepts:
- Non-parametric models that split data based on feature thresholds.
- Easy to visualize and interpret.

### Interview Questions:
- How does a decision tree decide which feature to split on?
- What is entropy or Gini impurity?

### Mini Case Study:
**Problem:** Approve or reject a bank loan application.  
**Model:** A decision tree learns rules based on income, credit score, and employment status to classify applicants.

---

## 4. Random Forest

### Key Concepts:
- Ensemble method using multiple decision trees (bagging).
- Reduces overfitting and improves accuracy.

### Interview Questions:
- How does Random Forest improve over Decision Trees?
- What is bagging?

### Mini Case Study:
**Problem:** Predict customer churn in a telecom company.  
**Model:** A random forest model combines trees trained on different subsets of customers to predict churn with high accuracy.

---

## 5. Support Vector Machine (SVM)

### Key Concepts:
- Finds the optimal hyperplane that maximally separates classes.
- Uses kernel tricks for non-linear classification.

### Interview Questions:
- What is the margin in SVM?
- How do kernels work?

### Mini Case Study:
**Problem:** Classify handwritten digits (e.g., MNIST dataset).  
**Model:** An SVM with an RBF kernel can learn to distinguish between 0–9 digits based on pixel intensity values.

---

## 6. K-Nearest Neighbors (KNN)

### Key Concepts:
- Instance-based learning.
- Classifies a new point based on the majority class of its k-nearest neighbors.

### Interview Questions:
- How do you choose the value of K?
- What are the downsides of KNN?

### Mini Case Study:
**Problem:** Recommend a movie based on user preferences.  
**Model:** KNN finds similar users and recommends movies liked by those with similar taste.

---

## 7. Naive Bayes

### Key Concepts:
- Probabilistic classifier based on Bayes’ theorem.
- Assumes features are conditionally independent.

### Interview Questions:
- Why is it called “naive”?
- When does Naive Bayes perform well?

### Mini Case Study:
**Problem:** Classify customer reviews as positive or negative.  
**Model:** Naive Bayes uses word frequencies to assign sentiment labels efficiently, especially useful in large text datasets.

---

## Quick Comparison Table

| Algorithm         | Type         | Strengths                          | Weaknesses                     |
|------------------|--------------|------------------------------------|--------------------------------|
| Linear Regression | Regression   | Simple, interpretable              | Assumes linearity              |
| Logistic Regression | Classification | Probabilistic output              | Struggles with non-linear data |
| Decision Tree     | Both         | Easy to interpret, fast            | Prone to overfitting           |
| Random Forest     | Both         | Robust, handles non-linearity      | Slower, less interpretable     |
| SVM               | Classification | Works in high-dimensions          | Hard to tune, less scalable    |
| KNN               | Both         | No training phase                  | Slow at prediction time        |
| Naive Bayes       | Classification | Fast, works well with text        | Assumes independence           |

---

> **Next Steps:**  
Proceed to [`unsupervised_learning.md`](./unsupervised_learning.md) to explore clustering and dimensionality reduction techniques.
