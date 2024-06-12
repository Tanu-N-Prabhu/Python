# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    
    my_dictionary = {}
    
    for item in A:
        if item not in my_dictionary:
            my_dictionary[item] = 1
    
    # print(my_dictionary)

    for i in range(1, len(A)+1 ):
        if i not in my_dictionary:
            return i
    
    return len(A)+1
