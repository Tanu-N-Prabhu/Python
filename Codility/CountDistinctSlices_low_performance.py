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
    
    for begin in range(len_A):
        end = begin
        # print(begin)
        while end < len_A:
            # print(end)
            if A[end] not in current_dictionary:
                current_dictionary[ A[end] ] = 1
                count_slice += 1
                # print('count plus 1')
                if count_slice > 1_000_000_000:
                    return 1_000_000_000
                end +=1
            else:
				# the same value happens (begin +=1)
                current_dictionary = {}
                break
        
		# important:
		# begin will plus 1, and so we reset 'current_dictionary'
        current_dictionary = {}

    return count_slice
