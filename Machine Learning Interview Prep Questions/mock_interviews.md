# Mock Interview Questions & Scenarios

This section is designed to simulate real interview environments with scenario-based, open-ended, and coding prompts that help you think like a practitioner.

Use these questions for:
- Solo practice
- Peer interviews
- Mock sessions with mentors

---

## Scenario-Based Questions

These require a structured, end-to-end answer. Think like an ML engineer or data scientist explaining your approach.

### Scenario 1: Customer Churn Prediction
> You're given a dataset from a telecom company. Your task is to predict whether a customer is likely to cancel their subscription.

**Practice Prompts:**
- What features would you expect in the dataset?
- How would you handle class imbalance?
- Which model(s) would you use and why?
- How would you evaluate the model?

---

### Scenario 2: Medical Diagnosis Model
> You are building a model to detect diabetes from patient health records.

**Practice Prompts:**
- What ethical concerns might arise?
- How would you deal with missing or sensitive data?
- Would you prioritize precision or recall in this case?
- How would you explain the model to a doctor?

---

### Scenario 3: Image Classification for a Startup
> A startup asks you to build an image classifier for product defect detection.

**Practice Prompts:**
- Would you train from scratch or use transfer learning?
- How would you collect or augment image data?
- What metrics would be most important?
- How would you deploy this model in production?

---

## Live Coding Prompts

Use these in a Colab notebook or whiteboard-style session.

### Prompt 1: Implement Logistic Regression from Scratch
- No libraries except NumPy.
- Include sigmoid, cost function, gradient descent.

### Prompt 2: Clean and Prepare the Titanic Dataset
- Handle missing values
- Encode categorical features
- Scale numeric features
- Output a ready-to-model DataFrame

### Prompt 3: Evaluate a Model with Precision, Recall, and F1
- Given a list of predictions and true labels, calculate evaluation metrics without `sklearn`.

---

## Role Play: Explain to a Non-Technical Stakeholder

These simulate explaining complex ideas to managers or clients.

### Prompt 1:
> "Explain how Random Forest works to someone without a technical background."

### Prompt 2:
> "Your accuracy dropped after deploying the model. How would you explain and address it with the product team?"

### Prompt 3:
> "The CEO wants to use your model in a highly regulated industry. What concerns would you raise?"

---

## Tips for Mock Interviews

- **Time yourself** - aim for 2–3 minutes per structured answer.
- **Speak out loud** - practice thinking and explaining clearly.
- **Ask clarifying questions** - interviewers like to see thoughtful analysis.
- **Use the STAR format** for behavioral prompts.

---

> **Next Steps:**  
Use [`coding_questions.ipynb`](./coding_questions.ipynb) to practice implementation-based exercises in Colab.
