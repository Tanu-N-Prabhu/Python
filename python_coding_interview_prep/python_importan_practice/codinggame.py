import sys
import math
from contextlib import redirect_stdout


def compute_closest_to_zero(ts):
    """
    Computes the closest value to zero from a given list of integers.

    Parameters:
    ts (List[int]): A list of integers representing the values.

    Returns:
    int: The value closest to zero.

    Explanation:
    - If the list is not empty and contains at most 10000 elements:
        - Find the element closest to zero using the min function and a lambda function.
        - Check if the closest element is negative and its absolute value exists in the list.
        - Return the absolute value if it exists; otherwise, return the closest element.
    - If the list is empty or exceeds 10000 elements, return 0.
    """
    if len(ts) > 0 and len(ts) <= 10000:
        # Find the element closest to zero
        #  iterating over the indices of ts, calculating the absolute difference between each element 
        # and zero, and then selecting the index corresponding to the minimum absolute difference
        temp = ts[min(range(len(ts)), key=lambda i: abs(ts[i] - 0))]
        if temp < 0 and abs(temp) in ts:
            return abs(temp)
        else:
            return temp
    return 0


# Ignore and do not change the code below
def main():
    # pylint: disable=C,W
    n = int(input())
    ts = [int(i) for i in input().split()]
    with redirect_stdout(sys.stderr):
        solution = compute_closest_to_zero(ts)
    print(solution)


if __name__ == "__main__":
    main()
