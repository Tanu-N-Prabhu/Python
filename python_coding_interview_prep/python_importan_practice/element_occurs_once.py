"""
Given an arr[] of length N. Every element appears thrice except
one which occurs once. Find out the element occurs once.
"""


def find_element_appears_once(arr, n):
    for i in range(n):
        # it will count how many times this element appears
        if arr.count(arr[i]) == 1:
            return arr[i]
    return -1


array = [3, 3, 3, 4, 5, 4, 4, 2, 2, 2, 1, 1, 1]
print(find_element_appears_once(array,  len(array)))
