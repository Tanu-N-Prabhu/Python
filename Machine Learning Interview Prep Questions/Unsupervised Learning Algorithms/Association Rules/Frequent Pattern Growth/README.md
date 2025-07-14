# FP-Growth Algorithm from Scratch (Pure Python)

This notebook contains a **from-scratch implementation** of the **FP-Growth (Frequent Pattern Growth)** algorithm using only basic Python, no libraries like `pandas`, `mlxtend`, or `NumPy`.

The FP-Growth algorithm is widely used for **frequent itemset mining**, especially in large-scale transaction data. Unlike Apriori, it avoids repeated database scans and eliminates candidate generation using a compact data structure called an **FP-Tree**.

---

## What You'll Learn

- How to build an **FP-Tree** (prefix tree) from transactions
- How to recursively **mine conditional FP-Trees**
- How to extract **frequent itemsets** efficiently
- Why FP-Growth is **faster than Apriori or ECLAT** for large datasets

---

## What is FP-Growth?

FP-Growth stands for **Frequent Pattern Growth**. It is an efficient algorithm that:

- **Compresses** the dataset using a prefix tree (FP-Tree)
- **Avoids** costly candidate generation
- **Recursively mines** frequent itemsets from conditional trees

---

## How It Works

1. **Build the FP-Tree**:
   - Scan the dataset to get item frequencies
   - Remove items below `min_support`
   - Sort each transaction by item frequency
   - Insert transactions into the FP-Tree

2. **Mine Frequent Patterns**:
   - Traverse the tree bottom-up using item links
   - Build **conditional pattern bases** for each item
   - Recursively mine smaller FP-Trees

---

## Files Included

| File                      | Description                                                  |
|:---------------------------|:--------------------------------------------------------------|
| `fp_growth_from_scratch.ipynb` | FP-Growth algorithm built using Python classes and recursion |
| `README.md`               | This file explains the implementation and usage            |

---

## Sample Transactions

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
With a minimum support count of 3:

```Frequent Itemsets:
('bread',): 6
('jam',): 3
('bread', 'jam'): 3
('butter',): 3
('bread', 'butter'): 3
('milk',): 4
('milk', 'bread'): 4
```

---


## Comparison with Other Algorithms

| Feature              | Apriori       | ECLAT       | FP-Growth        |
|:-------------------- |:------------- |:----------- |:---------------- |
| Strategy             | Breadth-First | Depth-First | Tree Growth      |
| Data Format          | Horizontal    | Vertical    | Compressed Tree  |
| Candidate Generation |  Yes         |  No        |  No             |
| Memory Usage         | Moderate      | Can be high | Efficient (Tree) |
| Speed (Large Data)   |  Slow        |  Medium   |  Fast           |

---

## How to Use
1. Clone or download this repo
2. Open `fp_growth_from_scratch.ipynb` in:
      1. Google Colab or
      2. Jupyter Notebook
3. Set your own `transactions` and `min_support`
4. Run all cells to:
      1. Build the FP-Tree
      2. Mine frequent itemsets
      3. View itemsets with their support count

---

## Requirements
Only Python 3 is needed:

```
python 3.x
```
No external dependencies required.

---

## Suggestions
* Add support for association rule generation (confidence, lift)
* Compare runtime with Apriori and ECLAT on larger datasets
* Export itemsets to a CSV or JSON file
* Visualize the FP-Tree using `graphviz` or `networkx` (optional)

---

## License
This project is open-source under the MIT License, free to use for education, learning, and improvement.

---


## Contribute
PRs welcome! Help improve the algorithm, add rule mining, or integrate with a real-world dataset (e.g., Groceries, Retail).

> Happy learning

