# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

import math

def solution(N):
    # write your code in Python 3.6
    
    my_dictionary = {}

    # be careful about the range    
    # O(n)
    '''
    for n in range( 1, N+1 ):
        if N % n == 0:
            my_dictionary[n] = True
    '''
    
    # O( log(n) )
    # be careful: we need to check 'math.sqrt(N)+1'
    for n in range( 1, int( math.sqrt(N) ) +1 ):
        if N % n ==0:
            my_dictionary[n] = True
            another_factor = int( N/n ) 
            my_dictionary[another_factor] = True
    
    # print(my_dictionary)
    
    num_factors = len( my_dictionary )
    
    return num_factors
