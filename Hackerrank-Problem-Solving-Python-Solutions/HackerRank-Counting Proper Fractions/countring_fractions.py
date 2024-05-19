"""
Problem: Count Perfect Fractions

Problem Description:

A perfect fraction is a fraction where the numerator (n) and denominator (d) are coprime 
(i.e., their greatest common divisor is 1). Given a positive integer `d`, 
your task is to count the number of perfect fractions where the denominator is less than or equal to `d`.

Write a function `count_perfect_fractions(d)` that takes 
a positive integer `d` as input and returns the count of perfect fractions 
where the denominator is less than or equal to `d`.

Input Format:

- The input consists of a single line containing a single integer `d` (1 ≤ d ≤ 10^5), 
representing the upper limit for the denominators of the perfect fractions.

Output Format:

- Print a single integer representing the count of perfect fractions 
where the denominator is less than or equal to `d`.

Sample Input:

```
5
```

Sample Output:

```
11
```

Explanation:

For `d = 5`, the perfect fractions with denominators less than or equal to 5 are:

- 1/2
- 1/3
- 2/3
- 1/4
- 3/4
- 1/5
- 2/5
- 3/5
- 4/5
- 1/6
- 5/6

Therefore, the output is 11.
"""

# count all proper fractions from an int
def count_proper_fractions(d):
    # Initialize count variable to store the count of proper fractions
    count = 0
    
    # Iterate over each denominator from 2 to d
    for denom in range(2, d + 1):
        # Iterate over each numerator from 1 to denom-1
        for numer in range(1, denom):
            # Check if the greatest common divisor of numerator and denominator is 1
            if gcd(numer, denom) == 1:
                # If they are coprime, increment the count of proper fractions
                count += 1
    
    # Return the count of proper fractions
    return count

def gcd(a, b):
    # Compute the greatest common divisor using Euclid's algorithm
    while b != 0:
        a, b = b, a % b
    return a

d = 5
result = count_proper_fractions(d)
print(result)
