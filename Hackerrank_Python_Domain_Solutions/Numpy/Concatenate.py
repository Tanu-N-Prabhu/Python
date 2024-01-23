"""
Problem   : https://www.hackerrank.com/challenges/np-concatenate/problem
"""


import numpy

n, m, p = map(int, input().split())

ar1 = []
ar2 = []
for _ in range(n):
    tmp = list(map(int, input().split()))
    ar1.append(tmp)
for _ in range(m):
    tmp = list(map(int, input().split()))
    ar2.append(tmp)
np_ar1 = numpy.array(ar1)
np_ar2 = numpy.array(ar2)
print(numpy.concatenate((np_ar1, np_ar2), axis=0))
