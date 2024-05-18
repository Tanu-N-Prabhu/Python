"""
Coin Game:

Raman is playing a game where he starts with x coins. In each step, he either wins or loses money, 
and the psychic predicts the outcomes after each step.

The goal is for Raman to start with the minimum amount of money where he doesn’t run out of funds. 
He must avoid going into a credit situation.

Input Format:

First line: n, the number of steps in the game
Next n lines: n integers denoting the outcomes of each game (positive for winning, negative for losing money)
Output Format:
One integer representing the minimum amount Raman should start with.

Example:

Input
n=4

outcomes=[
2
-9
15
2
]

Output: 7 (If he starts with 7 rupees, the sequence becomes 7 -> 9 -> 0 -> 15 -> 17.)1

"""
# To find the minimum amount Raman should start with, you can iterate through the outcomes
# while keeping track of the cumulative sum.
# The minimum amount he should start with would be the absolute maximum of the cumulative sum encountered.


def min_starting_amount(n, outcomes):
    # Initialize variables to keep track of cumulative sum and minimum starting amount
    cumulative_sum = 0
    min_start = 0

    # Iterate through each outcome
    for outcome in outcomes:
        # Update the cumulative sum by adding the outcome
        cumulative_sum += outcome
        # Update the minimum starting amount by taking
        # the absolute maximum of the cumulative sum encountered
        min_start = max(min_start, abs(cumulative_sum))

    # Return the minimum starting amount
    return min_start


# Example usage:
n = 4
outcomes = [2, -9, 15, 2]
print(min_starting_amount(n, outcomes))  # Output: 7
