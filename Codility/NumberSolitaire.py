# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

import sys

def solution(A):
    # write your code in Python 3.6

    len_a = len(A)
    
	# initialize 'dp' as [ A[0], 0, 0, ..., 0] 
    dp = [A[0]] + ([0]*(len_a-1))
    
    # print(dp)

	# build up 'dp' (bottom-up)
    for index in range(1, len_a):
        
		# note: the min_int is '(-sys.maxsize)-1'
        temp_max = (-sys.maxsize)-1

		# there might be '6' possible combination (at most) 
        for die_number in range(1, 6+1):
            if index-die_number >= 0:
                temp_max = max( dp[index-die_number] + A[index], temp_max ) # super important!
        
		# keep the max (temp_max)
        dp[index] = temp_max
    
    # print(dp)

	# return the last one
    return dp[len_a-1]
    