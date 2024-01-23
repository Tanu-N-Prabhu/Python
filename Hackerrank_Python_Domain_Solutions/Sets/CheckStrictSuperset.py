"""
Title     : Check Strict Superset
Subdomain : Sets
Domain    : Python
Author    : Ahmedur Rahman Shovon
Created   : 15 July 2016
Updated   : 19 June 2022
Problem   : https://www.hackerrank.com/challenges/py-check-strict-superset/problem
"""

first_set = set(map(int, input().split()))
number_of_other_sets = int(input())
is_strict_superset = True
for _ in range(number_of_other_sets):
    other_set = set(map(int, input().split()))
    if not first_set.issuperset(other_set):
        is_strict_superset = False
print(is_strict_superset)
