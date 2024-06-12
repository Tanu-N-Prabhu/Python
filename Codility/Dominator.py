# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    
    my_dictionary = {}
    
    for item in A:
        my_dictionary[item] = 0 
        
    for item in A:
        my_dictionary[item] += 1
        
    # print(my_dictionary)

    have_dominator = False
    value_dominator = -1
    index_dominator = -1

    for index in range( len(A) ):
        if my_dictionary[ A[index] ] > float( len(A) / 2):
            have_dominator = True
            value_dominator = A[index]
            index_dominator = index

    if have_dominator == False:
        return -1
    else:
        return index_dominator
    