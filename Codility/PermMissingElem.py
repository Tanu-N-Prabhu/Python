# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    
    N = len(A)
    
    my_list = [0] * (N+2)
    
    missing_element = -1
    
    for index in range(0, N): 
        my_list[ A[index] ] += 1
    
    for index in range(1, N+2):
        if my_list[ index ] == 0:
            missing_element = index

    return missing_element
