"""
Problem   : https://www.hackerrank.com/challenges/zipped/problem
"""

N, X = map(int, input().split())
scores = []
for _ in range(X):
    scores.append(list(map(float, input().split())))
for i in zip(*scores):
    print(sum(i) / len(i))
