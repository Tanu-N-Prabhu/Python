# K-Means Clustering from Scratch (No Classes, No ML Libraries)

This notebook demonstrates how to implement the **K-Means Clustering algorithm** from scratch using only **NumPy**, no machine learning libraries, and no object-oriented programming. It’s written to help beginners clearly understand each step of the algorithm.

---

## What You'll Learn

- What K-Means Clustering is and how it works
- The difference between supervised and unsupervised learning
- How to:
  - Initialize random centroids
  - Assign each point to its closest centroid
  - Recalculate centroids based on clusters
  - Repeat until convergence
- Visualize clusters and final centroids using Matplotlib

---

## What is K-Means?

K-Means is an **unsupervised learning algorithm** used to group similar data points into clusters. Unlike supervised models, it does **not require labeled data**.

### Algorithm Steps:
1. Choose `k` random centroids
2. Assign points to the **nearest** centroid
3. Recompute each centroid as the **mean** of its cluster
4. Repeat until centroids stop changing (or max iterations reached)

---

## Files Included

| File                        | Description                                               |
|-----------------------------|-----------------------------------------------------------|
| `kmeans_from_scratch.ipynb` | Full implementation of K-Means with visualizations       |
| `README.md`                 | This file explains the project and how to run it       |

---

## How to Use

1. Clone or download this repository
2. Open `kmeans_from_scratch.ipynb` in **Jupyter Notebook** or **Google Colab**
3. Run each cell to:
   - Generate sample 2D data
   - Initialize centroids
   - Perform clustering
   - Visualize final results

---

## Requirements

This notebook uses only:

- Python 3.x
- NumPy
- Matplotlib

Install dependencies:

```bash
pip install numpy matplotlib
```

---

## Example Use-Cases
* Customer segmentation in marketing
* Document clustering
* Image compression
* Anomaly detection (indirectly)

---

## Why Learn K-Means?
* Common in real-world applications
* Frequently asked in interviews
* Builds foundation for more complex clustering methods (e.g., GMM, DBSCAN)

---

## Suggested Challenges
* Test with different `k` values
* Add stopping criteria based on minimal centroid change
* Compare with `sklearn.cluster.KMeans` for validation
* Try clustering on real datasets (e.g., Iris, MNIST)

---

## License
This project is licensed under the MIT License.

---

## Contribute
Feel free to fork, edit, and contribute new ideas — whether it's new clustering methods, real datasets, or optimization tweaks!
