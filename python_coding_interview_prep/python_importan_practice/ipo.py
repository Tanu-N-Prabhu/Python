"""
Suppose LeetCode will start its IPO soon. In order to sell a good price of its shares to Venture Capital, LeetCode would like to work on some projects to increase its capital before the IPO. Since it has limited resources, it can only finish at most k distinct projects before the IPO. Help LeetCode design the best way to maximize its total capital after finishing at most k distinct projects.

You are given n projects where the ith project has a pure profit profits[i] and a minimum capital of capital[i] is needed to start it.

Initially, you have w capital. When you finish a project, you will obtain its pure profit and the profit will be added to your total capital.

Pick a list of at most k distinct projects from given projects to maximize your final capital, and return the final maximized capital.

The answer is guaranteed to fit in a 32-bit signed integer.



Example 1:

Input: k = 2, w = 0, profits = [1,2,3], capital = [0,1,1]
Output: 4
Explanation: Since your initial capital is 0, you can only start the project indexed 0.
After finishing it you will obtain profit 1 and your capital becomes 1.
With capital 1, you can either start the project indexed 1 or the project indexed 2.
Since you can choose at most 2 projects, you need to finish the project indexed 2 to get the maximum capital.
Therefore, output the final maximized capital, which is 0 + 1 + 3 = 4.
Example 2:

Input: k = 3, w = 0, profits = [1,2,3], capital = [0,1,2]
Output: 6


Constraints:

1 <= k <= 105
0 <= w <= 109
n == profits.length
n == capital.length
1 <= n <= 105
0 <= profits[i] <= 104
0 <= capital[i] <= 109
"""


import heapq

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        # Create a list of projects sorted by their capital requirements
        projects = sorted(zip(capital, profits))

        # Initialize a max-heap to store available profits
        available_profits = []

        # Iterate up to k projects
        for _ in range(k):
            # Add projects with capital less than or equal to current capital to the max-heap
            while projects and projects[0][0] <= w:
                capital, profit = projects.pop(0)
                heapq.heappush(available_profits, -profit)

            # If there are available profits, take the project with the maximum profit
            if available_profits:
                w -= heapq.heappop(available_profits)
            else:
                break

        return w


# Test cases
solution = Solution()

# Test Case 1
k1 = 2
w1 = 0
profits1 = [1, 2, 3]
capital1 = [0, 1, 1]
result1 = solution.findMaximizedCapital(k1, w1, profits1, capital1)
print(result1)  # Expected output: 4

# Test Case 2
k2 = 3
w2 = 0
profits2 = [1, 2, 3]
capital2 = [0, 1, 2]
result2 = solution.findMaximizedCapital(k2, w2, profits2, capital2)
print(result2)  # Expected output: 6
