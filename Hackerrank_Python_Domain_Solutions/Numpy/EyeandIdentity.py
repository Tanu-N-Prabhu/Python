"""
Problem   : https://www.hackerrank.com/challenges/np-eye-and-identity/problem
"""
import numpy as np

np.set_printoptions(legacy="1.13")
n, m = map(int, input().split())
print(np.eye(n, m, k=0))
