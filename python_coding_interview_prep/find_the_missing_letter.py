"""
Write a method that takes an array of consecutive (increasing) letters as input and that returns
the missing letter in the array.

You will always get a valid array. And it will be always exactly one letter be missing.
The length of the array will always be at least 2.
The array will always contain letters in only one case.

Example:

['a','b','c','d','f'] -> 'e'
['O','Q','R','S'] -> 'P'
(Use the English alphabet with 26 letters!)
"""


def find_missing_letter(chars):
    chars_len = len(chars)
    if chars_len < 2:
        return None

    # Iterate through the characters in the array
    for i in range(chars_len - 1):
        # Check if the ASCII difference between consecutive characters is greater than 1
        if ord(chars[i + 1]) - ord(chars[i]) > 1:
            # Return the missing character
            return chr(ord(chars[i]) + 1)


# Example usage:
print(find_missing_letter(['a', 'b', 'c', 'd', 'f']))  # Output: 'e'
print(find_missing_letter(['O', 'Q', 'R', 'S']))         # Output: 'P'


