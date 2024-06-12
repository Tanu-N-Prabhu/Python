"""
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step


Constraints:

1 <= n <= 45
"""


class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        # Initialize the DP array with 0s
        dp = [0] * (n + 1)
        # Fill the first two positions with 1s
        dp[1] = 1
        dp[2] = 2
        
        # Fill the DP array from 3rd to end 
        for i in range(3, n + 1):
            # Recurrence relation for the DP array
            dp[i] = dp[i - 1] + dp[i - 2]
            print(dp)

        return dp[n]


# Test code
solution = Solution()

# Test case 1
n1 = 2
result1 = solution.climbStairs(n1)
print("Test case 1 result:", result1)  # Expected output: 2

# Test case 2
n2 = 3
result2 = solution.climbStairs(n2)
print("Test case 2 result:", result2)  # Expected output: 3

