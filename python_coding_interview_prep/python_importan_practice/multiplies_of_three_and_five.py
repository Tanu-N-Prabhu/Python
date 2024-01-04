"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
The sum of these multiples is 23.

Finish the solution so that it returns the sum of all the multiples of 3 or 5 below the number passed in.

Additionally, if the number is negative, return 0.

Note: If the number is a multiple of both 3 and 5, only count it once.
"""


def solution(number):
    # Check if the number is negative
    if number < 0:
        return 0

    # Initialize sum to 0
    sum_multiples = 0

    # Iterate through numbers below the given number
    for i in range(number):
        # Check if the number is a multiple of 3 or 5
        if i % 3 == 0 or i % 5 == 0:
            # Add the multiple to the sum
            sum_multiples += i

    return sum_multiples


# Example usage:
result = solution(10)
print(result)  # Output: 23
