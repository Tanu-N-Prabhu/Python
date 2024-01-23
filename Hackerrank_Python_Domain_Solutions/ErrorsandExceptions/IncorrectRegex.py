# Context:
# The provided code takes an integer 'n' as input, followed by 'n' strings. It attempts to compile each string as a
# regular expression using the 're.compile' method. If the compilation is successful, it prints True; otherwise, it
# catches the exception and prints False.

# Input:
# - n: An integer representing the number of strings to process.
# - For each string 's':
#   - s: The string to be compiled as a regular expression.

# Output:
# - For each string, True if it can be compiled as a regular expression; otherwise, False.

import re

n = int(input())

for _ in range(n):
    s = input()
    try:
        re.compile(s)
        print(True)
    except Exception as e:
        print(False)
