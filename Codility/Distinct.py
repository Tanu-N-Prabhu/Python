# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    
    my_dictionary = {}
    for item in A:
        if item not in my_dictionary:
            my_dictionary[item] = True 

    # print(my_dictionary)

    num_distinct = len(my_dictionary)    

    return num_distinct
