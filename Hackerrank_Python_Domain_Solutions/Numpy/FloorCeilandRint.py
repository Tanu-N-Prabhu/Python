# Importing numpy module with alias np
import numpy as np

# Setting print options for numpy
np.set_printoptions(legacy="1.13")

# Creating a numpy array from input values
A = np.array(input().split(), float)

# Printing the floor, ceiling, and rounded values of the array
# only integer part and discarding the decimal part eg. 23.45 become 23
print(np.floor(A))
# next integer eg. 23.45 become 24
print(np.ceil(A))
print(np.rint(A))

# Alternate solution
# print(*(f(A) for f in [np.floor, np.ceil, np.rint]), sep='\n')
