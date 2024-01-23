"""
Title     : Set .discard(), .remove() &amp; .pop()
Subdomain : Sets
Domain    : Python
Author    : Ahmedur Rahman Shovon
Created   : 15 July 2016
Problem   : https://www.hackerrank.com/challenges/py-set-discard-remove-pop/problem
"""

number_of_elements = int(input())
elements = set(map(int, input().split()))
number_of_commands = int(input())
for _ in range(number_of_commands):
    cmd = list(input().split())
    if len(cmd) == 1:
        elements.pop()
    else:
        value = int(cmd[1])
        operation = cmd[0]
        if operation == "discard":
            elements.discard(value)
        else:
            elements.remove(value)
print(sum(elements))
