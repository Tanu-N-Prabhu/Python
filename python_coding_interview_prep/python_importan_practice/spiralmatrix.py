"""
Given an m x n matrix, return all elements of the matrix in spiral order.



Example 1:


Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]
Example 2:


Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]


Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 10
-100 <= matrix[i][j] <= 100
"""

from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]) -> List[int]:
        result = []
        while matrix:
            result += matrix[0]  # Append the first row
            matrix = list(zip(*matrix[1:]))[::-1]  # Rotate the matrix clockwise
        return result

# Create a Solution instance
solution = Solution()

# Test cases
matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix2 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]

result1 = solution.spiralOrder(matrix1)  # Expected output: [1, 2, 3, 6, 9, 8, 7, 4, 5]
result2 = solution.spiralOrder(matrix2)  # Expected output: [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]

print(result1)
print(result2)

