# Importing combinations function from itertools
from itertools import combinations

# Taking input for the string and the value of n
s, n = input().split()
n = int(n) + 1

# Sorting the characters in the string
s = sorted(s)

# Generating combinations and printing them for each size from 1 to n
for i in range(1, n):
    for j in combinations(s, i):
        print("".join(j))
