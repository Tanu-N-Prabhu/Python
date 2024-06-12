# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A, B, K):
    # write your code in Python 3.6
    
    # need to achieve low complexity O(1)
    # using math equation (low complexity)

    # number of divisible values smaller than B
    num_B = B // K
    # note: take "Math.floor" which is the basic number
    
    # number of divisible values smaller than A
    num_A = A // K
    # note: take "Math.floor" which is the basic number
    
    # number of divisible numbers
    num_divisible = num_B - num_A
    
    # note: plus one (if A % K == 0)
    # because "A" is also divisble 
    plus = 0
    if A % K ==0:
        plus =1
    
    num_divisible = num_divisible + plus
            
    return num_divisible
    