"""
Title     : No Idea!
Subdomain : Sets
Domain    : Python
Author    : Ahmedur Rahman Shovon
Created   : 15 July 2016
Updated   : 19 June 2022
Problem   : https://www.hackerrank.com/challenges/no-idea/problem
"""
from collections import Counter

n, m = map(int, input().split())
data = list(map(int, input().split()))
data_counter = Counter(data)
data_set = set(data)
set_a = set(map(int, input().split()))
set_b = set(map(int, input().split()))
happiness = 0
for i in data_set & set_a:
    happiness += data_counter[i]
for i in data_set & set_b:
    happiness -= data_counter[i]
print(happiness)
