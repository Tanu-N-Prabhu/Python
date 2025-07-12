# Hierarchical Clustering from Scratch (Agglomerative)

This notebook contains a simple and fully documented implementation of **Agglomerative Hierarchical Clustering** using only **NumPy**. It's designed to help students understand how hierarchical clustering works, without any machine learning libraries or classes.

---

## What You’ll Learn

- What hierarchical clustering is and when to use it
- The difference between agglomerative and divisive clustering
- How to:
  - Start with each point as its cluster
  - Merge the closest clusters using **single linkage**
  - Visualize final cluster groups

---

## What is Hierarchical Clustering?

Hierarchical clustering is a method of **unsupervised learning** that builds a tree-like structure of nested clusters (called a **dendrogram**).

We implement the **agglomerative (bottom-up)** approach:

1. Start with each point as a cluster.
2. At each step, merge the two **closest clusters**.
3. Repeat until the desired number of clusters is reached.

### Linkage Methods (Distance Between Clusters):
- **Single Linkage** – Minimum distance between any two points
- Complete Linkage, Average Linkage (not covered here)

---

## Files Included

| File                                   | Description                                      |
|----------------------------------------|--------------------------------------------------|
| `hierarchical_clustering_from_scratch.ipynb` | Full implementation and visualization           |
| `README.md`                            | This file explains the notebook          |

---

## How to Use

1. Clone or download this repository
2. Open `hierarchical_clustering_from_scratch.ipynb` in:
   - Jupyter Notebook, OR
   - Google Colab
3. Run each cell to:
   - Generate a 2D dataset
   - Implement agglomerative clustering step-by-step
   - Plot final grouped clusters

---

## Requirements

This notebook uses:

- Python 3.x
- NumPy
- Matplotlib

To install required packages:

```bash
pip install numpy matplotlib
```

---

## When to Use Hierarchical Clustering
* You don’t know how many clusters to expect
* You want a visual hierarchy of cluster relationships
* Your data may not be well-separated in shape or size

---

## Suggested Extensions
* Visualize a dendrogram using `scipy.cluster.hierarchy`
* Add support for complete or average linkage
* Apply the algorithm to real-world datasets (e.g., gene expression, social networks)

---

## License
This project is open-source and available under the MIT License.

---


## Contribute
* Feel free to fork and improve! You can:
    * Add distance metrics
    * Introduce divisive clustering
    * Add dendrogram tree visualizations
