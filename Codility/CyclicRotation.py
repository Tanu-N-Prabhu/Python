# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A, K):
    # write your code in Python 3.6
    
    # initialize array [0, 0, ..., 0] 
    temp_array = [0] * len(A)
    
    for index in range( len(A) ) :
        new_index = (index + K) % len(A) # new position
        temp_array[new_index] = A[index] # set value
    
    return temp_array
