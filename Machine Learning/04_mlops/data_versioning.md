# Data Versioning in Machine Learning

Data versioning is the practice of **tracking, labeling, and managing changes** to datasets used in ML pipelines—just like you version control code with Git.

---

## Why Is Data Versioning Important?

- **Reproducibility**: Know exactly which data was used for a model.
- **Collaboration**: Share consistent versions with your team.
- **Experiment Tracking**: Compare model performance across data changes.
- **Auditing**: For regulated industries (healthcare, finance, etc.).
- **Debugging**: Go back to the dataset that caused a specific bug.

---

## Tools for Data Versioning

| Tool      | Description                                                  | Type            |
|-----------|--------------------------------------------------------------|-----------------|
| **DVC**   | Git-like tool for large datasets, integrates with Git        | Open-source CLI |
| **LakeFS**| Git for data lakes, supports branching & commit history      | Cloud/On-prem   |
| **Pachyderm** | Data pipelines with versioned data                        | Open-source     |
| **Weights & Biases (W&B)** | Dataset tracking, metrics, and artifacts       | SaaS Platform   |
| **Git LFS**| Extension to Git for large binary files                     | Git plugin      |

---

## Example: Using DVC (Data Version Control)

### Step 1: Initialize DVC

```python
pip install dvc
dvc init
```

### Step 2: Add a dataset

```python
dvc add data/train.csv
git add data/train.csv.dvc .gitignore
git commit -m "Versioned training data with DVC"
```

### Step 3: Push to remote storage (e.g., Google Drive, S3)

```python
dvc remote add -d myremote gdrive://<your-drive-id>
dvc push
```
---

## Best Practices
* Keep raw and processed data separate (e.g., `/data/raw/`, `/data/processed/`)
* Automate version bumps when data changes using CI/CD tools
* Use a centralized remote for team access
* Log dataset versions along with model runs

---

## Summary
* Data versioning is essential for traceable, production-ready ML.
* Tools like DVC integrate seamlessly with Git workflows.
* Always treat your data as a first-class citizen in your ML repo.

---

## Resources
* [DVC Official Docs](https://dvc.org/doc)
* [MLOps with DVC - GitHub Example](https://github.com/iterative/example-get-started)
* [W&B Artifacts Overview](https://docs.wandb.ai/guides/artifacts)




