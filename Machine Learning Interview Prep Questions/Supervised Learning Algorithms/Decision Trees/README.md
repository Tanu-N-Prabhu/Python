# Decision Tree from Scratch (No Libraries)

This notebook demonstrates how to implement a simple **Decision Tree Classifier** from scratch using only **NumPy**.

It’s designed for beginners and students to understand the fundamentals of how decision trees work, without using libraries like `scikit-learn`.

---

## What You’ll Learn

- What a decision tree is and how it splits data
- How to calculate **Gini Impurity**
- How to select the **best split** at each node
- How to recursively build a tree
- How to make predictions using the trained tree
- How to implement all logic using **pure Python and NumPy**

---

##  Files Included

| File | Description |
|------|-------------|
| `decision_tree_from_scratch.ipynb` | Main notebook implementing a binary decision tree using Gini Impurity |
| `README.md` | Explanation of the notebook and how to use it |

---

## How to Use

1. Clone or download this repository.
2. Open `decision_tree_from_scratch.ipynb` in Jupyter Notebook or Google Colab.
3. Run the notebook step by step to:
   - Load and visualize simple binary data
   - Calculate gini impurity
   - Split and train a basic decision tree
   - Predict outputs for new samples

---

## Why This Matters for Interviews

Understanding how decision trees work internally will:

- Boost your ML intuition  
- Help you answer interview questions about model interpretability  
- Make it easier to debug or explain black-box ML models  
- Impress interviewers with hands-on algorithm knowledge

---

## Requirements

- Python 3.x
- NumPy
- Matplotlib (for visualizing data)
- Jupyter Notebook or Google Colab

Install via pip if needed:

```bash
pip install numpy matplotlib
```

---

## Future Extensions (Challenge Ideas)
* Add support for multiple features (we use only 1D here)
* Add tree pruning
* Implement entropy instead of Gini
* Visualize the full tree structure

---

## License
This project is licensed under the MIT License — free to use and modify.

---


## Contributions
Feel free to fork, improve, or suggest additions to this notebook. Let’s help more students learn ML the hands-on way!

