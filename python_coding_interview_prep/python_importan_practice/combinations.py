"""
Given two integers n and k, return all possible combinations of k numbers chosen from the range [1, n].

You may return the answer in any order.

Example 1:

Input: n = 4, k = 2
Output: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
Explanation: There are 4 choose 2 = 6 total combinations.
Note that combinations are unordered, i.e., [1,2] and [2,1] are considered to be the same combination.
Example 2:

Input: n = 1, k = 1
Output: [[1]]
Explanation: There is 1 choose 1 = 1 total combination.


Constraints:

1 <= n <= 20
1 <= k <= n
"""
from typing import List

class Solution:
    """
    Backtracking solution.
    Time complexity: O(n^k)
    Space complexity: O(k)
    where n is the number of elements in the input array and k is the desired length of the combinations.
    """
    def combine(self, n: int, k: int) -> List[List[int]]:

        # Define a helper function for backtracking
        def backtrack(start, current_combination):
            # If the current combination has reached the desired length, append it to the result
            if len(current_combination) == k:
                result.append(current_combination[:])
                return
            # Iterate over possible elements to include in the combination
            for i in range(start, n + 1):
                # Add the current element to the combination
                current_combination.append(i)
                # Recursively call backtrack with the next start index and updated combination
                backtrack(i + 1, current_combination)
                # Backtrack: remove the last added element to explore other combinations
                current_combination.pop()

        # Initialize an empty list to store the resulting combinations
        result = []
        # Start backtracking from index 1 with an empty initial combination
        backtrack(1, [])
        # Return the resulting combinations
        return result



# Example usage
n = 4
k = 2
solution = Solution()
result = solution.combine(n, k)
print(result)  # Output: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
