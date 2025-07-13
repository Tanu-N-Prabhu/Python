# t-SNE (t-distributed Stochastic Neighbor Embedding) from Scratch

This notebook provides a simplified, from-scratch implementation of **t-SNE** using only **NumPy**. It’s designed to help students and beginners understand the intuition behind t-SNE without diving into heavy math or library abstractions.

---

## What You'll Learn

- What t-SNE is and why it’s used
- The difference between **high-dimensional** and **low-dimensional** similarity distributions
- How to compute **pairwise affinities** using:
  - Gaussian kernel (high-dimensional space)
  - t-distribution kernel (low-dimensional space)
- How to implement a simplified **KL divergence minimization loop**
- How to visualize high-dimensional data in 2D

---

## What is t-SNE?

**t-SNE** is a powerful **non-linear dimensionality reduction** technique used primarily for **visualizing high-dimensional data** (like word embeddings, images, or gene expression data).

### Core Idea:
t-SNE tries to preserve local neighborhoods by converting point distances into **probabilities** and matching those probabilities between high and low dimensions.

- In high-D: Similar points have **high probability** of being neighbors.
- In low-D: We arrange points so that these probabilities are preserved as much as possible.

---

## Files Included

| File                          | Description                                                |
|-------------------------------|------------------------------------------------------------|
| `tsne_from_scratch.ipynb`     | Simplified implementation with visualizations              |
| `README.md`                   | This file explains the concept and how to use the notebook |

---

## How to Use

1. Clone or download the repository
2. Open `tsne_from_scratch.ipynb` in:
   - Jupyter Notebook
   - Google Colab
3. Run each cell to:
   - Generate synthetic high-D data
   - Apply simplified t-SNE
   - Visualize 2D embeddings

---

## Requirements

```bash
pip install numpy matplotlib scipy scikit-learn
```
> Note: We use `scipy.spatial.distance` for computing pairwise distances and `make_blobs` from `sklearn.datasets` to generate high-dimensional test data.
---


## Key Simplifications
* To keep things educational and readable:
* No heavy optimization or momentum tricks
* Basic NumPy loops for gradient updates
* No multicore or Barnes-Hut acceleration
* Ideal for teaching and interview prep

---

## Suggested Experiments
* Change the number of dimensions in input (e.g., 10D, 100D)
* Vary `sigma` to control Gaussian bandwidth
* Adjust `learning_rate` and `iterations`
* Apply to real-world datasets (e.g., Iris, MNIST)

---

## License
This project is open-source and available under the MIT License.

---

##  Contribute
* Want to help improve it?
  * Add full t-SNE with gradient descent
  * Compare with PCA or UMAP
  * Create 3D visualizations
> Pull requests are welcome!
