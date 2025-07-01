# Model Deployment in Machine Learning

Once a model is trained and evaluated, it needs to be deployed so others can **interact with it via applications or APIs**. This process is called **model deployment**.

---

## Why Deploy a Model?

- Make predictions on real-world data (e.g., via web apps, APIs)
- Enable integration with other systems (e.g., CRMs, sensors)
- Deliver ML value to end-users or business operations

---

## Common Deployment Strategies

| Method               | Description                                               | Best For                  |
|----------------------|-----------------------------------------------------------|---------------------------|
| **REST API**         | Expose model via HTTP endpoints                           | Web apps, microservices   |
| **Batch Inference**  | Run predictions on large batches at intervals             | Offline processing        |
| **Streaming Inference** | Predict in real-time from data streams                 | IoT, finance, live feeds  |
| **Edge Deployment**  | Deploy model on mobile or IoT devices                     | Low-latency or offline use|
| **Serverless**       | On-demand model inference using cloud functions           | Lightweight workloads     |

---

## Tools & Frameworks for Deployment

| Tool/Framework     | Purpose                               | Notes                            |
|-------------------|----------------------------------------|----------------------------------|
| **Flask/FastAPI** | Lightweight Python APIs                | Simple RESTful model serving     |
| **Docker**        | Containerize model + dependencies      | Run anywhere consistently        |
| **TensorFlow Serving** | Serve TensorFlow models at scale | Production-grade deployment      |
| **TorchServe**     | Serve PyTorch models                  | Custom handlers supported        |
| **ONNX Runtime**   | Optimized serving for multiple frameworks | Convert + speed up inference |
| **MLflow**         | Track, package, and deploy models     | Part of end-to-end ML workflow   |
| **Seldon Core** / **KServe** | Kubernetes-native deployment | Advanced MLOps & monitoring       |

---

## Example: Deploy with FastAPI

### Save Your Model
```python
import joblib
joblib.dump(model, "model.pkl")
```

---

## Create API (main.py)

```python
from fastapi import FastAPI
import joblib
import numpy as np

app = FastAPI()
model = joblib.load("model.pkl")

@app.get("/")
def root():
    return {"message": "Model is ready!"}

@app.post("/predict/")
def predict(data: list):
    prediction = model.predict(np.array(data).reshape(1, -1))
    return {"prediction": int(prediction[0])}
```

---

## Run It

```python
uvicorn main:app --reload
```

---

## Optional: Dockerize It

```python
# Dockerfile
FROM python:3.10
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

---

## Production Considerations
* **Input validation** (e.g., Pydantic, Marshmallow)
* **Model versioning**
* **Scalability** (e.g., Gunicorn, Kubernetes)
* **Monitoring** (e.g., Prometheus, Grafana)
* **CI/CD pipelines** for auto-deploying new versions

---

## Summary
* Deployment makes your ML model usable in real-world applications.
* Start with simple REST APIs, then scale with containers or cloud-native tools.
* Keep performance, security, and versioning in mind from day one.

---

## Resources
* [FastAPI Docs](https://fastapi.tiangolo.com/)
* [MLflow Deployment Guide](https://mlflow.org/docs/latest/models.html)
* [TensorFlow Serving Guide](https://www.tensorflow.org/tfx/guide/serving)
* [ONNX Tutorials](https://onnx.ai/tutorials/)



  
