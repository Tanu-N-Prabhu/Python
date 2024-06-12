# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(X, Y, D):
    # write your code in Python 3.6
    
    distance = Y - X 
    
    num_jump_float = float(distance / D) 
    num_jump_int = int(distance / D)

    num_jump_need = num_jump_int
    if num_jump_float > num_jump_int:
        num_jump_need += 1
    
    return num_jump_need

