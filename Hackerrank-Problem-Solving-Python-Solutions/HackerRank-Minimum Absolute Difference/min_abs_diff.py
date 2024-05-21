"""
### HackerRank Problem Statement: Minimum Absolute Difference in an Array

**Objective:**

Given an array of integers, find and print the minimum absolute difference 
between any two elements in the array.

**Function Description:**

Complete the function `minimum_absolute_difference` in the editor below. 
The function must return an integer representing the minimum absolute difference 
between any two elements in the array.

`minimum_absolute_difference` has the following parameter(s):
- `arr`: an array of integers.

**Input Format:**

The first line contains a single integer `n`, the number of elements in the array.
The second line contains `n` space-separated integers `arr[i]` (1 ≤ i ≤ n).

**Constraints:**

- 2 ≤ n ≤ 10^5
- -10^9 ≤ arr[i] ≤ 10^9

**Output Format:**

Print the minimum absolute difference between any two elements in the array.

**Sample Input 1:**

```
5
3 8 15 1 6
```

**Sample Output 1:**

```
2
```

**Explanation:**

The sorted array is `[1, 3, 6, 8, 15]`. The minimum absolute difference is 
between the elements `1` and `3`, which is `2`.

**Sample Input 2:**

```
3
-10 7 8
```

**Sample Output 2:**

```
1
```

**Explanation:**

The sorted array is `[-10, 7, 8]`. The minimum absolute difference is 
between the elements `7` and `8`, which is `1`.


"""

def minimum_absolute_difference(arr):
    # Sort the array in ascending order
    arr.sort()
    
    # Initialize the minimum difference with a very large number
    min_diff = float('inf')
    
    # Iterate through the array to find the minimum absolute difference
    for i in range(len(arr) - 1):
        # Calculate the absolute difference between consecutive elements
        diff = abs(arr[i] - arr[i + 1])
        
        # Update the minimum difference if a smaller one is found
        if diff < min_diff:
            min_diff = diff
    
    # Return the minimum absolute difference found
    return min_diff

# Example usage:
arr = [3, 8, 15, 1, 6]
print(minimum_absolute_difference(arr))  # Output: 2
