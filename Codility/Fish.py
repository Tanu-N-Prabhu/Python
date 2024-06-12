# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A, B):
    # write your code in Python 3.6
    
    downstream_stack = []
    
    n = len(A)
    
    num_alive = n
    
    for i in range(n):
        
        # downstream
        if B[i] == 1:
            downstream_stack.append( A[i] )
        
        # upstream
        if B[i] == 0:
            
            while len(downstream_stack) != 0:
                pop = downstream_stack.pop( len(downstream_stack)-1 )
                if pop >= A[i]:
                    num_alive -=1
                    downstream_stack.append(pop) # just push back
                    break
                elif pop < A[i]:
                    num_alive -=1
                    # keep looping (pop another downstrem fish)
        
    return num_alive
    