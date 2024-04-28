"""
For a given set of denominations, you are asked to find the minimum number of coins with
which a given amount of money can be paid. That problem can be approached by a greedy
algorithm that always selects the largest denomination not exceeding the remaining amount
of money to be paid. As long as the remaining amount is greater than zero, the process is
repeated.
A correct algorithm should always return the minimum number of coins. It turns out
that the greedy algorithm is correct for only some denomination selections, but not for all.
For example, for coins of values 1, 2 and 5 the algorithm returns the optimal number of
coins for each amount of money, but for coins of values 1, 3 and 4 the algorithm may return
a suboptimal result. An amount of 6 will be paid with three coins: 4, 1 and 1 by using the
greedy algorithm. The optimal number of coins is actually only two: 3 and 3.
Consider n denominations 0 < m0 ¬ m1 ¬ . . . ¬ mn−1 and the amount k to be paid.
"""
from typing import List, Tuple


def greedy_coin_changing(coins: List[int], amount: int) -> List[Tuple[int, int]]:
    """
    Computes the minimum number of coins needed to make up a given amount using greedy approach.

    :param coins: List of coin denominations
    :param amount: Target amount to make up
    :return: List of tuples containing coin denomination and its count
    """
    n = len(coins)
    result = []

    # Iterate through the coin denominations in reverse order
    for i in range(n - 1, -1, -1):
        # Calculate the maximum number of coins of current denomination that can be used
        coin_count = amount // coins[i]

        # Add a tuple containing the coin denomination and its count to the result list
        result.append((coins[i], coin_count))

        # Update the remaining amount after using the current denomination
        # For example, let's say we have coin denominations [1, 2, 5] and the target amount is 9. 
        # After using the maximum number of 5's possible (one 5 coin), 
        # the remaining amount would be 9 % 5 = 4, indicating that 4 units still need to be achieved.
        amount %= coins[i]

    return result


if __name__ == '__main__':
    coins = [1, 3, 4]
    amount = 6
    print(f'coins: {coins} and amount: {amount}')
    print(greedy_coin_changing(coins, amount))

    coins = [1, 2, 5, 10]
    amount = 15
    print(f'coins: {coins} and amount: {amount}')
    print(greedy_coin_changing(coins, amount))
    