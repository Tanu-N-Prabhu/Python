#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the counterGame function below.
def counterGame(n):
    n = bin(n)[2:]
    n = n.split('1')
    turns = len(n)+len(n[-1])-2
    return 'Louise' if turns&1 else 'Richard'
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = counterGame(n)

        fptr.write(result + '\n')

    fptr.close()
