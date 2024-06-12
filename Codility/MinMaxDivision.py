# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

import math

def solution(K, M, A):
    # write your code in Python 3.6
    
    # try to find minMaxSum 
    # we can try 'minMaxSum' by using binary search (fast)
    # but, we need to know 
    # min_possible_sum and max_possible_sum
    # so, we can try mid_possible_sum (using binary search)
    
    # 1. find min_possible_sum and max_possible_sum
    min_possible_sum = 0 
    max_possible_sum = 0
    for item in A:
        min_possible_sum = max(min_possible_sum, item) # at least one element (large)
        max_possible_sum += item # at most all elements (sum of all)
    #print(min_possible_sum)
    #print(max_possible_sum)
    
    # 3. check if mid_possible_sum is 'ok' or not (define the method)
    def check_if_mid_sum_possible(K, M, A, mid_sum):
        num_block_allowed = K
        current_block_sum = 0 
        for item in A:
            current_block_sum += item
            if current_block_sum > mid_sum: # need another block
                num_block_allowed -= 1
                current_block_sum = item # important (the item in next block)
                if num_block_allowed ==0:
                    return False
        # all blocks can be smaller than (or equal to) mid_sum
        return True
    
    # 2. binary search
    result = max_possible_sum
    
    while min_possible_sum <= max_possible_sum:
        mid_possible_sum = math.ceil( (min_possible_sum + max_possible_sum) / 2 )
        # print(mid_possible_sum)
        
        # try smaller 
        is_sum_possible = check_if_mid_sum_possible(K, M, A, mid_possible_sum)
        # print(is_sum_possible)
        if is_sum_possible == True:
            result = mid_possible_sum
            max_possible_sum = mid_possible_sum - 1
        
        # try bigger
        else:
            min_possible_sum = mid_possible_sum + 1
    
    return result
    