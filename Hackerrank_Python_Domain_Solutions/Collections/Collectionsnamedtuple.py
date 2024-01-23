"""
Title     : Collections.namedtuple()
Problem   : https://www.hackerrank.com/challenges/py-collections-namedtuple/problem
"""

from collections import namedtuple

n = int(input())
columns = ",".join(input().split())
Student = namedtuple("Student", columns)
data = []
for i in range(n):
    row = input().split()
    s = Student._make(row)
    data.append(s)
avg = sum(float(s.MARKS) for s in data) / n
print(f"{avg:.2f}")
