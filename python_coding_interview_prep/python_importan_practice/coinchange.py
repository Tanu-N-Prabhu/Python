"""
You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.


Example 1:

Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1
Example 2:

Input: coins = [2], amount = 3
Output: -1
Example 3:

Input: coins = [1], amount = 0
Output: 0


Constraints:

1 <= coins.length <= 12
1 <= coins[i] <= 231 - 1
0 <= amount <= 104
"""
from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Initialize the dp array with a large value
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0  # Base case, 0 coins needed for amount 0

        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] = min(dp[i], dp[i - coin] + 1)

        return dp[amount] if dp[amount] != float('inf') else -1


# Test code
solution = Solution()

# Test case 1
coins1 = [1, 2, 5]
amount1 = 11
result1 = solution.coinChange(coins1, amount1)
print("Test case 1 result:", result1)  # Expected output: 3

# Test case 2
coins2 = [2]
amount2 = 3
result2 = solution.coinChange(coins2, amount2)
print("Test case 2 result:", result2)  # Expected output: -1

# Test case 3
coins3 = [1]
amount3 = 0
result3 = solution.coinChange(coins3, amount3)
print("Test case 3 result:", result3)  # Expected output: 0

