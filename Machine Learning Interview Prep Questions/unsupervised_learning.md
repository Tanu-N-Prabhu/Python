# Unsupervised Learning Interview Questions

Unsupervised learning models work with unlabeled data to find hidden patterns or structures. Common techniques include **clustering** and **dimensionality reduction**.

---

## 1. What is Unsupervised Learning?

Unsupervised learning deals with input data that has **no labels**. The model tries to learn the structure or distribution of the data to uncover useful patterns.

---

## 2. K-Means Clustering

### Key Concepts:
- Partition data into **K distinct clusters**.
- Uses the **centroid** of clusters to minimize intra-cluster variance.
- Sensitive to initialization and requires specifying K.

### Interview Questions:
- How does K-Means work step-by-step?
- How do you choose the right number of clusters?
- What are the limitations of K-Means?
- What is the Elbow Method?

### Mini Case Study:
**Problem:** Segment customers based on purchasing behavior.  
**Model:** K-Means clusters customers into groups like “high spenders,” “occasional buyers,” etc., for targeted marketing.

---

## 3. DBSCAN (Density-Based Spatial Clustering of Applications with Noise)

### Key Concepts:
- Groups together points that are **close in density**.
- Can find **non-spherical clusters** and **handle noise/outliers**.
- Does **not** require the number of clusters in advance.

### Interview Questions:
- How does DBSCAN determine dense regions?
- What are `eps` and `min_samples`?
- What are the advantages of DBSCAN over K-Means?
- Can DBSCAN be used in high-dimensional data?

### Mini Case Study:
**Problem:** Detect spatial clusters of disease outbreaks.  
**Model:** DBSCAN can identify dense areas of infection without requiring a predefined number of clusters.

---

## 4. Hierarchical Clustering

### Key Concepts:
- Builds a hierarchy of clusters using either **agglomerative (bottom-up)** or **divisive (top-down)** approach.
- Often visualized using a **dendrogram**.

### Interview Questions:
- What is the difference between agglomerative and divisive clustering?
- How do you interpret a dendrogram?
- What is linkage criteria (single, complete, average)?
- When is hierarchical clustering preferred over K-Means?

### Mini Case Study:
**Problem:** Group news articles by topic.  
**Model:** Hierarchical clustering reveals nested topic groupings based on text similarity.

---

## 5. PCA (Principal Component Analysis)

### Key Concepts:
- A **dimensionality reduction** technique that transforms data into new axes (principal components).
- Captures the **most variance** in the data using fewer features.

### Interview Questions:
- What is PCA and how does it work?
- What are eigenvectors and eigenvalues in PCA?
- How do you decide how many principal components to keep?
- Is PCA a supervised or unsupervised method?

### Mini Case Study:
**Problem:** Reduce image data size while retaining features.  
**Model:** PCA transforms high-dimensional pixel data into a smaller set of features while preserving structure.

---

## Comparison Table

| Technique         | Type        | Strengths                           | Limitations                     |
|------------------|-------------|-------------------------------------|---------------------------------|
| K-Means           | Clustering  | Simple, scalable                    | Needs K, sensitive to noise     |
| DBSCAN            | Clustering  | Handles noise, arbitrary shapes     | Struggles with varying densities |
| Hierarchical Clustering | Clustering | Dendrogram visualization, no need to pre-specify K | Computationally expensive        |
| PCA               | Dimensionality Reduction | Reduces overfitting, improves visualization | Components may be hard to interpret |

---

> **Next Steps:**  
Move to [`evaluation_metrics.md`](./evaluation_metrics.md) to learn how to evaluate your models effectively using metrics like accuracy, precision, recall, and F1 score.
