# Importing the combinations function from itertools
from itertools import combinations

# Taking input for the size of the list
n = int(input())

# Taking input for the list of elements as space-separated values
ar = input().split()

# Taking input for the size of combinations to be generated
k = int(input())

# Generating all combinations of size k from the input list
comb_list = list(combinations(ar, k))

# Filtering combinations that contain the element "a"
a_list = [e for e in comb_list if "a" in e]

# Calculating and printing the probability of having "a" in a combination
print(len(a_list) / len(comb_list))
