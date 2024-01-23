# Importing numpy module
import numpy

# Taking input as a list of floats
ar = list(map(float, input().split()))

# Creating a numpy array from the input list
np_ar = numpy.array(ar, float)

# Printing the reversed numpy array
print(np_ar[::-1])
