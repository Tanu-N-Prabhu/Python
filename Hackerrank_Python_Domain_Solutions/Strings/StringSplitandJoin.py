"""
Title     : String Split and Join
Subdomain : Strings
Domain    : Python
Author    : Ahmedur Rahman Shovon
Created   : 08 July 2020
Problem   : https://www.hackerrank.com/challenges/python-string-split-and-join/problem
"""


def split_and_join(sentence):
    return "-".join(sentence.split())


if __name__ == "__main__":
    line = input()
    result = split_and_join(line)
    print(result)
