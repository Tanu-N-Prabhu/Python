"""
Problem   : https://www.hackerrank.com/challenges/np-sum-and-prod/problem
"""

import numpy

n, m = map(int, input().split())
ar = []
for _ in range(n):
    tmp = list(map(int, input().split()))
    ar.append(tmp)
np_ar = numpy.array(ar)
s = numpy.sum(np_ar, axis=0)
print(numpy.prod(s))
