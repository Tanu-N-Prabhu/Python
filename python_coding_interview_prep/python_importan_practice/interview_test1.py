# *** TASK 2 ***
#
# Explain the following behavior in Python Interactive shell.

"""
>>> True, True, True == (True, True, True)
(True, True, False)
"""

# *** // TASK 2 END ***

# *** TASK 3 ***
#
# Transform uppercase chars to lowercase and vice-versa
# So following will become "AAbbccJJiiAAAmmMMLLlllLIIOIS"
from functools import reduce

s = "aaBBCCjjIIaaaMMmmllLLLliiois"
print([x.upper() if x.islower() else x.lower() for x in s])

# *** // TASK 3 END ***

# *** TASK 4 ***
#
# Transform following list into dict, using item as value and it's position in list as key:

l = [45, 22, 14, 65, 97, 72]
dict = {}
map(lambda x: dict.append([x]),for i in l)
# *** // TASK 4 END ***``


# *** TASK 5 ***
#
# Sort a list of dicts by price descending
cars = [
    {"model": "Ford T", "price": 2000},
    {"model": "Ford F150", "price": 25000},
    {"model": "Ford Focus", "price": 12000},
]

sorted(cars.items(), key=lambda x: x['price'], reversed=True)

# *** // TASK 5 END ***


# *** TASK 6 ***
#
# Sum squares of first 100000 integers

result = reduce(lambda x, y: ((x ** x) + (y ** y)), range(1, 100000))

# *** // TASK 6 END ***


