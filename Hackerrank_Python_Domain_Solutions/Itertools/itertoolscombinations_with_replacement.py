# Importing combinations_with_replacement function from itertools
from itertools import combinations_with_replacement

# Taking input for the string and the value of n
s, n = input().split()
n = int(n)

# Sorting the characters in the string
s = sorted(s)

# Generating combinations with replacement and printing them
for j in combinations_with_replacement(s, n):
    print("".join(j))
