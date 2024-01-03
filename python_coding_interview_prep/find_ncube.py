"""
Your task is to construct a building which will be a pile of n cubes.
The cube at the bottom will have a volume of (n-1)^3
You are given the total volume m of the building.
Being given m can you find the number n of cubes you will have to build?


"""


def find_nb(m):
    n = 1
    total_volume = 0

    while total_volume < m:
        total_volume += n ** 3
        if total_volume == m:
            return n
        n += 1

    return -1

# Test cases
result1 = find_nb(1071225)
print(result1)  # Should print 45

result2 = find_nb(91716553919377)
print(result2)  # Should print -1
