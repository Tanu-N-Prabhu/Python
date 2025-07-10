# Advanced Topics in Machine Learning

This section covers advanced ML concepts including deep learning, transfer learning, model deployment, and more. These topics are increasingly relevant in real-world AI applications and technical interviews.

---

## 1. Deep Learning

### Key Concepts:
- Subset of ML based on artificial neural networks with multiple layers.
- Learns hierarchical features directly from data.
- Requires large datasets and GPU/TPU support.

### Interview Questions:
- What is the architecture of a neural network?
- What are activation functions? Name a few.
- What is the vanishing gradient problem?
- How is deep learning different from traditional machine learning?

### Mini Case Study:
**Problem:** Classify images of handwritten digits (e.g. MNIST).  
**Solution:** Use a deep neural network (DNN) or convolutional neural network (CNN) to achieve high accuracy on image classification.

---

## 2. Transfer Learning

### Key Concepts:
- Reusing a pre-trained model on a new, related task.
- Common in image and NLP tasks.
- Saves training time and improves performance with less data.

### Interview Questions:
- What is transfer learning and when is it used?
- How do you fine-tune a pre-trained model?
- What is the difference between feature extraction and fine-tuning?

### Mini Case Study:
**Problem:** Classify plant diseases using a small labeled image dataset.  
**Solution:** Use a pre-trained CNN (like ResNet or EfficientNet) and fine-tune the last few layers on the plant images.

---

## 3. Model Deployment

### Key Concepts:
- Making a trained model available for real-time predictions or batch inference.
- Common tools: Flask, FastAPI, Docker, AWS SageMaker, TensorFlow Serving.

### Interview Questions:
- What are the steps in deploying a model?
- What’s the difference between batch and real-time inference?
- How do you monitor model performance after deployment?

### Mini Case Study:
**Problem:** Deploy a sentiment analysis model for a live chat support tool.  
**Solution:** Build a REST API using FastAPI, containerize with Docker, and host on a cloud platform.

---

## 4. Model Interpretability & Explainability

### Key Concepts:
- Understanding how a model makes decisions.
- Tools: SHAP, LIME, feature importance plots.

### Interview Questions:
- Why is interpretability important in ML?
- How do SHAP values work?
- What is the difference between global and local interpretability?

---

## 5. Hyperparameter Tuning

### Key Concepts:
- The process of optimizing model parameters that are not learned from data (e.g., learning rate, number of trees).
- Techniques: Grid Search, Random Search, Bayesian Optimization

### Interview Questions:
- What is the difference between parameters and hyperparameters?
- How does grid search compare to random search?
- What tools can automate hyperparameter tuning?

---

## 6. Model Monitoring & Drift

### Key Concepts:
- Monitoring deployed models for performance decay.
- Detecting **concept drift** (change in data distribution) and **data drift** (change in input features).

### Interview Questions:
- What is concept drift and how do you handle it?
- How can you set up monitoring for a deployed model?

---

## Summary Table

| Topic                     | Tools & Techniques                         |
|--------------------------|--------------------------------------------|
| Deep Learning            | TensorFlow, PyTorch, Keras, CNN, RNN       |
| Transfer Learning        | ResNet, BERT, Hugging Face Transformers    |
| Deployment               | Flask, FastAPI, Docker, AWS SageMaker      |
| Interpretability         | SHAP, LIME, Feature Importance             |
| Hyperparameter Tuning    | Grid Search, Random Search, Optuna         |
| Monitoring & Drift       | MLflow, Evidently AI, Prometheus           |

---

## Advanced Interview Questions

- How does a CNN differ from a fully connected network?
- When would you use transfer learning vs training from scratch?
- What are the challenges in deploying ML models in production?
- How do you handle models that degrade over time?
- What’s the difference between model explainability and interpretability?

---

> **Next Steps:**  
Check out [`behavioral_questions.md`](./behavioral_questions.md) to prepare for common project-based and HR-style interview questions.
