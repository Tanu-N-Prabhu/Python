# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6

    sorted_array = sorted(A)

    expected_num = 1
    for item in sorted_array:
        if item == expected_num:
            expected_num += 1
        else:
            return 0

    return 1
