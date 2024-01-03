"""
Simple, given a string of words, return the length of the shortest word(s).

String will never be empty and you do not need to account for different data types.
"""


def find_short(s):
    # Split the string into words
    words = s.split()

    # Find the length of the shortest word
    shortest_length = min(len(word) for word in words)

    return shortest_length


# Test case
result = find_short("This is a test string")
print(result)  # Should print 1 (length of the shortest word "a")
