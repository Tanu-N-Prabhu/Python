# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    
    my_dictionary = {}
    odd_element = -1
    
    # create dictionary
    for item in A:
        my_dictionary[item] = 0 
    
    # counting
    for item in A:
        my_dictionary[item] += 1
    
    # find odd element
    for key in my_dictionary:
        if (my_dictionary[key] % 2 != 0):
            odd_element = key
    
    return odd_element
