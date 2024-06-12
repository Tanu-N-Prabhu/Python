# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

import math

def solution(A):

    # count the elements of A (by using dictionary)
    my_dictionary_1 = {}
    for item in A:
        if item not in my_dictionary_1:
            my_dictionary_1[item] = 1
        else:
            my_dictionary_1[item] += 1
    # print(my_dictionary_1)
    
    # count the number of non-divisors (into dictionary_2)
    my_dictionary_2 = {}
    for item in my_dictionary_1:
        num_divisor = 0
        item_sqrt = math.floor(math.sqrt(item))
        # print( str(item) + ' , ' + str(item_sqrt) )
        for i in range(1, item_sqrt+1, 1):
            if (item % i ==0):
                another_divisor = item / i 
                
                if i in my_dictionary_1:
                    num_divisor = num_divisor + my_dictionary_1[i] 
                
                if another_divisor != i:
                    if another_divisor in my_dictionary_1:
                        num_divisor = num_divisor + my_dictionary_1[another_divisor]
                
        num_non_divisor = len(A) - num_divisor
        my_dictionary_2[item] = num_non_divisor
    # print(my_dictionary_2)
    
    # put the number of non-divisors into an 'array' (by using list)
    array_non_divisor = []
    for i in range( len(A) ):
        array_non_divisor.append( my_dictionary_2[A[i]] )
    
    return array_non_divisor
