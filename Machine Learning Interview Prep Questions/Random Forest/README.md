# Random Forest from Scratch (No Libraries)

This notebook walks you through building a **Random Forest Classifier** step by step using only **NumPy** — no scikit-learn, no black boxes.

It’s designed for students preparing for interviews and anyone who wants to understand how Random Forests work internally.

---

## What You’ll Learn

- What Random Forest is and why it works
- How to build a decision tree from scratch using Gini Impurity
- How to perform **bootstrap sampling**
- How to build an ensemble of trees (the forest)
- How to make predictions using **majority voting**
- How to test and interpret the model’s behavior

---

## Files Included

| File | Description |
|------|-------------|
| `random_forest_from_scratch.ipynb` | Complete implementation of a Random Forest classifier using NumPy |
| `README.md` | This file — explains what’s inside and how to use the notebook |

---

## How to Use

1. Clone or download this repo.
2. Open `random_forest_from_scratch.ipynb` in Jupyter Notebook or Google Colab.
3. Run the notebook step-by-step to:
   - Understand decision trees
   - Build a forest using bootstrap samples
   - Predict using majority voting
   - Test the model on new examples

---

## Requirements

- Python 3.x
- NumPy
- Matplotlib (optional, for visualizing data)
- Jupyter Notebook or Google Colab

Install dependencies:

```bash
pip install numpy matplotlib
```

---

## Why It’s Great for Interviews
* Most students can use `sklearn`, but few understand what’s happening inside.
* By writing Random Forest from scratch, you’ll:
    * Build strong fundamentals
    * Explain every part of the algorithm
    * Stand out in coding interviews and ML system design questions


---

## Suggested Extensions
* Handle multiple features (we use 1D data here for clarity)
* Add randomness in feature selection (extra credit!)
* Visualize the trees or forest structure
* Support regression instead of classification
  
---

## License
This project is open source under the MIT License. Use it freely for learning or teaching.

---

## Contributions
Pull requests to extend or improve this notebook are welcome. Let’s help students learn ML hands-on!
