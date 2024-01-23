# Importing product function from itertools
import itertools

# Taking input for the values of k and m
k, m = map(int, input().split())

# Initializing a list to store sublists from input
main_ar = []

# Populating main_ar with sublists
for _ in range(k):
    ar = list(map(int, input().split()))
    main_ar.append(ar[1:])

# Generating all combinations of elements from sublists
all_combination = itertools.product(*main_ar)

# Initializing result variable to store the maximum sum modulo m
result = 0

# Iterating through each combination and updating the result
for single_combination in all_combination:
    # Calculating the sum of squares for each element in the current combination
    current_sum = sum(x * x for x in single_combination)

    # Updating the result with the maximum of the current sum modulo m and the existing result
    result = max(current_sum % m, result)

# Printing the final result
print(result)
