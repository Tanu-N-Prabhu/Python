"""
The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

Given an integer n, return the number of distinct solutions to the n-queens puzzle.



Example 1:


Input: n = 4
Output: 2
Explanation: There are two distinct solutions to the 4-queens puzzle as shown.
Example 2:

Input: n = 1
Output: 1


Constraints:

1 <= n <= 9
"""
class Solution:
    def totalNQueens(self, n: int) -> int:
        def is_safe(row, col, queens, n):
            for prev_row in range(row):
                if queens[prev_row] == col or \
                   queens[prev_row] - prev_row == col - row or \
                   queens[prev_row] + prev_row == col + row:
                    return False
            return True

        def solve(row):
            if row == n:
                nonlocal count
                count += 1
                return
            for col in range(n):
                if is_safe(row, col, queens, n):
                    queens[row] = col
                    solve(row + 1)
                    queens[row] = -1

        queens = [-1] * n
        count = 0
        solve(0)
        return count

# Example usage:
n = 4
solution = Solution()
result = solution.totalNQueens(n)
print(result)
