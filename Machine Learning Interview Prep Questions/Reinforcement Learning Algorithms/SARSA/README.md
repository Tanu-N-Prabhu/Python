# SARSA from Scratch – Reinforcement Learning in GridWorld

This repository contains a **from-scratch implementation of the SARSA algorithm** (State-Action-Reward-State-Action) using only NumPy and basic Python constructs. It teaches reinforcement learning principles through a 4x4 GridWorld environment.

---

## What is SARSA?

SARSA is an **on-policy temporal-difference control algorithm** in reinforcement learning. It updates the action-value function (`Q`) using the action actually taken, based on the current policy.

### SARSA Update Rule

$$[
Q(s_t, a_t) \leftarrow Q(s_t, a_t) + \alpha \left[ r_{t+1} + \gamma \cdot Q(s_{t+1}, a_{t+1}) - Q(s_t, a_t) \right]
]$$

---

## Environment

- A simple **4x4 GridWorld**
- Start: top-left cell (state 0)
- Goal: bottom-right cell (state 15)
- Reward: `-1` for every move, `+10` for reaching the goal
- Agent can move: Up, Right, Down, Left

---

## File Structure

```bash
├── sarsa.ipynb       # Main Jupyter notebook with implementation and explanations
└── README.md         # This file
```

---

## How It Works
- Initialize Q-table to zeros
- Choose actions using ε-greedy policy
- Update Q-values using the SARSA update rule
- Repeat for multiple episodes
- Print the learned policy using arrows

---

## Hyperparameters

| Parameter       | Value |
| --------------- | ----- |
| Episodes        | 500   |
| Learning rate   | 0.1   |
| Discount factor | 0.99  |
| Epsilon         | 0.1   |

---

## Sample Output

```
Learned Policy (SARSA):
[['→' '→' '↓' '↓']
 ['↑' '→' '↓' '↓']
 ['↑' '→' '→' '↓']
 ['↑' '→' '→' '🏁']]
```

---

Legend:
- ↑ = Up
- → = Right
- ↓ = Down
- ← = Left
- 🏁 = Goal


---

## Dependencies
- Python 3.x
- NumPy

You can install NumPy via:

```
pip install numpy
```

---

## Educational Use
This repo is ideal for
- Students learning reinforcement learning
- Educators needing a clean, minimal example
- Anyone building RL intuition from scratch

---

## References
- Sutton & Barto: _Reinforcement Learning_ - An Introduction
- OpenAI Gym (for advanced users and environments)

---

## Contributions
Feel free to fork, experiment, and submit pull requests to improve this notebook or adapt it to more complex environments, such as CliffWalking or FrozenLake.

---

## License
MIT License, Use freely with attribution.
