# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A, B):
    # write your code in Python 3.6

    # the array is already sorted by B (the right end)
    
	# special cases (zero or only one)
    if len(A) == 0:
        return 0
    elif len(A) == 1:
        return 1
    
	# keep 'the current right-end' and 'the current left-end'
    current_right_end = B[0]
    current_left_end = A[0]
    
    num_non_overlapping = 1
    
    for index in range( len(A) ):
        current_left_end = A[index] # moving the left-end
        if current_left_end > current_right_end:
            num_non_overlapping += 1
            current_right_end = B[index] # update the right-end
    
    return num_non_overlapping
