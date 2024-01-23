"""
Title     : Re.start() &amp; Re.end()
Subdomain : Regex and Parsing
Domain    : Python
Author    : Ahmedur Rahman Shovon
Created   : 15 July 2016
Problem   : https://www.hackerrank.com/challenges/re-start-re-end/problem
"""
import re

s = input().strip()
k = input().strip()
s_len = len(s)
found_flag = False
for i in range(s_len):
    match_result = re.match(k, s[i:])
    if match_result:
        start_index = i + match_result.start()
        end_index = i + match_result.end() - 1
        print((start_index, end_index))
        found_flag = True
if found_flag == False:
    print("(-1, -1)")
