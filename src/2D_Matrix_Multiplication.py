import numpy as np

print("Make sure that a should be equal to b * c")
b = int(input("Enter the value of b ===> "))
c = int(input("Enter the value of c ===> "))
a = int(input("Enter the value of a ===> "))

first = np.arange(a).reshape(b, c)
print(first)

second = np.arange(a).reshape(b, c)
print(second)

product = first * second
print(product)

