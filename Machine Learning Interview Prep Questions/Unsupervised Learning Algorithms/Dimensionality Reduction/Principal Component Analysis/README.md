# Principal Component Analysis (PCA) from Scratch (No ML Libraries, No Classes)

This notebook provides a simple, step-by-step implementation of **Principal Component Analysis (PCA)** using only **NumPy**. It’s designed for learners who want to understand PCA deeply and implement it without relying on libraries like `scikit-learn`.

---

## What You’ll Learn

- The mathematical intuition behind PCA
- How to find **principal components** using eigenvalues and eigenvectors
- How PCA is used for **dimensionality reduction**
- How to implement PCA from scratch using NumPy
- How to visualize reduced data in lower dimensions (e.g., 1D)

---

## What is PCA?

**Principal Component Analysis (PCA)** is an unsupervised learning algorithm used for:

- Dimensionality Reduction 
- Noise Filtering 
- Data Compression 
- Visualization of high-dimensional data 

### How It Works:
1. **Center the data** (subtract the mean)
2. **Calculate the covariance matrix**
3. **Find eigenvectors & eigenvalues**
4. **Sort eigenvectors by eigenvalues**
5. **Project data onto top `k` eigenvectors**

PCA finds directions (called **principal components**) that capture the **most variance** in your dataset.

---

## Files Included

| File                    | Description                                        |
|-------------------------|----------------------------------------------------|
| `pca_from_scratch.ipynb` | Full PCA implementation with 1D/2D visualizations |
| `README.md`             | This file explains usage and concepts            |

---

## How to Use

1. Clone or download this repository
2. Open `pca_from_scratch.ipynb` in:
   - Jupyter Notebook, OR
   - Google Colab
3. Run each cell to:
   - Center and visualize data
   - Calculate principal components
   - Reduce data to lower dimensions (e.g., 1D or 2D)
   - Plot projections and components

---

## Requirements

```bash
pip install numpy matplotlib
```

> No machine learning libraries are used.

---

## Why Learn PCA?
* Common topic in interviews (concept + implementation)
* Used in:
  * Exploratory data analysis (EDA)
  * Preprocessing before training models
  * Reducing overfitting in high-dimensional datasets
* Makes large datasets easier to understand and visualize

---

## Suggested Experiments
* Reduce to 2D and visualize with labels (for classification)
* Compare variance retained for different `k` components
* Apply to real-world datasets (e.g., MNIST, Iris)
* Chain PCA with K-Means or GMM for better clustering

---

## License
This project is open-source and available under the MIT License.

---

## Contribute
* Want to improve this?
  * Add interactive sliders for choosing components
  * Extend to 3D visualizations
  * Include real-world datasets

> Pull requests welcome!
