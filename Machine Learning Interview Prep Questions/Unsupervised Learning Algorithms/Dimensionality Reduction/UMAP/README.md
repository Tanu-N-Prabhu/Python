# UMAP (Uniform Manifold Approximation and Projection) from Scratch

This notebook contains a simplified, from-scratch implementation of **UMAP** using only **NumPy**. It’s designed for students and learners who want to understand the core concepts behind UMAP without the complexity of full library implementations like `umap-learn`.

---

## What You'll Learn

- What UMAP is and why it's used in ML workflows
- How to preserve both **local** and **global** structure in data
- How to build a **k-nearest neighbor graph**
- How to optimize low-dimensional embeddings using distance-based updates
- Differences between UMAP and t-SNE

---

## What is UMAP?

**UMAP** is a fast, scalable, and flexible algorithm used for:
- Visualizing high-dimensional data (e.g., word embeddings, gene data, image vectors)
- Dimensionality reduction before clustering or classification
- Preserving both **local relationships** and **global structure**

UMAP builds a **neighborhood graph** from high-dimensional data, then optimizes a 2D/3D representation that maintains similar relationships.

---

## Comparison: t-SNE vs UMAP

| Metric              | t-SNE                  | UMAP                   |
|:---------------------|:------------------------|:------------------------|
| Local Structure      | Preserved well       | Preserved well      |
| Global Structure     | Often distorted        | Preserved better      |
| Speed                | Slower               | Faster                |
| Interpretation       | Probabilistic           | Graph-theoretic         |

---

## Files Included

| File                      | Description                                             |
|:---------------------------|:---------------------------------------------------------|
| `umap_from_scratch.ipynb` | Full UMAP implementation with NumPy and visualization  |
| `README.md`               | This file explains concepts and how to run the notebook |

---

## How to Use

1. Clone or download this repository
2. Open `umap_from_scratch.ipynb` in:
   - Jupyter Notebook **or**
   - Google Colab
3. Run all cells to:
   - Generate high-dimensional data
   - Build a k-nearest neighbor graph
   - Reduce dimensions using UMAP logic
   - Visualize embeddings in 2D

---

## Requirements

```bash
pip install numpy matplotlib scipy scikit-learn
```
This implementation uses:
* **NumPy** - for matrix ops
* **SciPy** - for distance matrix
* **Matplotlib** - for plotting
* **scikit-learn** - only for data generation (make_blobs)

---

## Key Concepts in This Notebook
* k-NN Graph: Captures neighborhood structure
* Distance Preservation: Optimizes low-dimensional points
* Symmetric Updates: Ensures structure in both directions
* No Classes: Procedural code for easy understanding

---

## Suggested Experiments
* Change `k` (number of neighbors) and observe results
* Vary number of clusters or dimensions in input data
* Visualize using 3D plots
* Compare output to t  -SNE or PCA

---

## License
This notebook is licensed under the MIT License. Use it freely for learning, teaching, or adapting.

---


## Contribute
* Want to improve this notebook?
    * Add real datasets (e.g., Iris, MNIST)
    * Implement fuzzy set construction
    * Optimize with gradient descent
> Pull requests welcome!
