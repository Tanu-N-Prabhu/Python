# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N):
    # write your code in Python 3.6
    # using the "concept of bit manipulation" and "& operation"
    
    current_gap = 0
    max_gap = 0
    
    start_counting = False

    temp = N
    
    while temp > 0: 
        
        # case 1
        if (temp & 1 == 1): 
            # case 1-1
            if (start_counting == False):
                start_counting = True
            # case 1-2
            elif (start_counting == True):
                max_gap = max(max_gap, current_gap)
                current_gap = 0 #reset
        
        # case 2
        elif (temp & 1 == 0):
            if(start_counting == True):
                current_gap += 1
        
        # shift one bit (every loop)
        temp = temp >> 1
    
    return max_gap
    