# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    
    #special case:
    if (len(A) <= 3):
        return 0
    
    # main idea: 
    # use "golden slice algorithm" O(n)
    # take maxEnding[i] = max( 0, maxEnding[i-1] + A[i] ) <--- important~!!
    # explanation : 
    # At the end of each slice, we decide whether its value 
    # is going to be carried to the next element's computation 
    # based on whether the value is "negative or positive". <--- "key point" 
    # If positive, we carry it (so it contributes to the next slice)
    # Otherwise we start from "0"
    
    #(X, Y, Z)
    # 1st slice: A[X+1] + ... + A[Y-1] 
    # 2nd slice: A[Y+1] + ... + A[Z-1]
    # Key Point:
    # The array will be split at "Y" 
    # main idea:
    # if the middle point is "Y",
    # find "maxLeft" and "maxRight"
        
    maxLeft = [0] * len(A)
    maxRight = [0] * len(A)
        
    # 1) find "maxLeft"
    # maxLeft[i] is the maximum sum "contiguous subsequence" ending at index i 
    # note: because it is "contiguous", we only need the ending index (important)
    
    for index in range( 1, len(A) ):
    # be careful: from i=1 (because of maxLeft[i-1])
        maxLeft[index] = max(0, maxLeft[index-1]+A[index] ); 
        # golden slice algorithm: max(0, maxLeft[i-1]+A[i] )
        
    # 2) find "maxRight"
    for index in range( len(A)-2, -1, -1 ):
    # be careful: from i=A.length-2 (because of maxLeft[i+1])
        maxRight[index] = max(0, maxRight[index+1]+A[index] );
        # golden slice algorithm: Math.max(0, maxRight[i+1]+A[i] )
        
    # 3) find the maximum of "maxLeft + maxRight"
    maxDoubleSlice = A[1] + A[len(A)-2];
    for index in range( 1, len(A)-1 ):
        if (maxLeft[index-1] + maxRight[index+1]) > maxDoubleSlice:
            maxDoubleSlice = maxLeft[index-1] + maxRight[index+1]
            #print(maxLeft[index-1])
            #print(maxRight[index+1])
            # be careful: "not" maxLeft[i] + maxRight[i]
            # left end at "i-1", and right begins at "i+1"

    return maxDoubleSlice;
