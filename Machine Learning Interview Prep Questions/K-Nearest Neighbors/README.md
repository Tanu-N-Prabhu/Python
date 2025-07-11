# K-Nearest Neighbors (KNN) from Scratch (No Libraries)

This notebook provides a step-by-step implementation of the **K-Nearest Neighbors (KNN)** algorithm using **NumPy only**, no `scikit-learn` or machine learning libraries.

KNN is one of the simplest and most intuitive ML algorithms. It’s perfect for beginners to learn classification logic and **distance-based learning**.

---

## What You’ll Learn

- What K-Nearest Neighbors is and how it works  
- How to compute **Euclidean distance** between points  
- How to implement the **majority vote** prediction  
- How to visualize classification and test points  
- Why KNN is called a **lazy learning** algorithm

---

## Files Included

| File | Description |
|------|-------------|
| `knn_from_scratch.ipynb` | Full implementation of KNN using NumPy, tested on a small 2D dataset |
| `README.md` | This file — explains the notebook and usage instructions |

---

## How to Use

1. Clone or download this repository.
2. Open `knn_from_scratch.ipynb` in Jupyter Notebook or Google Colab.
3. Run the cells to:
   - Load a simple dataset
   - Write your own `euclidean_distance` function
   - Implement `knn_predict()` from scratch
   - Classify new test points
   - Visualize the predictions

---

## Requirements

- Python 3.x
- NumPy
- Matplotlib
- Jupyter Notebook or Google Colab

Install dependencies if needed:

```bash
pip install numpy matplotlib
```

---

## Why It’s Great for Interviews
Understanding KNN helps with:
  * Explaining distance-based algorithms
  * Building a mental model for nearest-neighbor logic
  * Discussing trade-offs in model complexity vs simplicity
  * Writing simple models without relying on libraries

---

## Suggested Extensions
* Try different values of K
* Add support for weighted voting
* Use other distance metrics (e.g., Manhattan)
* Extend to multi-class datasets
* Add accuracy evaluation on test data

---

## License
This project is open source under the MIT License.

---

## Contributions
Contributions, bug fixes, and suggestions are welcome! Help others learn machine learning from the ground up.
