# Dimensionality Reduction in Machine Learning

Dimensionality reduction is the process of reducing the number of input variables or features in a dataset. It helps simplify models, speed up computation, and visualize complex data more effectively.

This folder contains practical, from-scratch implementations of the most important dimensionality reduction techniques using **NumPy** and **visual examples** to help you truly understand how they work.

---

## Why Dimensionality Reduction?

- Reduce high-dimensional data to 2D or 3D for visualization
- Improve model performance and training speed
- Remove noise and irrelevant features
- Reveal hidden patterns and clusters
- Make data interpretable for humans

---

## Files Included

| Notebook/File                    | Description                                                  |
|:----------------------------------|:--------------------------------------------------------------|
| `pca_from_scratch.ipynb`         | Principal Component Analysis (PCA) using eigenvectors        |
| `tsne_from_scratch.ipynb`        | Visualizes high-dimensional data with t-SNE                  |
| `umap_from_scratch.ipynb`        | UMAP implementation using k-NN graph and manifold learning   |
| `autoencoder_from_scratch.ipynb` | Neural network-based compression and reconstruction (AE)     |
| `README.md`                      | This file explains how and why to use these techniques     |

---

## Techniques Covered

| Technique     | Type                | Purpose                                          | Best Use-Cases                                     |
|:---------------|:---------------------|:--------------------------------------------------|:----------------------------------------------------|
| **PCA**        | Linear               | Maximize variance along orthogonal axes          | Feature compression, noise reduction               |
| **t-SNE**      | Non-linear           | Preserve local relationships (probabilistic)     | Visualizing word embeddings, clusters              |
| **UMAP**       | Non-linear           | Preserve both local and global structure         | High-speed visualizations of large datasets        |
| **Autoencoder**| Neural Network-based | Learn compressed representations with a decoder  | Denoising, anomaly detection, deep feature learning|

---

## Example Use-Cases

- Compressing 1000+ word embedding features into 2D for plotting
- Exploring hidden structure in gene expression datasets
- Reducing image features for classification tasks
- Visualizing high-dimensional text or NLP embeddings

---

## Requirements

You only need basic Python libraries:

```bash
pip install numpy matplotlib scipy scikit-learn
```

> No `tensorflow`, `pytorch`, or `umap-learn` used; this repo is focused on learning the core math from scratch.

---

## How to Use
* Open any notebook (e.g., `pca_from_scratch.ipynb`) in Jupyter or Google Colab.
* Run each cell sequentially.
* Read the step-by-step explanations.
* Try modifying dimensions, neighbors, or data sources.

---

## Suggested Projects
* Apply PCA or UMAP to real-world datasets (Iris, MNIST, CIFAR)
* Combine Autoencoder + K-Means for unsupervised clustering
* Compare PCA vs t-SNE vs UMAP on same dataset
* Build a GUI to visualize 2D projections interactively

---

## License
All notebooks are open-source and free to use under the MIT License.

---

## Contributions
Pull requests and suggestions are welcome! You can:
  * Add new datasets
  * Improve visualizations
  * Extend the Autoencoder to Convolutional layers (CNN)
