# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    
    cumulative_sum = [0] * len(A)
    
    cumulative_sum[0] = A[0]

    for i in range( 1, len(A) ):
        cumulative_sum[i] = cumulative_sum[i-1] + A[i]
    
    # print(cumulative_sum)
    
    total_passing = 0

    for i in range( len(A) ):
        if A[i] == 0: 
            passing = cumulative_sum[len(A)-1] - cumulative_sum[i]
            total_passing += passing
            if total_passing > 1000000000:
                return -1
    
    return total_passing
