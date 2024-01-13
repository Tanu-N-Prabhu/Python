#!/bin/python3

import math
import os
import random
import re
import sys
# Complete the aVeryBigSum function below.
def aVeryBigSum(ar):
    sum = 0
    for i in range(len(ar)):
        sum+=ar[i]
    return sum

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = aVeryBigSum(ar)

    fptr.write(str(result) + '\n')

    fptr.close()
