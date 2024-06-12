# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N, A):
    # write your code in Python 3.6

    num_counters = N    
    num_operations = len(A)
    
    my_list = [0] * N 
    
    max_value = 0
    min_value = 0
    
    for operation in A:
        
        if operation < N+1:
            
            if my_list[operation-1] < min_value:
                my_list[operation-1] = min_value
			
            if my_list[operation-1] == max_value:
                max_value += 1
                
            my_list[operation-1] += 1
        
			
        elif operation == N+1:
            #max_value = max(my_list)
            #my_list = [max_value] * N
            min_value = max_value
			
        # print(my_list)
    
    for i in range(num_counters):
        if my_list[i] < min_value:
            my_list[i] = min_value
	
    return my_list
