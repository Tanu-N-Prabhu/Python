#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'fizzBuzz' function below.
# given a number n, each integer i in range of 1 to n inclusive. 
#
# The function accepts INTEGER n as parameter.
#

def fizzBuzz(n):
    # Write your code here
    if n > 0 and n < 2 * 10**5:
        for i in range(1, n+1):
            if i % 3 == 0 and i % 5 == 0:
                print("HackerRank-FizzBuzz")
            elif i % 3 == 0 and i % 5 != 0:
                print("Fizz")
            elif i % 5 == 0 and i % 3 != 0:
                print("Buzz")
            else:
                print(i) 
        

if __name__ == '__main__':
    n = int(input().strip())
    fizzBuzz(n)
