
"""
Problem: Efficient Janitor

Problem Description:

A janitor has to move a list of weights, with each weight being a positive real number. 
However, the janitor can only carry up to 3.0 units of weight at a time. 
To minimize the number of trips, the janitor wants to carry as many weights as possible 
in each trip without exceeding the weight limit.

Write a function `efficient_janitor(weights)` that takes a list of weights as input and returns the minimum number of trips 
the janitor needs to make.

nput Format:

- The input consists of a single line containing a space-separated list of weights, 
where each weight (w) is a positive real number (0 < w ≤ 3.0).
- The length of the list of weights (n) is at most 10^5.

Output Format:

- Print a single integer representing the minimum number of trips the janitor needs to make.

Sample Input:

```
1.01 1.99 2.5 1.5 1.01
```

Sample Output:

```
2
```

Explanation:

The janitor can make two trips:

1. Trip 1: Carrying weights 1.01, 1.99, and 1.5 (total = 4.5).
2. Trip 2: Carrying weights 2.5 and 1.01 (total = 3.51).

This is the minimum number of trips required.
"""

# Efficient janitor
def efficient_janitor(weights):
    weights.sort()
    trips = 0
    # left pointer start from first one
    left = 0
    # right pointer start from last one
    right = len(weights) - 1
    
    # till both side pointer trying to cross each other
    while left <= right:
        # can carry only upto 3.0
        if weights[left] + weights[right] <= 3.0:
            # taking one after another sorted weights
            left += 1
        right -= 1
        trips += 1
    
    return trips


# Example usage:
weights = [1.01, 1.99, 2.5, 1.5, 1.01]
print(efficient_janitor(weights))
