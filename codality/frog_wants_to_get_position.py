"""
Problem: A small frog wants to get from position 0 to k (1 ¬ k ¬ 10 000). The frog can
jump over any one of n fixed distances s0 , s1 , . . . , sn−1 (1 ¬ si ¬ k). The goal is to count the
number of different ways in which the frog can jump to position k. To avoid overflow, it is
sufficient to return the result modulo q, where q is a given number.
We assume that two patterns of jumps are different if, in one pattern, the frog visits
a position which is not visited in the other pattern.

Solution O(n · k): The task can be solved by using dynamic programming. Let’s create an
array dp consisting of k elements, such that dp[j] will be the number of ways in which the
frog can jump to position j.
2We update consecutive cells of array dp. There is exactly one way for the frog to jump to
position 0, so dp[0] = 1. Next, consider some position j > 0.
The number of ways in which the frog can jump to position j with a final jump of si is
dp[j − si ]. Thus, the number of ways in which the frog can get to position j is increased by
the number of ways of getting to position j − si , for every jump si .
0
j−s1
j−s0
j
More precisely, dp[j] is increased by the value of dp[j − si ] (for all si ¬ j) modulo q.
"""
from typing import List


def frog_jump_combinations(stones: List[int], target_distance: int, modulo: int) -> int:
    """
    Computes the number of ways the frog can reach a target distance using given stones.

    :param stones: List of distances the frog can jump
    :param target_distance: Target distance the frog needs to reach
    :param modulo: Modulo value to keep the result within bounds
    :return: Number of ways the frog can reach the target distance
    """
    n = len(stones)
    # Initialize dynamic programming array with 1 at index 0
    # [1, 0, 0, 0, 0, 0, 0............]
    dp = [1] + [0] * target_distance

    # Iterate through each distance from 1 to target_distance
    for j in range(1, target_distance + 1):
        # Iterate through each stone's distance
        for i in range(n):
            # Check if the current stone's distance is less than or equal to the current distance
            if stones[i] <= j:
                # Update dp[j] by adding the previous dp[j] with dp[j - stones[i]]
                dp[j] = (dp[j] + dp[j - stones[i]]) % modulo

    return dp[target_distance]


if __name__ == "__main__":
    print(frog_jump_combinations([1, 3, 5, 8, 12, 17], 20, 1000000007))
    print(frog_jump_combinations([1, 3, 5, 8, 12, 17], 20, 10))
    print(frog_jump_combinations([1, 3, 5, 8, 12, 17], 20, 1))
