"""
Let’s check whether a sequence a0 , a1 , . . . , an≠1 (1 ˛ ai ˛ 109 ) contains a contiguous subse-
quence whose sum of elements equals s. For example, in the following sequence we are looking
for a subsequence whose total equals s = 12.
a0 a1 a2 a3 a4 a5 a6
6 2 7 4 1 3 6
Each position of the caterpillar will represent a different contiguous subsequence in which
the total of the elements is not greater than s. Let’s initially set the caterpillar on the first
element. Next we will perform the following steps:
• if we can, we move the right end (f ront) forward and increase the size of the caterpillar;
• otherwise, we move the left end (back) forward and decrease the size of the caterpillar.
In this way, for every position of the left end we know the longest caterpillar that covers
elements whose total is not greater than s. If there is a subsequence whose total of elements
equals s, then there certainly is a moment when the caterpillar covers all its elements.
"""
from typing import List


def caterpillar_method(array, target_sum):
    """
    Checks if there exists a contiguous subarray with a given sum using the Caterpillar method.

    :param array: List of integers
    :param target_sum: Target sum to find in the contiguous subarray
    :return: True if a contiguous subarray with the target sum exists, False otherwise
    """
    # Length of the input array
    n = len(array)
    # Initializing pointers for the caterpillar method
    front, total = 0, 0

    # Iterate through the array from the back pointer
    for back in range(n):
        # Move the front pointer until the total sum exceeds or equals the target sum
        while front < n and total + array[front] <= target_sum:
            total += array[front]
            front += 1
        # Check if the total sum matches the target sum
        if total == target_sum:
            return True
        # Adjust the total sum by subtracting the element at the back pointer
        total -= array[back]
    
    # If no contiguous subarray with the target sum is found, return False
    return False

            