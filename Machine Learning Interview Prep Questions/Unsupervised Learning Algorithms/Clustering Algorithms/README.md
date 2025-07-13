# Clustering Algorithms (Unsupervised Learning)

This section contains clean, step-by-step implementations of **clustering algorithms** using only **NumPy** (no scikit-learn), crafted for learning, interview preparation, and deep conceptual understanding.

Each notebook is:
- **Class-free** (for clarity and readability)
- **Heavily commented** with math and intuition
- **Hands-on**, with visualizations and real examples

---

## Included Algorithms

| Algorithm                 | Description                                                                 | Best Use-Cases                                 |
|:--------------------------|:-----------------------------------------------------------------------------|:------------------------------------------------|
| [`kmeans_from_scratch.ipynb`](./kmeans_from_scratch.ipynb)         | Partitions data into `k` clusters by minimizing intra-cluster variance               | Customer segmentation, Market clustering       |
| [`dbscan_from_scratch.ipynb`](./dbscan_from_scratch.ipynb)         | Groups points based on density, detects outliers automatically                        | Anomaly detection, GPS-based grouping          |
| [`hierarchical_clustering_from_scratch.ipynb`](./hierarchical_clustering_from_scratch.ipynb) | Builds a tree of clusters using a bottom-up (agglomerative) approach                  | Dendrogram visualization, small datasets       |
| [`mean_shift_from_scratch.ipynb`](./mean_shift_from_scratch.ipynb) | Shifts each point toward areas of higher density — finds number of clusters automatically | Image segmentation, Mode-seeking clustering    |
| [`gmm_from_scratch.ipynb`](./gmm_from_scratch.ipynb)               | Uses probabilistic clustering via Gaussian Mixtures with Expectation-Maximization (EM) | Soft clustering, Voice/signal segmentation     |

---

## What is Clustering?

Clustering is a type of **unsupervised learning** where the goal is to group similar data points together based on inherent patterns — **without using labels**.

Each algorithm has a unique approach:
- **K-Means**: Hard partitioning into `k` fixed clusters
- **DBSCAN**: Density-based, automatically finds clusters + noise
- **Hierarchical**: Builds a cluster tree (dendrogram) you can "cut"
- **Mean Shift**: Finds modes of high-density and auto-detects clusters
- **GMM**: Models data as a combination of Gaussian distributions (soft clustering)

---

## How to Use

1. Clone this repository
2. Navigate to the `clustering/` directory
3. Open any notebook in:
   - Jupyter Notebook
   - Google Colab
4. Run all cells to:
   - Understand the concept
   - Implement from scratch
   - Visualize results and clusters

---

## Requirements

```bash
pip install numpy matplotlib
```

