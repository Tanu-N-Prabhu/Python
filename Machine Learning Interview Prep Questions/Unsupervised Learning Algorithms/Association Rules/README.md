# Association Rule Mining

This section of the repository is dedicated to **Association Rule Mining**, a key technique in data mining that helps uncover interesting relationships (associations) between variables in large datasets, especially **transactional data**.

You’ll learn and implement three major algorithms **from scratch** using pure Python:

- Apriori
- ECLAT
- FP-Growth

---

## What is Association Rule Mining?

**Association rule mining** uncovers patterns like:

> "If a customer buys bread and butter, they are likely to buy jam."

Each rule is evaluated using three key metrics:

| Metric     | Meaning                                                                 |
|:------------|:-------------------------------------------------------------------------|
| **Support** | How frequently the itemset appears in the dataset                      |
| **Confidence** | How often the rule is true                        |
| **Lift**     | How much more likely the consequent is, given the antecedent          |

---

##  Algorithms Covered

### 1.  Apriori Algorithm

- **Strategy**: Bottom-up, level-wise candidate generation
- **How it works**:
  - Iteratively expands frequent itemsets
  - Prune infrequent ones using minimum support
- **Drawback**: Slower due to repeated scans and candidate generation

> File: [apriori_from_scratch.ipynb](https://github.com/Tanu-N-Prabhu/Python/blob/master/Machine%20Learning%20Interview%20Prep%20Questions/Unsupervised%20Learning%20Algorithms/Association%20Rules/Apriori%20Algorithm/apriori_from_scratch.ipynb)

---

### 2. ECLAT Algorithm

- **Strategy**: Depth-first search using TID (Transaction ID) sets
- **How it works**:
  - Stores data in a vertical format
  - Mine frequent itemsets via set intersections
- **Advantage**: Faster than Apriori on dense datasets

> File: [eclat_from_scratch.ipynb](https://github.com/Tanu-N-Prabhu/Python/blob/master/Machine%20Learning%20Interview%20Prep%20Questions/Unsupervised%20Learning%20Algorithms/Association%20Rules/Equivalence%20Class%20Clustering%20and%20bottom-up%20Lattice%20Traversal/eclat_from_scratch.ipynb)

---

### 3. FP-Growth Algorithm

- **Strategy**: Tree-based pattern growth
- **How it works**:
  - Builds a compressed prefix-tree (FP-Tree)
  - Avoids candidate generation altogether
- **Advantage**: Fastest and most scalable

> File: [fp_growth_from_scratch.ipynb](https://github.com/Tanu-N-Prabhu/Python/blob/master/Machine%20Learning%20Interview%20Prep%20Questions/Unsupervised%20Learning%20Algorithms/Association%20Rules/Frequent%20Pattern%20Growth/fp_growth_from_scratch.ipynb)

---

## Folder Structure

```text
association_rule_mining/
├── apriori_from_scratch.ipynb         # Apriori with support, confidence, lift
├── eclat_from_scratch.ipynb           # ECLAT with frequent itemset mining
├── fp_growth_from_scratch.ipynb       # FP-Growth with prefix tree mining
└── README.md                          # This file
```


---

## Algorithm Comparison

| Feature               | Apriori           | ECLAT             | FP-Growth         |
|:----------------------|:-------------------|:-------------------|:-------------------|
| Data Format           | Horizontal         | Vertical           | Tree (prefix)     |
| Search Strategy       | Breadth-First      | Depth-First        | Pattern Growth    |
| Candidate Generation  | Yes             |  No              |  No              |
| Speed on Large Data   | Slow            |  Medium          | Fastest         |
| Memory Usage          | Moderate           | Can be high        | Efficient          |
| Ease of Implementation| Easy            | Moderate         | Complex         |

---

## Output Example (Apriori)

```text
milk → bread   (support=0.67, confidence=1.0, lift=1.5)
jam → bread    (support=0.5, confidence=1.0, lift=1.5)
```

---

## Suggested Applications
* Market Basket Analysis 
* Recommender Systems 
* Fraud Detection 
* Cross-sell/Up-sell Strategies 
* Web Usage Mining 

---

## Requirements
All notebooks use pure Python. No external libraries are required to run the core logic:

```
python 3.x
```

For visualization or performance analysis, you can optionally add:
* `matplotlib`, `pandas` (for display)
* `networkx` or `graphviz` (for tree visualization)

---

## Who This Is For
This resource is ideal for:
  * ML/DS beginners
  * Students preparing for interviews
  * Learners wanting to understand how things work under the hood

---

## License
MIT License: free to use, fork, improve, and share.

---

## Contribute
* Pull requests are welcome! You can help by:
    * Adding association rule generation to FP-Growth
    * Testing with real-world datasets
    * Improving code readability or performance

> Happy Mining!
