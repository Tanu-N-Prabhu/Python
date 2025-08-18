# Deep Q-Network (DQN)

This project demonstrates a **Deep Q-Network (DQN)** applied to the
**CartPole-v1** environment from OpenAI Gym.

------------------------------------------------------------------------

## What is DQN?

Deep Q-Network (DQN) is a reinforcement learning algorithm that uses a
**neural network** to approximate the Q-function.
It combines Q-Learning with deep learning to handle large and complex
state spaces.

------------------------------------------------------------------------

## Key Concepts

1.  **Environment**
    -   We use `CartPole-v1` where the agent must balance a pole on a
        cart.
2.  **Q-Network**
    -   A small feedforward neural network predicts Q-values for each
        action.
3.  **Epsilon-Greedy Policy**
    -   Balances exploration (random moves) and exploitation (choosing
        the best known action).
4.  **Experience Replay**
    -   Stores experiences (state, action, reward, next_state, done) in
        memory.
    -   Randomly samples mini-batches to break the correlation between
        consecutive experiences.
5.  **Target Network**
    -   A copy of the Q-network that updates slowly for stability.

------------------------------------------------------------------------

## How Training Works

1.  Initialize Q-network and target network.
2.  For each episode:
    -   Start at the initial state.
    -   Choose actions using epsilon-greedy policy.
    -   Store experiences in memory.
    -   Train the Q-network using mini-batches.
    -   Occasionally update the target network.
3.  Repeat until the agent learns to balance the pole.

------------------------------------------------------------------------

## Requirements

Install the following libraries before running the notebook:

``` bash
pip install torch gym numpy matplotlib
```

------------------------------------------------------------------------

## Running the Code

1.  Open the notebook.
2.  Run all cells in order.
3.  Watch the agent learn to balance the pole over episodes.

------------------------------------------------------------------------

## Output

-   During training, you will see:
    -   Episode number
    -   Total reward achieved
    -   Current epsilon value

As training progresses, rewards increase as the agent gets better.

------------------------------------------------------------------------

## Why DQN is Important?

-   Solves environments with large/continuous states.
-   Forms the foundation for advanced RL methods (Double DQN, Dueling
    DQN, etc.).
-   Widely used in robotics, games (Atari, Go), and decision-making
    systems.

------------------------------------------------------------------------

## References

-   [DeepMind DQN Paper (2015)](https://www.nature.com/articles/nature14236)
-   [OpenAI Gym](https://www.gymlibrary.dev/)
