# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(M, A):
    # write your code in Python 3.6
    
	# try to remember which value was counted
    current_dictionary = {} 
    
    len_A = len(A)
    count_slice = 0
    begin = 0
    end = 0
    
    # cbombine the two loops (using one while loop)
    while (begin < len_A) and (end < len_A):
        # distinct value (end +=1)
        if A[end] not in current_dictionary:
            current_dictionary[ A[end] ] = 1
            # super important: not just plus 1 (the key to be faster)
            count_slice += (end - begin +1)
            if count_slice > 1_000_000_000:
                return 1_000_000_000
            end +=1
        # smae value
        else:
			# the same value happens (begin +=1)
            # important: remove the value of begin
            current_dictionary.pop(A[begin])
            begin+=1

    return count_slice
