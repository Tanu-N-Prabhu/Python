# Ensemble Learning from Scratch (No Libraries)

This notebook walks you through the fundamentals of **Ensemble Learning**, with working code examples for **Bagging (Random Forest idea)** and **Boosting (AdaBoost)**, all implemented using simple NumPy operations.

---

## What You’ll Learn

- What ensemble learning is and why it works
- Key ensemble types:
  - Bagging
  - Boosting
  - Stacking (concept only)
- How to implement:
  - **Random Forest logic** using multiple decision stumps
  - **AdaBoost** from scratch using weighted sampling and stump training
- How ensemble methods reduce bias, variance, and improve accuracy

---

## Files Included

| File                             | Description                                                |
|----------------------------------|------------------------------------------------------------|
| `ensemble_learning_from_scratch.ipynb` | Main notebook showing Bagging and Boosting from scratch |
| `README.md`                      | This file explains purpose, usage, and learning goals   |

---

## How to Use

1. Clone or download this repository.
2. Open `ensemble_learning_from_scratch.ipynb` in Jupyter Notebook or Google Colab.
3. Run the notebook cells in order to:
   - Load and visualize synthetic binary data
   - Simulate a Random Forest with random decision thresholds
   - Build AdaBoost step by step with log-based weight updates
   - Compare the accuracy of ensemble models

---

## Requirements

- Python 3.x
- NumPy
- Matplotlib
- Jupyter Notebook or Google Colab

To install dependencies:

```bash
pip install numpy matplotlib
```

---

## Why It’s Great for Interviews
* Ensemble methods are widely used in production ML (e.g., XGBoost, Random Forests)
* Interviewers often ask about the differences between bagging and boosting
* Knowing how these work under the hood helps you:
    * Talk about bias–variance tradeoffs
    * Explain model robustness
    * Understand decision trees better
 

---

## Suggested Extensions
* Replace stumps with actual decision trees (e.g., using `sklearn.tree.DecisionTreeClassifier`)
* Add stacking (combine predictions from both models)
* Tune the number of rounds, thresholds, and learning rates
* Add visualizations of decision boundaries

---

## License
This project is open source under the MIT License.

---

## Contributions
Pull requests and improvements are welcome! Feel free to adapt this notebook for multiclass datasets or real-world examples
  
