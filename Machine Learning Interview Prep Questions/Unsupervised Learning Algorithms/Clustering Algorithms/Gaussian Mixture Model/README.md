# Gaussian Mixture Models (GMM) from Scratch (No ML Libraries, No Classes)

This notebook contains a complete, step-by-step implementation of **Gaussian Mixture Models (GMM)** using only **NumPy**. It’s designed for students preparing for interviews or anyone who wants to understand how probabilistic clustering works under the hood, no `scikit-learn`, no classes, no shortcuts.

---

## What You’ll Learn

- What a Gaussian Mixture Model is
- The concept of **soft clustering** (assigning probabilities to points)
- How the **Expectation-Maximization (EM)** algorithm works
- How to implement GMM step-by-step with just NumPy
- How to visualize clusters, centroids, and data distribution

---

## What is GMM?

A **Gaussian Mixture Model** assumes that the data is generated from a combination of several **Gaussian distributions**. It finds the parameters of those distributions using the **Expectation-Maximization (EM)** algorithm.

### Components of a GMM:
- **Mean (μ)** — center of the Gaussian
- **Covariance (Σ)** — shape/spread of the distribution
- **Weight (π)** — proportion of points belonging to each Gaussian

### EM Algorithm:
- **E-Step**: Estimate probabilities (responsibilities) for each point belonging to each cluster
- **M-Step**: Update means, covariances, and weights based on those responsibilities

Unlike K-Means:
- GMM supports **soft clustering** (points belong partially to clusters)
- It models **elliptical** clusters using covariance, not just spherical blobs

---

## Files Included

| File                      | Description                                          |
|---------------------------|------------------------------------------------------|
| `gmm_from_scratch.ipynb`  | Full GMM implementation with visualization           |
| `README.md`               | This file explains the purpose and usage           |

---

## How to Use

1. Clone or download this repository
2. Open `gmm_from_scratch.ipynb` in:
   - Jupyter Notebook, **OR**
   - Google Colab
3. Run the cells to:
   - Generate synthetic data
   - Run the EM algorithm for GMM
   - Visualize clusters and learned parameters

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

##  Why Learn GMM?
* Often asked in machine learning interviews
* Used in real-world problems like:
    * Speech recognition
    * Image segmentation
    * Customer segmentation
* It’s a foundational concept in probabilistic modeling

---

## Suggested Experiments
* Change the number of clusters `k`
* Visualize covariance ellipses using `matplotlib.patches.Ellipse`
* Apply to real-world datasets (e.g., Iris, image pixels)
* Compare GMM’s soft clustering with K-Means hard clustering

---

## License
This project is open-source and available under the MIT License.

---

## Contribute
* Have ideas or improvements?
  * Add support for diagonal/full covariance options
  * Integrate model selection via AIC/BIC
  * Contribute real dataset examples
    
> Pull requests welcome!
