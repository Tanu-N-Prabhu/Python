# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S):
    # write your code in Python 3.6
    
    my_stack = []
    
    # note: use 'insert(index, item)' and 'pop(index)'
    
    for char in S: 
        if char == '{' or char == '[' or char == '(':
            my_stack.insert( len(my_stack), char) 
    
        # note: check if the stack is empty or not (be careful)
        if len(my_stack) == 0:
            return 0
        elif char == ')':
            pop = my_stack.pop( len(my_stack)-1 )
            if pop != '(':
                return 0
        elif char == ']':
            pop = my_stack.pop( len(my_stack)-1 )
            if pop != '[':
                return 0
        elif char == '}':
            pop = my_stack.pop( len(my_stack)-1 )
            if pop != '{':
                return 0
    
    # note: check if the stack is empty or not (be careful)
    if len(my_stack)!=0:
        return 0
    else:
        return 1
