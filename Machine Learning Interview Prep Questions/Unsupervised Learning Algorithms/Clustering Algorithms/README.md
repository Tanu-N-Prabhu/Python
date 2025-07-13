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
| [K-Means Clustering](https://github.com/Tanu-N-Prabhu/Python/tree/master/Machine%20Learning%20Interview%20Prep%20Questions/Unsupervised%20Learning%20Algorithms/Clustering%20Algorithms/K-Means%20Clustering)         | Partitions data into `k` clusters by minimizing intra-cluster variance               | Customer segmentation, Market clustering       |
| [DBSCAN Clustering](https://github.com/Tanu-N-Prabhu/Python/tree/master/Machine%20Learning%20Interview%20Prep%20Questions/Unsupervised%20Learning%20Algorithms/Clustering%20Algorithms/DBSCAN%20Clustering)         | Groups points based on density, detects outliers automatically                        | Anomaly detection, GPS-based grouping          |
| [Hierarchical Clustering](https://github.com/Tanu-N-Prabhu/Python/tree/master/Machine%20Learning%20Interview%20Prep%20Questions/Unsupervised%20Learning%20Algorithms/Clustering%20Algorithms/Hierarchical%20Clustering) | Builds a tree of clusters using a bottom-up (agglomerative) approach                  | Dendrogram visualization, small datasets       |
| [Mean Shift Clustering]([./mean_shift_from_scratch.ipynb](https://github.com/Tanu-N-Prabhu/Python/tree/master/Machine%20Learning%20Interview%20Prep%20Questions/Unsupervised%20Learning%20Algorithms/Clustering%20Algorithms/Mean%20Shift%20Clustering)) | Shifts each point toward areas of higher density, finds the number of clusters automatically | Image segmentation, Mode-seeking clustering    |
| [Gaussian Mixture Model](https://github.com/Tanu-N-Prabhu/Python/tree/master/Machine%20Learning%20Interview%20Prep%20Questions/Unsupervised%20Learning%20Algorithms/Clustering%20Algorithms/Gaussian%20Mixture%20Model)               | Uses probabilistic clustering via Gaussian Mixtures with Expectation-Maximization (EM) | Soft clustering, Voice/signal segmentation     |

---

## What is Clustering?

Clustering is a type of **unsupervised learning** where the goal is to group similar data points based on inherent patterns, **without using labels**.

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

> No machine learning libraries (like scikit-learn) are required; everything is built from the ground up.

---

##  Suggested Use
* Technical interview preparation
* ML algorithm deep-dives
* Teaching or tutoring ML fundamentals
* Experimenting on toy datasets

---

## Recommended Order to Learn
If you're just getting started, we suggest the following progression:

* **K-Means** - a foundational clustering algorithm
* **DBSCAN** - introduces density + noise detection
* **Hierarchical** - visualizes cluster structure (dendrogram)
* **Mean Shift** - auto-detects clusters via density peaks
* **GMM** - probabilistic view using distributions and the EM algorithm

---

## License
All content is licensed under the MIT License. Use it freely for learning or teaching.

---

## Contribute

Pull requests are welcome; you can:
   * Add kernel visualizations
   * Create animations of convergence
   * Port the notebooks to interactive dashboards

