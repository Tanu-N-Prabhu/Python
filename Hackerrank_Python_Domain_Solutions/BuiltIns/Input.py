"""
Problem   : https://www.hackerrank.com/challenges/input/problem
"""

if __name__ == "__main__":
    x, k = map(int, input().strip().split())
    equation = input().strip()
    print(eval(equation) == k)
