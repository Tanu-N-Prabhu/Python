# Anomaly Detection in Machine Learning

This section of the repository contains hands-on, from-scratch implementations of **Anomaly Detection** algorithms using Python and NumPy. These algorithms are designed to help identify rare items, events, or observations that raise suspicions by differing significantly from the majority of the data.

---

## What is Anomaly Detection?

**Anomaly detection** is the process of identifying unusual data points or patterns that do not conform to expected behavior. It is widely used in:

- Fraud detection (e.g., credit card fraud)
- Network security (e.g., intrusion detection)
- Industrial systems (e.g., fault detection)
- Healthcare (e.g., identifying disease outliers)
- Quality control in manufacturing

---

## Algorithms Covered

| Algorithm               | Description                                                                 |
|:------------------------|:-----------------------------------------------------------------------------|
| [`Isolation Forest`](./isolation_forest.ipynb)  | Detects anomalies by randomly isolating points in the feature space. |
| [`One-Class SVM`](./one_class_svm.ipynb)        | Learns a decision boundary that encloses normal instances only.      |
| [`Local Outlier Factor (LOF)`](./lof_from_scratch.ipynb) | Detects anomalies by comparing the local density of each point to its neighbors. |
| [`Elliptic Envelope`](./elliptic_envelope.ipynb) _(coming soon)_ | Assumes data is Gaussian and fits an ellipse around normal points. |
| [`Autoencoders`](../unsupervised_learning/autoencoders.ipynb) | Neural networks trained to reconstruct input; large reconstruction error may indicate anomaly. |

---

## Core Concepts

| Term                  | Meaning                                                                 |
|-----------------------|-------------------------------------------------------------------------|
| **Outlier**           | A data point that significantly differs from others.                    |
| **Density-based**     | Compare local density of data points (e.g., LOF).                       |
| **Distance-based**    | Use distance to neighbors or clusters to determine anomalies.           |
| **Model-based**       | Use statistical or machine learning models to detect deviations.        |
| **Reconstruction-based** | Use models like Autoencoders to reconstruct input and flag errors.   |

---

## When to Use Anomaly Detection

- When labels for anomalies are scarce or nonexistent.
- When your dataset is highly imbalanced.
- For early warning systems (e.g., predictive maintenance).
- In real-time detection pipelines (streaming anomalies).

---

## How to Use

Each notebook includes:

- A clean dataset generation or loading step.
- Step-by-step procedural implementation (no classes).
- Visualizations and anomaly score interpretations.
- Explanations written for interviews and academic clarity.

---

## Tools & Libraries Used

- `NumPy` – for mathematical operations.
- `Matplotlib` – for data visualization.
- `scikit-learn` – for dataset generation or comparison.

---

## Ideal For

- Students preparing for machine learning interviews.
- Anyone wanting to understand how anomaly detection works under the hood.
- Educators and mentors explaining ML algorithms interactively.

---

## Licensing

All code is provided under the MIT License. Please cite or link back if you use it for teaching or projects.

---

## Folder Structure

```text
anomaly_detection/
├── isolation_forest.ipynb
├── one_class_svm.ipynb
├── lof_from_scratch.ipynb
├── elliptic_envelope.ipynb # Coming soon
├── README.md
```

---

## Next Steps

- Compare these algorithms side-by-side on the same dataset.
- Try applying these on real datasets (e.g., credit card fraud, server logs).
- Extend the logic using `scikit-learn`, `PyOD`, or `TensorFlow`.

---

> Happy Detecting!
