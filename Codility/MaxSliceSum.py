# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

import sys

def solution(A):
    # write your code in Python 3.6
    
    # max_value = sys.maxsize
    # min_value = -sys.maxsize -1

    local_max_sum = A[0]
    global_max_sum = A[0]
    
    for index in range( 1, len(A) ):
        # note: be careful about the negative value (we may recount from A[index])
        local_max_sum = max( local_max_sum + A[index], A[index] )
        global_max_sum = max( global_max_sum, local_max_sum )

    # special case: all negtive value(s)
    if max(A) < 0:
        global_max_sum = max(A)    
    
    return global_max_sum
