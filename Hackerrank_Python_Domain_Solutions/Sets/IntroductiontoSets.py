"""
Title     : Introduction to Sets
Subdomain : Sets
Domain    : Python
Author    : Ahmedur Rahman Shovon
Created   : 15 July 2016
Updated   : 19 June 2022
Problem   : https://www.hackerrank.com/challenges/py-introduction-to-sets/problem
"""
import statistics


def average(array):
    distinct_heights = set(array)
    avg_heights = sum(distinct_heights) / len(distinct_heights)
    # It can also be solved using built-in function from statistics module
    # Uncomment the following line to use builtin function
    # avg_heights = statistics.mean(distinct_heights)
    return round(avg_heights, 3)


if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
