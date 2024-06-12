# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    
    my_dictionary = {}
    
    for item in A:
        temp = abs(item)
        if temp not in my_dictionary:
            my_dictionary[temp] = True 
    
    # print(my_dictionary)
    #print(len(my_dictionary))
    return len(my_dictionary)
