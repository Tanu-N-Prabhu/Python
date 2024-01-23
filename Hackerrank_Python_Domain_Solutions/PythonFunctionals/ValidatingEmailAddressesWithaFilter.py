"""
Title     : Validating Email Addresses With a Filter
Subdomain : Python Functionals
Domain    : Python
Author    : Ahmedur Rahman Shovon
Created   : 15 July 2016
Updated   : 08 February 2023
Problem   : https://www.hackerrank.com/challenges/validate-list-of-email-address-with-filter/problem
"""

import re


def fun(s):
    return re.search(r"^[\w-]+@[a-zA-Z0-9]+\.[a-zA-Z]{1,3}$", s)


def filter_mail(emails):
    return list(filter(fun, emails))


if __name__ == "__main__":
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)
