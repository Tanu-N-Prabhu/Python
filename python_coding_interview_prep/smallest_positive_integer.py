"""
Write a function:

def solution(A)

that, given an array A of N integers, returns

the smallest positive integer (greater than 0) that does not occur in A.

For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.

Given A = [1, 2, 3], the function should return 4.

Given A = [−1, −3], the function should return 1.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..100,000];
each element of array A is an integer within the range [−1,000,000..1,000,000].

"""


def solution(A):
    if 1 <= len(A) <= 100000:
        all_in_range = all(-1000000 <= x <= 1000000 for x in A)
        if all_in_range:
            positive_integers = set(x for x in A if x > 0)

            # If there are no positive integers in the array, return 1
            if not positive_integers:
                return 1

            # Iterate over positive integers starting from 1
            for i in range(1, len(A) + 2):
                if i not in positive_integers:
                    return i

    return 1