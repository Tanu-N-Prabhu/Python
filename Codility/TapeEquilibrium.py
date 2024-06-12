# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

import sys

def solution(A):
    # write your code in Python 3.6
    
    INT_MAX = sys.maxsize
    INT_MIN = -sys.maxsize-1
    
    min_diff = INT_MAX
    
    for index in range(0, len(A) ):
        
        first_total = 0
        for j in range(0, index):
            first_total += A[j]
        
        second_total = 0
        for k in range(index, len(A) ):
            second_total += A[k]
        
        current_difference = abs( first_total - second_total )
        
        min_diff = min( min_diff, current_difference )
    
    return min_diff
