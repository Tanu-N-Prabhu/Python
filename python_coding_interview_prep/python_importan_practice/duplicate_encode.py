"""
The goal of this exercise is to convert a string to a new string where each character
in the new string is "(" if that character appears only once in the original string, or ")"
if that character appears more than once in the original string.
Ignore capitalization when determining if a character is a duplicate.

Examples
"din"      =>  "((("
"recede"   =>  "()()()"
"Success"  =>  ")())())"
"(( @"     =>  "))(("
Notes
Assertion messages may be unclear about what they display in some languages.
If you read "...It Should encode XXX", the "XXX" is the expected result, not the input!
"""


def duplicate_encode(word):
    # Convert the word to lowercase for case-insensitive comparison
    word = word.lower()

    # Create a dictionary to store the count of each character
    char_count = {}

    # Populate the dictionary with character counts
    for char in word:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    # Create the result string based on character counts
    result = ''.join('(' if char_count[char] == 1 else ')' for char in word)

    return result


# Test cases
result1 = duplicate_encode("din")
print(result1)  # Should print "((("

result2 = duplicate_encode("recede")
print(result2)  # Should print "()()()"

result3 = duplicate_encode("Success")
print(result3)  # Should print ")())())"

result4 = duplicate_encode("(( @")
print(result4)  # Should print "))(("
