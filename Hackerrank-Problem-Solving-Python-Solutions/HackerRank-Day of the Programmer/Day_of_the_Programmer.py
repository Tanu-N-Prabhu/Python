#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(year):
    if (year == 1918):
        return '26.09.1918'
    elif ((year <= 1917) & (year%4 == 0)) or ((year > 1918) & (year%400 == 0 or ((year%4 == 0) & (year%100 != 0)))):
        return '12.09.%s' %year
    else:
        return '13.09.%s' %year

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    year = int(input())

    result = solve(year)

    fptr.write(result + '\n')

    fptr.close()
