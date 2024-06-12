# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    
    lower = [0] * len(A)
    upper = [0] * len(A)
    
    # all the lower and upper points 
    for i in range( len(A) ):
        lower[i] = i - A[i]
        upper[i] = i + A[i]
    
    sorted_lower = sorted(lower)
    sorted_upper = sorted(upper)
    
    intersection = 0
    j = 0 # for lower points
    
    # scan the upper points
    for i in range( len(A) ):
        # scan the lower points with condition (note: sorted)
        while j < len(A) and sorted_upper[i] >= sorted_lower[j]:
            intersection += j
            intersection -= i
            j += 1
    
    if intersection > 10_000_000:
        return -1
    
    return intersection
    