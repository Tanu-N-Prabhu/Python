"""
Build a pyramid-shaped tower, as an array/list of strings,
given a positive integer number of floors. A tower block is represented with "*" character.
"""


def tower_builder(n_floors):
    tower = []
    width = 2 * n_floors - 1

    for i in range(1, n_floors + 1):
        stars = '*' * (2 * i - 1)
        spaces = ' ' * ((width - len(stars)) // 2)
        tower.append(spaces + stars + spaces)

    return tower


# Test case
result = tower_builder(5)
print(result)
