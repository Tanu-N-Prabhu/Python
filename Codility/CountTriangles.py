# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    
    my_list = A
    my_list.sort()
    # print(my_list)
    
    if len(A) < 3:
        return 0
    
    count_triangular = 0 

    for index_one in range( len(A) -2):
        index_two = index_one + 1
        index_three = index_one + 2
        while (index_two< len(A)-1):
            if ( index_three<len(A) ) and (my_list[index_one] + my_list[index_two] > my_list[index_three]) :
                index_three +=1
            else: 
                count_triangular += (index_three - index_two - 1)
                index_two += 1

    return count_triangular
