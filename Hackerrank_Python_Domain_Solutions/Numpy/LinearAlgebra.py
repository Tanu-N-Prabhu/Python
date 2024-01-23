# Importing numpy module with alias np
import numpy as np

# Setting print options for numpy
np.set_printoptions(legacy="1.13")

# Taking input for the size of the square matrix
n = int(input())

# Creating a numpy array from input values
array = np.array([input().split() for _ in range(n)], float)

# Printing the determinant of the array using numpy's linalg.det function
print(np.linalg.det(array))
