"""
Title     : Set .intersection() Operation
Subdomain : Sets
Domain    : Python
Author    : Ahmedur Rahman Shovon
Created   : 15 July 2016
Updated   : 19 June 2022
Problem   : https://www.hackerrank.com/challenges/py-set-intersection-operation/problem
"""
number_of_english_subscribers = input()
english_subscribers = set(map(int, input().split()))
number_of_french_subscribers = input()
french_subscribers = set(map(int, input().split()))
print(len(english_subscribers.intersection(french_subscribers)))
# Alternative solution
# print(len(english_subscribers & french_subscribers))
