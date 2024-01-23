"""
Title     : Validating Postal Codes
Subdomain : Regex and Parsing
Domain    : Python
Author    : Ahmedur Rahman Shovon
Created   : 15 July 2016
Problem   : https://www.hackerrank.com/challenges/validating-postalcode/problem
"""
import re

p = input().strip()
range_check = bool(re.match(r"^[1-9][0-9]{5}$", p))
repeat_check = len(re.findall(r"(?=([0-9])[0-9]\1)", p))
print(range_check == True and repeat_check < 2)
