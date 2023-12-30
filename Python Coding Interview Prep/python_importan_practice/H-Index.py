"""
Given an array of integers citations where citations[i] is the number of citations a researcher received for their ith paper, return the researcher's h-index.

According to the definition of h-index on Wikipedia: The h-index is defined as the maximum value of h such that the given researcher has published at least h papers that have each been cited at least h times.



Example 1:

Input: citations = [3,0,6,1,5]
Output: 3
Explanation: [3,0,6,1,5] means the researcher has 5 papers in total and each of them had received 3, 0, 6, 1, 5 citations respectively.
Since the researcher has 3 papers with at least 3 citations each and the remaining two with no more than 3 citations each, their h-index is 3.
Example 2:

Input: citations = [1,3,1]
Output: 1


Constraints:

n == citations.length
1 <= n <= 5000
0 <= citations[i] <= 1000
"""
from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)  # Sort in non-decreasing order in reverse.
        h_index = 0

        for i, citation in enumerate(citations):
            if i + 1 <= citation:
                h_index = i + 1
            else:
                break

        return h_index


# Example usage
if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    citations1 = [3, 0, 6, 1, 5]
    result1 = solution.hIndex(citations1)
    print(result1)  # Expected output: 3

    # Test case 2
    citations2 = [1, 3, 1]
    result2 = solution.hIndex(citations2)
    print(result2)  # Expected output: 1
