"""
Given a triangle array, return the minimum path sum from top to bottom.

For each step, you may move to an adjacent number of the row below. More formally, if you are on index i on the current row, you may move to either index i or index i + 1 on the next row.



Example 1:

Input: triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
Output: 11
Explanation: The triangle looks like:
   2
  3 4
 6 5 7
4 1 8 3
The minimum path sum from top to bottom is 2 + 3 + 5 + 1 = 11 (underlined above).
Example 2:

Input: triangle = [[-10]]
Output: -10


Constraints:

1 <= triangle.length <= 200
triangle[0].length == 1
triangle[i].length == triangle[i - 1].length + 1
-104 <= triangle[i][j] <= 104


Follow up: Could you do this using only O(n) extra space, where n is the total number of rows in the triangle?
"""


class Solution:
    def minimumTotal(self, triangle: List[List[int]) -> int:
        n = len(triangle)

        # Start from the second-to-last row and work your way up.
        for i in range(n - 2, -1, -1):
            for j in range(len(triangle[i])):
                triangle[i][j] += min(triangle[i + 1][j], triangle[i + 1][j + 1])

        return triangle[0][0]


# Test code
solution = Solution()

# Test case 1
triangle1 = [[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]
result1 = solution.minimumTotal(triangle1)
print("Test case 1 result:", result1)  # Expected output: 11

# Test case 2
triangle2 = [[-10]]
result2 = solution.minimumTotal(triangle2)
print("Test case 2 result:", result2)  # Expected output: -10

