# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S, P, Q):
    # write your code in Python 3.6
    
    cumulative_A = [0] * ( len(S) +1 )
    cumulative_C = [0] * ( len(S) +1 )
    cumulative_G = [0] * ( len(S) +1 )
    # cumulative_T = [0] * len(S)
    
    for i in range( len(S) ):
        
        if S[i] == 'A':
            cumulative_A[i+1] = cumulative_A[i] + 1
            cumulative_C[i+1] = cumulative_C[i]
            cumulative_G[i+1] = cumulative_G[i]
        elif S[i] == 'C':
            cumulative_A[i+1] = cumulative_A[i]
            cumulative_C[i+1] = cumulative_C[i] + 1
            cumulative_G[i+1] = cumulative_G[i]    
        elif S[i] == 'G':
            cumulative_A[i+1] = cumulative_A[i]
            cumulative_C[i+1] = cumulative_C[i]
            cumulative_G[i+1] = cumulative_G[i] + 1
        else:
            cumulative_A[i+1] = cumulative_A[i]
            cumulative_C[i+1] = cumulative_C[i]
            cumulative_G[i+1] = cumulative_G[i]
    
    #print(cumulative_A)
    #print(cumulative_C)
    #print(cumulative_G)

    M = len(P) # =len(Q)
    
    result = [0] * M
    
    for j in range( M ):
        
        start_position = P[j]
        end_position = Q[j] + 1 # inclusive
        
        num_A = cumulative_A[end_position] - cumulative_A[start_position]
        num_C = cumulative_C[end_position] - cumulative_C[start_position]
        num_G = cumulative_G[end_position] - cumulative_G[start_position]
        
        if num_A > 0:
            result[j] = 1
        elif num_C > 0:
            result[j] = 2
        elif num_G > 0:
            result[j] = 3
        else:
            result[j] = 4
    
    return result

        
