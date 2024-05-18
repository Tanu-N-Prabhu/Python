"""
sort given binary digits in Input: 0010101001101, Output: 0000000011111111
"""


def sort_binary(input_str):
    # Count the number of zeroes and ones
    zeros = input_str.count('0')
    ones = len(input_str) - zeros

    # Sort the input binary digits
    sorted_binary = '0' * zeros + '1' * ones

    return sorted_binary


# Example usage:
input_binary = "0010101001101"
print(sort_binary(input_binary))  # Output: "0000000011111111"
