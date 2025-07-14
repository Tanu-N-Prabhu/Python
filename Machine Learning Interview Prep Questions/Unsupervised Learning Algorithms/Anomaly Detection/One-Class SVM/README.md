# One-Class SVM from Scratch (No Classes, Fully Explained)

This notebook implements the **One-Class Support Vector Machine (SVM)** algorithm from scratch using pure NumPy, without scikit-learn or classes, and with full explanations at every step.

It is perfect for learning how anomaly detection works under the hood and for preparing for interviews.

---

## What Is One-Class SVM?

**One-Class SVM** is an **unsupervised anomaly detection** algorithm. It learns the boundary of "normal" data and classifies any data point that falls **outside this learned boundary as an anomaly**.

It’s beneficial when you only have normal data and want to detect outliers.

---

## Core Concept

Given only normal data $$( X )$$, the model learns a function $$( f(x) )$$ such that:

- $$( f(x) \geq 0 )$$ for **normal** data  
- $$( f(x) < 0 )$$ for **anomalies**

This is achieved by solving the **dual optimization problem** using a **kernel function**, typically the **RBF (Gaussian)** kernel.

---

##  Dual Optimization Formula

We optimize the following objective:

$$[
\max_{\alpha} \sum_{i=1}^{n} \alpha_i K(x_i, x_i) - \sum_{i=1}^{n} \sum_{j=1}^{n} \alpha_i \alpha_j K(x_i, x_j)
]$$

Subject to:

$$[
0 \leq \alpha_i \leq \frac{1}{\nu n}, \quad \sum_{i=1}^{n} \alpha_i = 1
]$$

Where:
- $$( \nu )$$ controls the expected proportion of anomalies
- $$( K(x_i, x_j) )$$ is the RBF kernel function
- $$( \alpha_i )$$ are learned weights

---

##  What’s Included

| File                                | Description                                 |
|:-------------------------------------|:---------------------------------------------|
| `one_class_svm_from_scratch.ipynb`  | Pure NumPy implementation with no classes   |
| `README.md`                         | You’re reading it                           |

---

##  Features

- Full training using **gradient descent**
- Enforces constraints via **simplex projection**
- Computes anomaly scores for new data
- Pure **functional implementation** – no classes
- Works on **2D data**, can be extended

---

##  Output Example

```
Test Point 0: [ 0.3, -0.4 ] | Score: 0.7821 | Normal ✅
Test Point 12: [5.1, 5.6] | Score: 0.1034 | Anomaly 🚨
```

---

## How It Works

| Step | Description |
|:------|:-------------|
| 1.   | Generate training data (normal only) |
| 2.   | Define RBF (Gaussian) kernel |
| 3.   | Compute full kernel matrix |
| 4.   | Optimize α using gradient descent (dual form) |
| 5.   | Project α onto the simplex to meet constraints |
| 6.   | Compute decision function $$( f(x) )$$ |
| 7.   | Predict anomaly using score threshold |

---

##  Parameters

| Parameter   | Description                         |
|:------------|:-------------------------------------|
| `nu`        | Expected proportion of anomalies (e.g., 0.1) |
| `gamma`     | RBF kernel bandwidth                |
| `threshold` | Decision boundary (auto-calculated from training set) |
| `n_iters`   | Number of training iterations       |
| `lr`        | Learning rate for gradient descent  |

---

## Requirements

No libraries except:

```bash
numpy
matplotlib
```

---

## Who Is This For?
* Students learning ML internals
* Interview candidates
* Educators & tutors
* Anyone curious about how One-Class SVM works

---

## License
This project is licensed under the MIT License. You’re free to reuse, modify, and share for educational or personal use.


---

##  Contribute
Pull requests and improvements are welcome! Ideas:
* Extend to higher-dimensional data
* Compared to scikit-learn's OneClassSVM
* Visualize decision boundaries
  
> Happy Anomaly Hunting! 🎯




