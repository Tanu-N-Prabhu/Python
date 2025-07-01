# 📦 Data Versioning in Machine Learning

Data versioning is the practice of **tracking, labeling, and managing changes** to datasets used in ML pipelines—just like you version control code with Git.

---

## 🚨 Why Is Data Versioning Important?

- **Reproducibility**: Know exactly which data was used for a model.
- **Collaboration**: Share consistent versions with your team.
- **Experiment Tracking**: Compare model performance across data changes.
- **Auditing**: For regulated industries (healthcare, finance, etc.).
- **Debugging**: Go back to the dataset that caused a specific bug.

---

## 🧰 Tools for Data Versioning

| Tool      | Description                                                  | Type            |
|-----------|--------------------------------------------------------------|-----------------|
| **DVC**   | Git-like tool for large datasets, integrates with Git        | Open-source CLI |
| **LakeFS**| Git for data lakes, supports branching & commit history      | Cloud/On-prem   |
| **Pachyderm** | Data pipelines with versioned data                        | Open-source     |
| **Weights & Biases (W&B)** | Dataset tracking, metrics, and artifacts       | SaaS Platform   |
| **Git LFS**| Extension to Git for large binary files                     | Git plugin      |

---

## 🛠️ Example: Using DVC (Data Version Control)

### Step 1: Initialize DVC
```bash
pip install dvc
dvc init
