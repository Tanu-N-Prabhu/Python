# DBSCAN Clustering from Scratch (No ML Libraries, No Classes)

This notebook walks you through a simple implementation of **DBSCAN (Density-Based Spatial Clustering of Applications with Noise)** using only **NumPy**. It is designed for students and beginners to understand how clustering by density works, without relying on `scikit-learn`.

---

## What You’ll Learn

- What DBSCAN is and how it works
- Key terms: **core points**, **border points**, and **noise**
- How to implement DBSCAN step-by-step:
  - Compute point-to-point distances
  - Find dense neighborhoods (region queries)
  - Expand clusters recursively
- How to visualize DBSCAN results

---

## What is DBSCAN?

DBSCAN groups together points that are **close to each other** (high-density regions), and marks points in **low-density regions** as **outliers (noise)**.

### Main Parameters:
- `eps`: The distance threshold to search for neighboring points
- `min_samples`: Minimum number of neighbors (including self) to form a dense cluster

### Point Types:
| Type         | Definition |
|--------------|------------|
| Core Point   | Has at least `min_samples` neighbors within `eps` |
| Border Point | Has fewer than `min_samples`, but is within `eps` of a core point |
| Noise        | Neither core nor border (considered outlier) |

---

## Files Included

| File                     | Description                                          |
|--------------------------|------------------------------------------------------|
| `dbscan_from_scratch.ipynb` | Full DBSCAN implementation with visualization     |
| `README.md`              | This file describes the purpose and usage         |

---

## How to Use

1. Clone or download this repository
2. Open the notebook `dbscan_from_scratch.ipynb` in:
   - Jupyter Notebook, OR
   - Google Colab
3. Run each cell in order:
   - Generate sample clustered data with outliers
   - Implement DBSCAN logic step-by-step
   - Visualize the discovered clusters and noise

---

## Requirements

This project requires:

- Python 3.x
- NumPy
- Matplotlib

Install dependencies:

```bash
pip install numpy matplotlib
```

---

## Best Use-Cases for DBSCAN
* Clustering data with irregular shapes
* Detecting anomalies or outliers
* Geospatial clustering (e.g., identifying areas of interest)
* When the number of clusters is not known ahead of time
* When you’re okay with labeling some points as noise and don’t want to force every point into a cluster.

---

## Why DBSCAN?
* No need to specify the number of clusters (`k`)
* Automatically detects outliers (noise)
* Works well for non-spherical clusters (unlike K-Means)

---

## Suggested Experiments
* Try different `eps` and `min_samples` values
* Compare with K-Means to observe differences
* Visualize step-by-step region expansion
* Apply to real-world datasets (e.g., GPS coordinates, customer behavior)

---

## License
This project is open-source and licensed under the MIT License.

---

## Contribute
Contributions are welcome; feel free to optimize the implementation, visualize regions, or add interactive widgets for parameter tuning.

