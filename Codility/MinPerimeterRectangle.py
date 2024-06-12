# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

import math

def solution(N):
    # write your code in Python 3.6
    
    my_perimeter_list = []
    
    for n in range( 1, int(math.sqrt(N))+1 ): 
        if( N % n ==0):
            one_side = n
            another_side = int( N/n )
            perimeter = 2 * (one_side + another_side) 
            my_perimeter_list.append(perimeter)
    
    min_perimeter = min( my_perimeter_list )
    
    return min_perimeter
