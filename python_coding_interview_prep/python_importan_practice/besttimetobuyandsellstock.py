"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.



Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
Example 2:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.


Constraints:

1 <= prices.length <= 105
0 <= prices[i] <= 104

"""
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')  # Initialize min_price to positive infinity
        max_profit = 0

        for price in prices:
            # if price is less than min_price, update min_price
            if price < min_price:
                min_price = price
                print(f'min_price {min_price}')
            # if price is greater than min_price, update max_profit
            else:
                # Update max_profit if current price is greater
                max_profit = max(max_profit, price - min_price)
                print(f'max_profit {max_profit}')

        return max_profit

# Example usage
if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    prices1 = [7, 1, 5, 3, 6, 4]
    profit1 = solution.maxProfit(prices1)
    print(profit1)  # Expected output: 5

    # Test case 2
    prices2 = [7, 6, 4, 3, 1]
    profit2 = solution.maxProfit(prices2)
    print(profit2)  # Expected output: 0
