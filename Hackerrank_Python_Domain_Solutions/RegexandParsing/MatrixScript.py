"""
Title     : Matrix Script
Subdomain : Regex and Parsing
Domain    : Python
Author    : Ahmedur Rahman Shovon
Created   : 15 July 2016
Problem   : https://www.hackerrank.com/challenges/matrix-script/problem
"""
import re

n, m = map(int, input().split())
character_ar = [""] * (n * m)
for i in range(n):
    line = input()
    for j in range(m):
        character_ar[i + (j * n)] = line[j]
decoded_str = "".join(character_ar)
final_decoded_str = re.sub(
    r"(?<=[A-Za-z0-9])([ !@#$%&]+)(?=[A-Za-z0-9])", " ", decoded_str
)
print(final_decoded_str)
