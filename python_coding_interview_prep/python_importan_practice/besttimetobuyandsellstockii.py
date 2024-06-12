"""
You are given an integer array prices where prices[i] is the price of a given stock on the ith day.

On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time. However, you can buy it then immediately sell it on the same day.

Find and return the maximum profit you can achieve.

Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 7
Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
Total profit is 4 + 3 = 7.
Example 2:

Input: prices = [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
Total profit is 4.
Example 3:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: There is no way to make a positive profit, so we never buy the stock to achieve the maximum profit of 0.

Constraints:

1 <= prices.length <= 3 * 104
0 <= prices[i] <= 104

"""
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0

        # Iterate through the prices array, comparing each price to the previous one
        for i in range(1, len(prices)):
            # If the current price is greater than the previous one, calculate the profit
            if prices[i] > prices[i - 1]:
                # Add the profit to the overall max_profit
                max_profit += prices[i] - prices[i - 1]

        return max_profit


# Example usage
if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    prices1 = [7, 1, 5, 3, 6, 4]
    profit1 = solution.maxProfit(prices1)
    print(profit1)  # Expected output: 7

    # Test case 2
    prices2 = [1, 2, 3, 4, 5]
    profit2 = solution.maxProfit(prices2)
    print(profit2)  # Expected output: 4

    # Test case 3
    prices3 = [7, 6, 4, 3, 1]
    profit3 = solution.maxProfit(prices3)
    print(profit3)  # Expected output: 0
