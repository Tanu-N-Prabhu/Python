# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(H):
    # write your code in Python 3.6
    
    # key point: two different cases
    # case 1: from high to low
    # case 2: from low to high 
    
    # use stack
    my_stack = []
    
    num_block = 0 

    for i in range( len(H) ):
        
		# "stack is not empty" and "from high to low"; 
		# then, "pop" (it is the key point)
        while ( len(my_stack) !=0 ) and ( H[i] < my_stack[len(my_stack)-1] ):
            my_stack.pop( len(my_stack)-1 )
        
		# empty (stack)
        if len(my_stack) == 0:
            num_block += 1
            my_stack.append(H[i])
        
		# the height is the same
        elif H[i] == my_stack[ len(my_stack)-1 ] :
            # do nothing (no need to add any block)
            pass
        
		# from low to high
        elif H[i] >= my_stack[ len(my_stack)-1 ] :
            num_block += 1 
            my_stack.append(H[i])

    return num_block
