# Mean Shift Clustering from Scratch (No ML Libraries, No Classes)

This notebook walks you through the implementation of **Mean Shift Clustering**, a powerful unsupervised algorithm that discovers clusters by identifying high-density regions, all done using just **NumPy**, without classes or libraries like `scikit-learn`.

---

## What You'll Learn

- What Mean Shift is and how it works
- How to implement the algorithm step-by-step
- The role of the **bandwidth radius** in clustering
- How to find and visualize cluster centers
- How to auto-detect the number of clusters

---

## What is Mean Shift?

Mean Shift is a **density-based clustering algorithm** that works by:
1. Placing a circular window (radius = bandwidth) over each point
2. Shifting the window toward the **mean** of the points within it
3. Repeating until convergence (high-density regions)
4. Grouping similar "modes" into clusters

### Key Parameter:
- `radius` (bandwidth): The size of the search window that determines the smoothness and number of clusters

---

## Files Included

| File                          | Description                                           |
|-------------------------------|-------------------------------------------------------|
| `mean_shift_from_scratch.ipynb` | Full NumPy-based implementation with visualization |
| `README.md`                   | This file explains purpose, usage, and logic       |

---

## How to Use

1. Clone or download this repository
2. Open `mean_shift_from_scratch.ipynb` in:
   - Jupyter Notebook, **OR**
   - Google Colab
3. Run each cell to:
   - Generate synthetic 2D data
   - Run the Mean Shift algorithm
   - Visualize the clusters and centers

---

## Requirements

- Python 3.x
- NumPy
- Matplotlib

Install them with:

```bash
pip install numpy matplotlib
```

---

## Why Mean Shift?
* Automatically detects number of clusters
* Works well for irregular-shaped clusters
* Simple to implement and interpret
* Useful in image segmentation, pattern recognition, and GPS data analysis

---

## Suggested Experiments
* Try different `radius` (bandwidth) values
* Use the algorithm on real-world datasets (e.g., GPS, images)
* Compare with K-Means and DBSCAN
* Add kernel density weighting (Gaussian kernel)

---

## License
This project is open-source and available under the MIT License.

---

## Contribute
* Pull requests are welcome! Ideas
  * Add Gaussian kernel for smoother results
  * Support for higher-dimensional data
  * Visualize shifting paths for learning
