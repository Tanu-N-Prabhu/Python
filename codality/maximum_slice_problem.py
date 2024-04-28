"""
Let’s define a problem relating to maximum slices. You are given a sequence of n integers
a0 , a1 , . . . , a n-1 and the task is to find the slice with the largest sum. More precisely, we are
looking for two indices p, q such that the total ap + ap+1 + . . . + aq is maximal. We assume
that the slice can be empty and its sum equals 0.

a0, a1, a2, a3, a4, a5, a6
5, -7, 3, 5, -2, 4, -1

In the picture above, the slice with the largest sum is 3,5,-2,4. The sum of this slice
equals 10 and there is no slice with a larger sum. Notice that the slice we are looking for may
contain negative integers, as shown above.
"""
from typing import List


def max_slice_sum(integers: List[int]) -> int:
    """
    Finds the maximum slice sum in a list of integers.

    :param integers: List of integers
    :return: Maximum slice sum
    """
    # `max_ending_here` represents the maximum sum of a slice ending 
    # at the current position during the iteration through the list of integers.

    # `max_slice` represents the overall maximum sum of any slice 
    # encountered so far during the iteration through the list of integers.
    max_ending_here = max_slice = 0
    # max_ending_here tracks the maximum slice ending at the current position

    for num in integers:
        # Update max_ending_here by adding the current element
        max_ending_here = max(0, max_ending_here + num)
        # Update max_slice with the current maximum slice
        max_slice = max(max_slice, max_ending_here)

    return max_slice


if __name__ == "__main__":
    A = [5, -7, 3, 5, -2, 4, -1]
    print(A)
    print(solution(A))
    A = [3, 2, -6, 4, 0]
    print(A)
    print(solution(A))
