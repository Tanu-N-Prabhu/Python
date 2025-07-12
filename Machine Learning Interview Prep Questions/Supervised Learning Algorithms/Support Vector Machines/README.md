# Support Vector Machine (SVM) from Scratch (No Libraries)

This notebook demonstrates how to implement a **Linear Support Vector Machine (SVM)** from scratch using only **NumPy**.

It’s designed for students and beginners who want to build ML intuition and prepare for interviews by understanding how SVMs really work under the hood.

---

## What You’ll Learn

- What an SVM is and how it finds a decision boundary  
- How the **hinge loss** works  
- How to apply **gradient descent** to train a linear SVM  
- How to visualize the **margin** and decision boundary  
- How to write your own `predict()` function for inference

---

## Files Included

| File | Description |
|------|-------------|
| `svm_from_scratch.ipynb` | Full implementation of a binary SVM classifier using hinge loss and gradient descent |
| `README.md` | This file, explaining what’s in the notebook and how to use it |

---

## How to Use

1. Clone or download this repository.
2. Open `svm_from_scratch.ipynb` in Jupyter Notebook or Google Colab.
3. Follow the cells step by step to:
   - Generate binary classification data
   - Initialize weights and bias
   - Train using the hinge loss + gradient descent
   - Visualize the separating hyperplane and margins
   - Evaluate predictions and accuracy

---

## Requirements

- Python 3.x
- NumPy
- Matplotlib
- Jupyter Notebook or Google Colab

Install via pip:

```bash
pip install numpy matplotlib
```

---

## Why It’s Useful for Interviews
Writing SVM from scratch helps you:

  * Understand max-margin classifiers
  * Talk confidently about hinge loss and decision boundaries
  * Impress interviewers by going beyond scikit-learn

---

## Suggested Practice Extensions
* Add regularization parameter tuning
* Add support for mini-batch or stochastic gradient descent
* Implement multiclass classification (e.g., one-vs-rest strategy)
* Try different initializations and learning rates

---

## License
This project is released under the MIT License.

---

## Contributions
Feel free to fork this notebook, improve the training logic, or add visualizations. Let’s help more students understand machine learning by building it from the ground up!
