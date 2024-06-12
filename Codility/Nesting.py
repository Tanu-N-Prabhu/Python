# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S):
    # write your code in Python 3.6
    
    my_stack = []
    
    for char in S:
        
        if char == '(':
            my_stack.append(char)
        
        elif char == ')':
            
            # note: check if the stack is empty or not (be careful)
            if len(my_stack) == 0:
                return 0
            
            else:
                pop = my_stack.pop( len(my_stack)-1 )
    
    # note: check if the stack is empty or not (be careful)
    if len(my_stack) != 0:
        return 0
    else:
        return 1
