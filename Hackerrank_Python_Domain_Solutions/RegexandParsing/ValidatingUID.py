"""
Title     : Validating UID
Subdomain : Regex and Parsing
Domain    : Python
Author    : Ahmedur Rahman Shovon
Created   : 15 July 2016
Problem   : https://www.hackerrank.com/challenges/validating-uid/problem
"""

import re

n = int(input())
upper_check = r".*([A-Z].*){2,}"
digit_check = r".*([0-9].*){3,}"
alphanumeric_and_length_check = r"([A-Za-z0-9]){10}$"
repeat_check = r".*(.).*\1"
for _ in range(n):
    uid_string = input().strip()
    upper_check_result = bool(re.match(upper_check, uid_string))
    digit_check_result = bool(re.match(digit_check, uid_string))
    alphanumeric_and_length_check_result = bool(
        re.match(alphanumeric_and_length_check, uid_string)
    )
    repeat_check_result = bool(re.match(repeat_check, uid_string))
    if (
        upper_check_result
        and digit_check_result
        and alphanumeric_and_length_check_result
        and not repeat_check_result
    ):
        print("Valid")
    else:
        print("Invalid")
