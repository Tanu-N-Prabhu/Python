"""
Title     : Text Alignment
Subdomain : Strings
Domain    : Python
Author    : Ahmedur Rahman Shovon
Created   : 15 July 2016
Updated   : 08 July 2020
Problem   : https://www.hackerrank.com/challenges/text-alignment/problem
"""

thickness = int(input())
c = "H"

# Top Cone
for i in range(thickness):
    print((c * i).rjust(thickness - 1) + c + (c * i).ljust(thickness - 1))

# Top Pillars
for i in range(thickness + 1):
    print((c * thickness).center(thickness * 2) + (c * thickness).center(thickness * 6))

# Middle Belt
for i in range((thickness + 1) // 2):
    print((c * thickness * 5).center(thickness * 6))

# Bottom Pillars
for i in range(thickness + 1):
    print((c * thickness).center(thickness * 2) + (c * thickness).center(thickness * 6))

# Bottom Cone
for i in range(thickness):
    print(
        (
            (c * (thickness - i - 1)).rjust(thickness)
            + c
            + (c * (thickness - i - 1)).ljust(thickness)
        ).rjust(thickness * 6)
    )
