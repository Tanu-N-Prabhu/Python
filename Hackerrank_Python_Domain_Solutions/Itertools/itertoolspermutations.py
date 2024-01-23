# Importing permutations function from itertools
import itertools

# Taking input for the string and the value of n
s, n = list(map(str, input().split(" ")))

# Sorting the characters in the string
s = sorted(s)

# Generating permutations and printing them
for p in list(itertools.permutations(s, int(n))):
    print("".join(p))
