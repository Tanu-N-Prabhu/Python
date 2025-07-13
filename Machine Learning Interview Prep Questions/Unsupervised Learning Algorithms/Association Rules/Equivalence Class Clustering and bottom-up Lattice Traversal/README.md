# ECLAT Algorithm from Scratch (Python Only)

This notebook demonstrates a clean and minimal implementation of the **ECLAT algorithm** (Equivalence Class Clustering and bottom-up Lattice Traversal) using only **pure Python**.

ECLAT is a powerful algorithm for mining **frequent itemsets** and is often used as an alternative to Apriori when working with **dense datasets** or when performance matters.

---

## What is ECLAT?

**ECLAT** is an algorithm for **frequent pattern mining** that uses:
- A **vertical data format**: Each item is associated with a set of Transaction IDs (TIDs)
- **Set intersection** to find common occurrences of items
- A **depth-first search (DFS)** strategy to efficiently explore itemset combinations

It is generally faster and more memory-efficient than Apriori when working with smaller memory footprints or large datasets.

---

## How It Works

1. Transform the data into a **vertical format**: item → TID set
2. Use **recursive intersection** of TID sets to build itemsets
3. Prune combinations that don't meet the **minimum support threshold**

---

## Files Included

| File                      | Description                                                  |
|:---------------------------|:--------------------------------------------------------------|
| `eclat_from_scratch.ipynb`| Python notebook implementing ECLAT with support calculation  |
| `README.md`               | This file explains the algorithm and how to use it         |

---

## Example Transactions Used

```python
transactions = [
    ['milk', 'bread', 'butter'],
    ['bread', 'butter'],
    ['milk', 'bread'],
    ['milk', 'bread', 'butter', 'jam'],
    ['bread', 'jam'],
    ['milk', 'bread', 'jam']
]
```

---

## Sample Output
With a minimum support of 0.4 (i.e. 40% of transactions):

```
Frequent Itemsets (Support ≥ 0.4):
('bread',): 1.0
('milk',): 0.67
('butter',): 0.5
('jam',): 0.5
('bread', 'butter'): 0.5
('bread', 'milk'): 0.67
('bread', 'jam'): 0.5
('milk', 'jam'): 0.5
('bread', 'milk', 'jam'): 0.5
```

---

## Why Use ECLAT?

| Feature            | ECLAT                            | Apriori                       |
|:------------------ |:-------------------------------- |:----------------------------- |
| Data Format        | Vertical (item → TIDs)           | Horizontal (transaction-wise) |
| Search Strategy    | Depth-First Search (DFS)         | Breadth-First Search (BFS)    |
| Speed (Dense Data) | Faster with item intersections | Slower with repeated scans  |
| Memory Usage       | Can grow with large TID sets  | Moderate                      |

---

## Requirements
No libraries needed! This notebook runs with just basic Python:
```
python 3.x
```

---

## How to Use
1. Clone or download this repository
2. Open `eclat_from_scratch.ipynb` in:
    1. Jupyter Notebook or
    2. Google Colab
3. Set your own `transactions` list and `min_support` value\
4. Run all cells to:
    1. Convert to vertical format
    2. Mine frequent itemsets
    3. Display results

---

## Suggested Extensions
* Add association rule generation (confidence, lift) like Apriori
* Use a larger retail or grocery dataset (e.g., from Kaggle)
* Save frequent itemsets to a CSV or JSON
* Compare ECLAT vs Apriori vs FP-Growth on runtime and accuracy

---

## License
Open-source under the MIT License, use and adapt freely!

---


## Contribute
Feel free to open issues or pull requests to improve this notebook!
