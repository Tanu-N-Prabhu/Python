"""
Problem   : https://www.hackerrank.com/challenges/find-angle/problem
"""


import math

ab = float(input())
bc = float(input())
ac = math.sqrt(ab**2 + bc**2)
bm = ac / 2.0
mc = bm
# let,
b = mc
c = bm
a = bc
# where b=c
angel_b_radian = math.acos(a / (2 * b))
angel_b_degree = int(round((180 * angel_b_radian) / math.pi))
print(f"{angel_b_degree}°")
