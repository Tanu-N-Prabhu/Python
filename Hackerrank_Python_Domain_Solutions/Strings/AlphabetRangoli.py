"""
Title     : Alphabet Rangoli
Subdomain : Strings
Domain    : Python
Author    : Ahmedur Rahman Shovon
Created   : 15 July 2016
Problem   : https://www.hackerrank.com/challenges/alphabet-rangoli/problem
"""

n = int(input().strip())
w = (n - 1) * 2 + ((n * 2) - 1)
# upper half
for i in range(1, n):
    number_of_letter = (i * 2) - 1
    s = ""
    letter_value = 97 + n - 1
    for i in range(number_of_letter):
        if i != 0:
            s += "-"
        s += chr(letter_value)
        if i < (number_of_letter - 1) / 2:
            letter_value = letter_value - 1
        else:
            letter_value = letter_value + 1
    print(s.center(w, "-"))


# bottom half
for i in range(n, 0, -1):
    number_of_letter = (i * 2) - 1
    s = ""
    letter_value = 97 + n - 1
    for i in range(number_of_letter):
        if i != 0:
            s += "-"
        s += chr(letter_value)
        if i < (number_of_letter - 1) / 2:
            letter_value = letter_value - 1
        else:
            letter_value = letter_value + 1
    print(s.center(w, "-"))
