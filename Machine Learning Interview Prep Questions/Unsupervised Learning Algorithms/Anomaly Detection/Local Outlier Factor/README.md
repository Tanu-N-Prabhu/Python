# Local Outlier Factor (LOF) from Scratch

This notebook implements the **Local Outlier Factor (LOF)** algorithm from scratch using pure NumPy, no machine learning libraries and no object-oriented code. It’s written to help students understand the intuition, math, and implementation of LOF for anomaly detection.

---

## What is LOF?

**Local Outlier Factor (LOF)** measures the **local deviation of a data point** with respect to its neighbors. It identifies outliers by comparing the local density of a point to the densities of its neighbors.

### Key Concepts:
| Term                        | Description |
|:-----------------------------|:-------------|
| **k-distance**              | Distance from a point to its k-th nearest neighbor |
| **Reachability distance**   | Max(k-distance of neighbor, actual distance to neighbor) |
| **Local reachability density (LRD)** | Inverse of average reachability distance to k-nearest neighbors |
| **LOF score**               | Ratio of average LRD of neighbors to the LRD of the point |

---

##  What You'll Learn

- The full LOF algorithm in a simple procedural format
- How to compute distances and densities manually
- Visualizing outliers with clear matplotlib plots
- How to interpret LOF scores to detect anomalies

---

## File Structure

```
lof_from_scratch/
├── lof_from_scratch.ipynb # Jupyter notebook with full implementation
├── README.md # This documentation file
```


---

## ▶How to Run

1. Open the `lof_from_scratch.ipynb` file in **Google Colab** or **Jupyter Notebook**.
2. Run each cell sequentially to see:
   - Data generation
   - Manual k-nearest neighbor logic
   - Reachability and density computations
   - Final LOF score calculation and anomaly detection
3. Check the scatterplot for visual confirmation of anomalies.

---

## Output Example

- LOF scores printed for each point
- Data points colored based on LOF score (anomaly vs normal)
- A plot showing clusters and detected outliers

---

## LOF Score Interpretation

| LOF Score Range | Interpretation          |
|------------------|--------------------------|
| ≈ 1              | Normal point              |
| > 1              | Mild anomaly              |
| ≫ 1 (e.g., > 1.5) | Strong anomaly 🚨         |

---

## Tip for Students

If you're asked about LOF in an interview:
- Explain it compares **local density**.
- Mention **reachability distance** and **LRD**.
- Show how LOF uses the ratio of local densities to detect outliers.
- Be ready to describe or write core logic: like `k_nearest_neighbors()` and `compute_lof_scores()`.

---

## References

- [Original LOF Paper](https://www.dbs.ifi.lmu.de/Publikationen/Papers/LOF.pdf)
- [scikit-learn LOF](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.LocalOutlierFactor.html)

---

## License

MIT License

