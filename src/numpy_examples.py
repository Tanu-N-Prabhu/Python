import numpy as np

# For arrays of 3 zeros
a = np.zeros(3)
print(a)
print(type(a[0])) # Indicates that a is of float type and the values inside it is of type float


# For arrays of 10 zeros
b = np.zeros(10)
print(b)

# For looking to the shape of the array
print(b.shape)

# changing the shape of the array from 10 to 1

b.shape = (10, 1)
print(b)

# changing the zeros to ones
c = np.ones(5)
print(c)

# Using line space
d = np.linspace(2, 10, 5)
print(d)

# another way to create an array
e = np.array([10, 20])
print(e)
print(type(e))

# also we can add a list in a array
list = [1, 2, 3, 4, 5]
f = np.array([list])
print(f)

# creating a two dimension array
list2 = [[1, 2, 3, 4],[5, 6, 7,]]

g = np.array([list2])
print(g)

# creating a random array using random()

np.random.seed(0) # if you remove this line then, you can rerun the code and check that the random array is same.

h = np.random.randint(10, size=6)
print(h)
print(h[-1]) # gets the last element of the array