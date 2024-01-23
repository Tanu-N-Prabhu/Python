"""
Problem   : https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem
"""
if __name__ == "__main__":
    n = int(input())
    arr = map(int, input().split())
    # the line is finding the second largest unique element in the list arr after removing any duplicates.
    print(sorted(set(arr), reverse=True)[1])
