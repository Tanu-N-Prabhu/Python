# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(X, A):
    # write your code in Python 3.6
    
    my_set = set()
    
    for value in range(1, X+1):
        my_set.add( value )

    for index in range(0, len(A) ):
        if A[index] in my_set:
            my_set.remove( A[index] )
        if my_set == set():
            return index
    
    return -1
