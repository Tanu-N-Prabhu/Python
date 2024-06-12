"""
Finds the minimal subset A from an array arr such that:
    - Intersection of A and B (remaining elements) is null.
    - Union of A and B is equal to the original array.
    - Number of elements in A is minimal.
    - Sum of A's elements is greater than the sum of B's elements.
    - If multiple subsets exist, return the one with the maximal sum.

    Args:
        arr: An integer array.

    Returns:
        A list representing the subset A.
"""
import math
import os
import random
import re
import sys



#
# Complete the 'subsetA' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#


def subsetA(arr):
    total_sum = sum(arr)

    # Sort the array in descending order for efficient greedy approach
    arr.sort(reverse=True)

    # Initialize subset A and sum
    subset_a = []
    sum_a = 0

    # Iterate through the sorted array
    for num in arr:
        # Add element to subset A if it doesn't violate conditions
        if sum_a <= total_sum // 2:
            subset_a.append(num)
            sum_a += num

    subset_a.sort(reverse=False)
    return subset_a


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = []

    for _ in range(arr_count):
        arr_item = int(input().strip())
        arr.append(arr_item)

    result = subsetA(arr)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
