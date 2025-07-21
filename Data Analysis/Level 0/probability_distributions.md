
# Probability & Distributions

_This section introduces you to the fundamentals of probability and common statistical distributions used in data analysis and data science._

---

## What is Probability?

Probability is the measure of the likelihood that an event will occur. It ranges between **0** (an impossible event) and **1** (a certain event).

### Basic Terms:
- **Experiment**: An action that leads to one or more outcomes (e.g., flipping a coin).
- **Sample Space (S)**: Set of all possible outcomes.
- **Event (E)**: A subset of the sample space.

### Formula:
```python
P(E) = Number of favorable outcomes / Total number of possible outcomes
```

### Example:
```python
# Probability of getting a 'Head' in a coin toss
P_Head = 1 / 2  # 0.5
```

---

## Types of Probability

### 1. **Theoretical Probability**
Based on reasoning or math.
```python
P(rolling a 3 on a fair die) = 1/6
```

### 2. **Experimental Probability**
Based on actual experiments or historical data.
```python
P(E) = Number of times event occurred / Total trials
```

---

## Types of Distributions

### 1. **Uniform Distribution**
All outcomes are equally likely.
- Example: Rolling a fair die (1–6)
- Probability of any value = 1/6

### 2. **Binomial Distribution**
Used when there are exactly two outcomes (success/failure) across **n** trials.
- Parameters: `n` (number of trials), `p` (probability of success)
```python
from scipy.stats import binom
binom.pmf(k=2, n=5, p=0.5)
```

### 3. **Normal Distribution (Gaussian)**
A symmetric, bell-shaped distribution defined by its **mean** (µ) and **standard deviation** (σ).
- Many real-world datasets follow this.
```python
from scipy.stats import norm
norm.pdf(x=0, loc=0, scale=1)  # Standard normal distribution
```

### 4. **Poisson Distribution**
Used to model the number of times an event occurs in a fixed interval of time or space.
- Parameter: λ (average rate)
```python
from scipy.stats import poisson
poisson.pmf(k=3, mu=2)
```

---

## Probability in Python

```python
import random

# Simulate a coin toss
coin = random.choice(['Heads', 'Tails'])

# Simulate a dice roll
dice = random.randint(1, 6)
```

---

## Why Probability & Distributions Matter

- Essential for understanding data variability
- Used in hypothesis testing and inferential statistics
- Foundation for machine learning algorithms

---

## Practice Exercise

1. Simulate 1000 coin tosses and calculate the experimental probability.
2. Plot the normal distribution curve using `matplotlib`.
3. Use `scipy.stats` to compute binomial and Poisson probabilities.

---

## Summary

| Concept          | Key Idea                                      |
|------------------|-----------------------------------------------|
| Probability       | Likelihood of an event occurring              |
| Uniform           | Equal chance for all outcomes                 |
| Binomial          | Two outcomes over multiple trials             |
| Normal            | Bell-shaped distribution (mean & variance)   |
| Poisson           | Frequency of events in a fixed interval       |

---

