# Isolation Forest from Scratch (No Classes, Pure Python)

This notebook implements the **Isolation Forest** algorithm for **anomaly detection** using only basic Python and simple functions, no external libraries, no object-oriented code.

It’s designed to be easy to understand, beginner-friendly, and interview-ready.

---

## What Is Isolation Forest?

**Isolation Forest** is an efficient algorithm for detecting anomalies in data. Unlike other models that profile normal data, Isolation Forest directly **isolates anomalies** by:

- Randomly selecting a feature
- Randomly selecting a split value
- Recursively repeating until the data point is isolated

Because **anomalies are rare and different**, they require fewer splits to isolate, giving them **shorter path lengths** in the tree.

---

## Core Idea

| Concept         | Meaning                                                                 |
|:-----------------|:-------------------------------------------------------------------------|
| Isolation Tree  | A binary tree that splits data until points are isolated                |
| Path Length     | Number of splits it takes to isolate a data point                       |
| Anomaly Score   | Shorter average path length = more likely to be an anomaly              |
| Threshold       | You choose a score above which a point is considered an anomaly         |

---

## Files Included

| File                              | Description                                 |
|-----------------------------------|---------------------------------------------|
| `isolation_forest_from_scratch.ipynb` | Main notebook with function-based implementation |
| `README.md`                        | This file                                |

---

## How It Works

1. Generate synthetic normal + anomalous data  
2. Build multiple random binary trees (isolation trees)  
3. Compute path length for each point in each tree  
4. Average the lengths and normalize them  
5. Score each point: shorter path = higher anomaly score  
6. Use a threshold (like 0.6) to label data points  

---

## Output Example

```
Point 0: [0.2, -0.1] | Score: 0.31 | Normal ✅
Point 101: [6.4, 7.2] | Score: 0.89 | Anomaly 🚨
Point 102: [7.5, 6.9] | Score: 0.93 | Anomaly 🚨
```
---

## Parameters You Can Tune

| Parameter      | Description                                  |
|----------------|----------------------------------------------|
| `n_trees`      | Number of isolation trees (e.g. 100)          |
| `sample_size`  | Subset size for building each tree (e.g. 64) |
| `threshold`    | Score above which a point is an anomaly      |

---

## Why Use Isolation Forest?

| Feature                 | Benefit                                  |
|-------------------------|-------------------------------------------|
| No assumptions          | Works without assuming normality          |
| High-dimensional data   | Handles many features well                |
| Linear time complexity  | Very efficient for large datasets         |
| Easy to scale           | Great for online or real-time detection   |

---

## Requirements

No dependencies! Just basic Python 3:

```bash
python 3.x
```

This notebook does not use:
- scikit-learn
- pandas
- numpy

---

## Who Should Use This
* Students learning anomaly detection
* Anyone preparing for ML interviews
* Teachers/trainers looking to explain ML algorithms clearly
* Developers interested in internals of algorithms

---


## Learning Goals
* Understand how isolation works for anomalies
* Implement an algorithm without black-box libraries
* Explain your implementation line-by-line in interviews

---

## License
This project is licensed under the MIT License, open for education, reuse, and modification.

---


## Contributions Welcome
Feel free to:
* Add visualization (e.g., `matplotlib`)
* Test with real-world datasets (e.g., credit card fraud)
* Improve clarity, performance, or usability

> Happy Isolating! 
