"""
Title     : Check Subset
Subdomain : Sets
Domain    : Python
Author    : Ahmedur Rahman Shovon
Created   : 15 July 2016
Updated   : 19 June 2022
Problem   : https://www.hackerrank.com/challenges/py-check-subset/problem
"""

number_of_testcases = int(input())
for _ in range(number_of_testcases):
    number_of_elements_first_set = int(input())
    first_set = set(map(int, input().split()))
    number_of_elements_second_set = int(input())
    second_set = set(map(int, input().split()))
    print(first_set.issubset(second_set))
