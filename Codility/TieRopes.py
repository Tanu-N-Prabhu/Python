# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

import copy

def solution(K, A):
    # write your code in Python 3.6
    
    all_rope_list = []
    
    current_length = 0
    current_rope_list = []
    for item in A:
        current_length += item
        current_rope_list.append(item)
        # print(current_length)
        if current_length >= K:
            current_length = 0
            # all_rope_list.append( current_rope_list ) 
            # very important: need to use 'copy.copy()' for the current list 
            # print(current_rope_list)
            all_rope_list.append( copy.copy(current_rope_list) )
            # print(all_rope_list)
            current_rope_list.clear()
    
    num_rope = len(all_rope_list)
    return num_rope
