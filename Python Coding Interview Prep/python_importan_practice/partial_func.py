from functools import partial


def multiply(x, y):
    return x * y


# create a new function that multiplies by 2
print(multiply(2, 2))
dbl = partial(multiply, 2)
print(dbl(4))
