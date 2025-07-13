# Apriori Algorithm from Scratch (with Association Rules)

This notebook contains a full implementation of the **Apriori algorithm** from scratch using **pure Python**, no external machine learning libraries like `mlxtend`, `pandas`, or `NumPy`.

You’ll learn how to:
- Find **frequent itemsets**
- Generate **association rules**
- Calculate **support**, **confidence**, and **lift**

---

## What is the Apriori Algorithm?

The **Apriori algorithm** is a classic algorithm for **frequent itemset mining** and **association rule learning**. It helps discover patterns in transaction data — for example:

> If customers buy **milk** and **bread**, they’re likely to buy **butter**.

---

## Key Concepts

| Metric       | Description                                                                 |
|:--------------|:-----------------------------------------------------------------------------|
| **Support**  | How often the itemset appears in the data                                   |
| **Confidence** | How often the rule holds true: P(A → B) = P(A ∪ B) / P(A)                |
| **Lift**     | Measures strength of rule over random chance: Lift = Confidence / P(B)     |

---

## Files Included

| File                          | Description                                               |
|:-------------------------------|:-----------------------------------------------------------|
| `apriori_from_scratch.ipynb`  | Notebook with Apriori logic, rule generation, and metrics |
| `README.md`                   | This file explains the algorithm and how to use it      |

---

## Example Transactions

```python
transactions = [
    ['milk', 'bread', 'butter'],
    ['bread', 'butter'],
    ['milk', 'bread'],
    ['milk', 'bread', 'butter', 'jam'],
    ['bread', 'jam'],
    ['milk', 'bread', 'jam'],
]
```

---

## What the Notebook Does
- Identify frequent itemsets above `min_support`
- Generate association rules using frequent itemsets
- Filter rules based on `min_confidence` and `min_lift`
- Print rules in readable format

---

## How to Use
1. Clone or download this repository
2. Open `apriori_from_scratch.ipynb` in:
    1. Google Colab, or
    2. Jupyter Notebook
3. Run all cells to:
    1. Load the sample transactions
    2. Run the Apriori algorithm
    3. Print frequent itemsets
    4. Generate and view association rules

---

## Sample Output
> Frequent Itemsets (Support ≥ 0.4):

```
('bread',): 1.00  
('milk',): 0.67  
('butter',): 0.50  
('jam',): 0.50  
('bread', 'milk'): 0.67  
('bread', 'butter'): 0.50  
('bread', 'jam'): 0.50  
('milk', 'jam'): 0.50
```

---

## Association Rules (Confidence ≥ 0.6, Lift ≥ 1.0):

```
milk → bread     (support=0.67, confidence=1.0, lift=1.5)  
jam → bread      (support=0.5, confidence=1.0, lift=1.5)  
butter → bread   (support=0.5, confidence=1.0, lift=1.5)
```

---

## Requirements
You only need base Python (no pip install needed):

```
python 3.x
```

> No external libraries like pandas, NumPy, or scikit-learn are used.


---

## Suggested Exercises
- Add support for `min_confidence` and `min_lift` as parameters
- Modify the dataset to test new rules
- Visualize rules using a graph (e.g., with `networkx`)
- Export rules to a CSV for review

---

## License
MIT License – Free to use, modify, and share.

---


## Contribute
- Pull requests are welcome! Ideas for improvement:
  - Convert output to Pandas DataFrames
  - Add rule pruning
  - Include large datasets from real-world retail

> Happy learning!  
