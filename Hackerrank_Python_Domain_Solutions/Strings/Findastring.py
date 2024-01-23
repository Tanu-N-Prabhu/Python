"""
Title     : Find a string
Subdomain : Strings
Domain    : Python
Author    : Ahmedur Rahman Shovon
Created   : 15 July 2016
Updated   : 08 February 2023
Problem   : https://www.hackerrank.com/challenges/find-a-string/problem
"""


def count_substring(string, sub_string):
    count_sub_string = 0
    for i in range(len(string) - len(sub_string) + 1):
        if string[i : i + len(sub_string)] == sub_string:
            count_sub_string += 1
    return count_sub_string


if __name__ == "__main__":
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)
