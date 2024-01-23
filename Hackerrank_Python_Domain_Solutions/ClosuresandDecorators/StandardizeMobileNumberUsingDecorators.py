"""
Title     : Standardize Mobile Number Using Decorators
Problem   : https://www.hackerrank.com/challenges/standardize-mobile-number-using-decorators/problem
"""

n = int(input())
ar = []
for _ in range(n):
    tmp_str = input()
    tmp_str = tmp_str[len(tmp_str) - 10 :]
    ar.append(tmp_str)

ar.sort()
for item in ar:
    print(f"+91 {item[:5]} {item[5:]}")
