"""
Problem   : https://www.hackerrank.com/challenges/np-min-and-max/problem
"""

import numpy

n, m = map(int, input().split())
ar = []
for _ in range(n):
    tmp = list(map(int, input().split()))
    ar.append(tmp)
np_ar = numpy.array(ar)
print(numpy.max(numpy.min(np_ar, axis=1)))
