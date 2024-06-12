# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A, B):
    # write your code in Python 3.6
    
    L = len(A)
    max_is_sufficient = max(A)
    
    # compute num of ways (by using Fibonacci)
    dictionary_num_ways = {}
    dictionary_num_ways[1] = 1
    dictionary_num_ways[2] = 2 # 1+1 or 2
    for x in range(3, max_is_sufficient+1, 1):
        dictionary_num_ways[x] = dictionary_num_ways[x-1] + dictionary_num_ways[x-2]
        # dictionary_num_ways[x-1] + '1'
        # or
        # dictionary_num_ways[x-2] + '2'
        dictionary_num_ways[x] = dictionary_num_ways[x] % (2 ** 30)
        # note: very important (to be quick in the extreme_large case)
    
    # compute results ( num_ways % (2 ** B[index]) )
    result = [0] * L
    for index in range(L):
        num_ways = dictionary_num_ways[ A[index] ]
        each_result = num_ways % ( 2 ** B[index] ) 
        result[index] = each_result
    
    return result
