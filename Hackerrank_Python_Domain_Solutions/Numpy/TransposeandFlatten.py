"""
Problem   : https://www.hackerrank.com/challenges/np-transpose-and-flatten/problem
"""

import numpy

n, m = map(int, input().split())
ar = []
for _ in range(n):
    row = list(map(int, input().split()))
    ar.append(row)

np_ar = numpy.array(ar)
print(numpy.transpose(np_ar))
print(np_ar.flatten())
