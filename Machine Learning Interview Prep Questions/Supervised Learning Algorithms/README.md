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

| File / Folder                          | Description |
|----------------------------------------|-------------|
| `linear_regression_from_scratch.ipynb` | Predicting continuous outputs using Least Squares |
| `logistic_regression_from_scratch.ipynb` | Binary classification using Sigmoid & Gradient Descent |
| `decision_tree_from_scratch.ipynb`     | Simple if-else tree built using Gini Index |
| `random_forest_from_scratch.ipynb`     | Ensemble of trees using bagging |
| `svm_from_scratch.ipynb`               | Linear Support Vector Machine using Hinge Loss |
| `knn_from_scratch.ipynb`               | Classifying based on nearest neighbors |
| `naive_bayes_from_scratch.ipynb`       | Probabilistic classification using Bayes' theorem |
| `ensemble_learning_from_scratch.ipynb` | Bagging (Random Forest idea) and Boosting (AdaBoost) |
| `README.md`                            | This file is the main overview of all models |

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
