"""
According to Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

The board is made up of an m x n grid of cells, where each cell has an initial state: live (represented by a 1) or dead (represented by a 0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):

Any live cell with fewer than two live neighbors dies as if caused by under-population.
Any live cell with two or three live neighbors lives on to the next generation.
Any live cell with more than three live neighbors dies, as if by over-population.
Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
The next state is created by applying the above rules simultaneously to every cell in the current state, where births and deaths occur simultaneously. Given the current state of the m x n grid board, return the next state.



Example 1:


Input: board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
Output: [[0,0,0],[1,0,1],[0,1,1],[0,1,0]]
Example 2:


Input: board = [[1,1],[1,0]]
Output: [[1,1],[1,1]]


Constraints:

m == board.length
n == board[i].length
1 <= m, n <= 25
board[i][j] is 0 or 1.


Follow up:

Could you solve it in-place? Remember that the board needs to be updated simultaneously: You cannot update some cells first and then use their updated values to update other cells.
In this question, we represent the board using a 2D array. In principle, the board is infinite, which would cause problems when the active area encroaches upon the border of the array (i.e., live cells reach the border). How would you address these problems?
"""
from typing import List


class Solution:
    def gameOfLife(self, board: List[List[int]) -> None:
        m, n = len(board), len(board[0])

        # Helper function to count live neighbors
        def countLiveNeighbors(row, col):
            live_neighbors = 0
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]
            for dr, dc in directions:
                r, c = row + dr, col + dc
                if 0 <= r < m and 0 <= c < n and (board[r][c] == 1 or board[r][c] == -1):
                    live_neighbors += 1
            return live_neighbors

        # Update the board based on the rules
        for i in range(m):
            for j in range(n):
                live_neighbors = countLiveNeighbors(i, j)

                if board[i][j] == 1:
                    if live_neighbors < 2 or live_neighbors > 3:
                        # Cell dies
                        board[i][j] = -1
                else:
                    if live_neighbors == 3:
                        # Cell becomes alive
                        board[i][j] = 2

        # Restore the board values
        for i in range(m):
            for j in range(n):
                if board[i][j] == 2:
                    board[i][j] = 1
                elif board[i][j] == -1:
                    board[i][j] = 0

# Create a Solution instance
solution = Solution()

# Test cases
board1 = [[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]]
board2 = [[1, 1], [1, 0]]

solution.gameOfLife(board1)
solution.gameOfLife(board2)

for row in board1:
    print(row)

for row in board2:
    print(row)

