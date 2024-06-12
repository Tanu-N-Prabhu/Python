# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    
    my_sorted = sorted(A)
    
    possible_max_1 = my_sorted[len(A)-1] * my_sorted[len(A)-2] * my_sorted[len(A)-3] 
    possible_max_2 = my_sorted[0] * my_sorted[1] * my_sorted[len(A)-1] 
    
    max_product = max(possible_max_1, possible_max_2)

    return max_product
