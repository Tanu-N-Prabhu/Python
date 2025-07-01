# Monitoring Machine Learning Models in Production

Monitoring is a critical part of MLOps. Once a model is deployed, you need to **track its performance, reliability, and behavior over time**—just like with any other software system.

---

## Why Model Monitoring Matters

✅ Detect model drift (data or concept drift)  
✅ Identify performance degradation in real-world scenarios  
✅ Catch data pipeline issues (e.g., missing or malformed inputs)  
✅ Ensure fairness, transparency, and compliance  
✅ Maintain trust with users and stakeholders

---

## What to Monitor

### 1. **Prediction Quality**
- Accuracy, precision, recall, F1-score (compared to ground truth if available)
- Confidence score distributions
- Class imbalance warnings

### 2. **Data Quality**
- Missing values or NaNs
- Unexpected value ranges
- Data type mismatches
- Sudden spikes in feature distributions (schema drift)

### 3. **Model Drift**
- **Data Drift**: Input distribution shifts from training
- **Concept Drift**: The relationship between input and output changes

### 4. **Operational Metrics**
- Latency (response time per request)
- Throughput (number of inferences per second)
- Failure rates / system errors

### 5. **Business KPIs**
- Is the model helping meet business goals? (CTR, conversion, churn rate, etc.)

---

## 🛠Tools for Model Monitoring

| Tool                  | Use Case                             | Integration Type     |
|-----------------------|--------------------------------------|----------------------|
| **Prometheus + Grafana** | Monitor latency, memory, CPU        | System-level         |
| **Evidently AI**       | Track drift, data quality, metrics   | Model-level, open-source |
| **WhyLogs**            | Logging and profiling data streams   | Data logging          |
| **Fiddler.ai**         | Monitoring, explainability, bias     | Cloud platform        |
| **Seldon Alibi Detect**| Drift detection with statistical tests | Works with Kubernetes |
| **Arize AI**           | Full model observability             | SaaS platform         |
| **MLflow**             | Model performance tracking (basic)   | Experiment-level      |

---

## Example: Drift Detection with Evidently

```bash
pip install evidently
```

```python
from evidently.report import Report
from evidently.metric_preset import DataDriftPreset
from evidently.test_suite import TestSuite
from evidently.test_preset import DataStabilityTestPreset

ref_data = pd.read_csv("train.csv")
prod_data = pd.read_csv("production_batch.csv")

report = Report(metrics=[DataDriftPreset()])
report.run(reference_data=ref_data, current_data=prod_data)
report.save_html("drift_report.html")
```

---

## Real-Time vs Batch Monitoring

| Type          | Description                                  | Example Tools      |
| ------------- | -------------------------------------------- | ------------------ |
| **Real-Time** | Monitor as predictions happen (e.g., alerts) | Prometheus, Arize  |
| **Batch**     | Daily/weekly analysis on logs/data snapshots | Evidently, WhyLogs |

---

## Best Practices

* Set alert thresholds for key metrics
* Monitor training and inference environments separately
* Log input data + predictions for traceability
* Use shadow mode to test new models quietly before replacing live ones
* Incorporate monitoring into your CI/CD pipeline

---

## Summary
Monitoring ensures that your deployed ML models:

* Stay healthy over time
* Continue adding business value
* Remain fair, accurate, and robust

> Think of monitoring as continuous feedback from production to improve your model lifecycle.

---

## Resources
* [Evidently AI Docs](https://docs.evidentlyai.com/)
* [Prometheus Monitoring Guide](https://prometheus.io/docs/introduction/overview/)
* [Seldon Alibi Detect](https://docs.seldon.io/projects/alibi-detect/)
* [Arize AI Monitoring](https://arize.com/)


