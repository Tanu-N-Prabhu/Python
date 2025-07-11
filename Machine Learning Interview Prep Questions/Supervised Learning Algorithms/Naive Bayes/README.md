# Naive Bayes from Scratch (No Class, No Libraries)

This notebook shows how to build a **Gaussian Naive Bayes classifier** using only **NumPy and basic functions**, no classes, no libraries, and no machine learning frameworks.

Perfect for students preparing for interviews or anyone who wants to understand how Naive Bayes works under the hood.

---

## What You’ll Learn

- What Naive Bayes is and how it applies Bayes’ Theorem
- How to handle **continuous features** using the Gaussian probability density function
- How to compute:
  - **Class priors**
  - **Feature means and variances**
  - **Log-likelihoods and predictions**
- How to write Naive Bayes using **just functions and NumPy**

---

## Files Included

| File                             | Description                                              |
|----------------------------------|----------------------------------------------------------|
| `naive_bayes_from_scratch.ipynb` | Full notebook: train + test Naive Bayes with no classes |
| `README.md`                      | This file shows how to use and learn from the notebook       |

---

## How to Use

1. Clone or download this repository.
2. Open `naive_bayes_from_scratch.ipynb` in Jupyter Notebook or Google Colab.
3. Run the cells to:
   - Load the sample data
   - Calculate priors, means, and variances
   - Implement prediction using basic math
   - Test the model on new inputs

---

## Requirements

- Python 3.x
- NumPy
- Jupyter Notebook or Google Colab

Install NumPy if you don’t already have it:

```bash
pip install numpy
```

---

## Why This Helps in Interviews
* Shows you understand Bayesian reasoning
* Helps you explain probabilistic classifiers
* No reliance on libraries like scikit-learn
* Shows you can build ML models from scratch

---

## Extensions and Challenges
* Extend to multi-class classification (3 or more classes)
* Add Laplace smoothing for discrete feature datasets
* Try applying this logic to a real dataset like Iris
* Create a version using Python `class` (OOP)

---

## License
This project is licensed under the MIT License.

---

## Contributions
Pull requests are welcome! If you have a cleaner implementation or want to extend this for more datasets, feel free to contribute.

