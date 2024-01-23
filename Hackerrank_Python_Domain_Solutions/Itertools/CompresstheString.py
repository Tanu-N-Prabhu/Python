# Importing the itertools module for grouping functionality
import itertools

# Taking input and removing leading/trailing whitespaces
s = input().strip()

# Finding unique elements in the input string
s_unique_element = list(set(s))

# Lists to store grouped elements and corresponding keys
group = []
key = []

# Using itertools.groupby to group consecutive identical elements
for k, g in itertools.groupby(s):
    group.append(list(g))  # Storing the grouped elements as a list
    key.append(k)  # Storing the key (unique element) for each group

# Printing the length and key for each group
for i in range(len(group)):
    group_length = len(group[i])
    k = int(key[i])  # Converting key to integer
    print((group_length, k), end=" ")  # Printing the result tuple for each group
