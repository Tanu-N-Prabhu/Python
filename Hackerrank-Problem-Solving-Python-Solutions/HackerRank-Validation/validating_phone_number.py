"""
Let's dive into the interesting topic of regular expressions! You are given some input, and you are required to check whether they are valid mobile numbers.

A valid mobile number is a ten digit number starting with a  7,8 or 9.

Concept

A valid mobile number is a ten digit number starting with a  7,8 or 9.

Regular expressions are a key concept in any programming language. A quick explanation with Python examples is available here. You could also go through the link below to read more about regular expressions in Python.

https://developers.google.com/edu/python/regular-expressions

Input Format

The first line contains an integer N, the number of inputs.
N lines follow, each containing some string.

Constraints
1<=N<=10
2<=len(Number)<= 15

Output Format

For every string listed, print "YES" if it is a valid mobile number and "NO" if it is not on separate lines. Do not print the quotes.

Sample Input

2
9587456281
1252478965
Sample Output

YES
NO
"""
import re


def is_valid_mobile_number(number):
    # Define a regular expression pattern for a valid mobile number
    pattern = r'^[789]\d{9}$'

    # Use re.match to check if the string matches the pattern
    match = re.match(pattern, number)

    # Return "YES" if there is a match, "NO" otherwise
    return "YES" if bool(match) else "NO"


if __name__ == '__main__':
    # Read the number of inputs
    n = int(input().strip())

    # Process each input and check if it's a valid mobile number
    for _ in range(n):
        mobile_number = input().strip()
        print(is_valid_mobile_number(mobile_number))
