"""
You might know some pretty large perfect squares. But what about the NEXT one?

Complete the findNextSquare method that finds the next integral perfect square after
the one passed as a parameter. Recall that an integral perfect square is an integer n such that
sqrt(n) is also an integer.

If the parameter is itself not a perfect square then -1 should be returned.
You may assume the parameter is non-negative.

Examples:(Input --> Output)

121 --> 144
625 --> 676
114 --> -1 since 114 is not a perfect square
"""


def find_next_square(sq):
    # Check if the given number is a perfect square
    sqrt = sq ** 0.5
    if sqrt.is_integer():
        # If it is, find the next perfect square
        next_square = (sqrt + 1) ** 2
        return int(next_square)
    else:
        # If not, return -1
        return -1


# Test cases
result1 = find_next_square(121)
print(result1)  # Should print 144

result2 = find_next_square(625)
print(result2)  # Should print 676

result3 = find_next_square(114)
print(result3)  # Should print -1
