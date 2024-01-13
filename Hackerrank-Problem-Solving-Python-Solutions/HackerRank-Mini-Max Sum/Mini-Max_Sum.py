#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    sum=0
    for i in range(len(arr)):
        sum+=arr[i]
    print ( sum-max(arr), sum-min(arr))

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
