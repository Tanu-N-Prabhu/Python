# 📘 `q_learning.ipynb` – Q-Learning from Scratch

This notebook demonstrates how to implement the **Q-Learning algorithm** from scratch using only NumPy and basic Python logic—no machine learning libraries or classes. It is designed to help students and interviewees understand the foundational principles of reinforcement learning by **building a working model step by step**.

---

## 📌 What is Q-Learning?

Q-Learning is a **model-free**, **off-policy**, **value-based** reinforcement learning algorithm. It teaches an agent how to act optimally in a Markov Decision Process (MDP) by learning the value of actions in states—without needing a model of the environment.

### 🧠 Bellman Equation (Q-Update Rule):
```
Q(s, a) ← Q(s, a) + α * [r + γ * max(Q(s′, a′)) − Q(s, a)]
```
- `s` = current state  
- `a` = action taken  
- `r` = reward received  
- `s′` = next state  
- `α` = learning rate  
- `γ` = discount factor  

---

## 🧱 Environment

- A **4×4 grid** world is used.
- The agent starts at the top-left corner `(0, 0)`.
- The goal is to reach the bottom-right corner `(3, 3)` with the **maximum reward**.
- Actions = Up, Down, Left, Right
- Rewards:
  - +1 for reaching the goal  
  - −0.01 for every other step (to encourage faster solutions)

---

## 🔁 Training Parameters

| Parameter         | Value          | Description |
|------------------|----------------|-------------|
| `episodes`       | 500            | Number of training episodes |
| `alpha`          | 0.1            | Learning rate |
| `gamma`          | 0.99           | Discount factor for future rewards |
| `epsilon`        | 1.0 → 0.01     | Exploration rate (decays each episode) |

---

## ✅ What You’ll Learn

- How Q-learning works behind the scenes  
- Why the **Q-table** matters and how it’s updated  
- Implementing ε-greedy exploration  
- Understanding the **trade-off between exploration and exploitation**  
- Visualizing the optimal policy using directional arrows  

---

## 🧭 Output

At the end of training, the agent learns the **optimal action** at each position in the grid. You will see a map like:

```
→ → → ↓  
↓ → ↓ ↓  
→ → ↓ ↓  
→ → → ✅
```

---

## 📂 Files

| File                          | Description |
|------------------------------|-------------|
| `q_learning.ipynb`           | Fully documented Q-Learning notebook with implementation from scratch |
| `README.md`                  | This file - explains theory, setup, and purpose |

---

## 🎓 Who Should Use This?

- Students preparing for ML/AI interviews  
- Beginners trying to understand reinforcement learning  
- Educators building curriculum materials  
- Developers exploring agent-based AI  
