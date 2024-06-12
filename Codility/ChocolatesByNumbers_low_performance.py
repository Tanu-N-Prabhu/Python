# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N, M):
    # write your code in Python 3.6
    
    my_dictionary = {}
    
    current_value = 0 
    
    while current_value not in my_dictionary:
        my_dictionary[current_value] = 1 
        current_value = (current_value + M) % N 
    # print(my_dictionary)
    
    return len(my_dictionary)
