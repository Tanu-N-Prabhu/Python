"""
You are given a string, and you have to validate whether it's a valid Roman numeral. If it is valid, print True.
Otherwise, print False. Try to create a regular expression for a valid Roman numeral.

Input Format

A single line of input containing a string of Roman characters.

Output Format

Output a single line containing True or False according to the instructions above.

Constraints

The number will be between 2 and  3999 (both included).

Sample Input

CDXXI
Sample Output

True
References

Regular expressions are a key concept in any programming language. A quick explanation with Python examples is
available here. You could also go through the link below to read more about regular expressions in Python.

https://developers.google.com/edu/python/regular-expressions
"""
import re


def is_valid_roman_numeral(s):
    # Define a regular expression pattern for a valid Roman numeral
    pattern = r'^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$'

    # Use re.match to check if the string matches the pattern
    match = re.match(pattern, s)

    # Return True if there is a match, False otherwise
    return bool(match)


if __name__ == '__main__':
    # Read the input string
    roman_numeral = input().strip()

    # Check if it's a valid Roman numeral and print the result
    print(is_valid_roman_numeral(roman_numeral))
