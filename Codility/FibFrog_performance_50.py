# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    
    #test_A = [1,1,1,1,1,1,1]
    #result = my_solution(test_A)
    #print(result)
    #print('end')
    
    result = my_solution(A)
    return result
    
def my_solution(A):
    len_river = len(A)
    
    fabonacci = []
    fabonacci.append(0)
    fabonacci.append(1)
    index = 1 
    while fabonacci[index] <= len_river:
        index += 1
        temp = fabonacci[index-1] + fabonacci[index-2]
        fabonacci.append(temp)    
    
    # print(fabonacci)
    # fabonacci = fabonacci[:-1] # remove the last element
    fabonacci = fabonacci[::-1] # reverse a list in Python
    # print(fabonacci)

    my_queue = []
    my_dictionary = {-1:0} # position:-1, steps:0
    my_queue.append(my_dictionary)
    # print(my_queue)
    # print(len(my_queue))

    index = 0 
    while True:
        
        # cannot take element from queue anymore
        if len(my_queue)==index:
            # print( len(my_queue) )
            # print( index )
            return -1
        
        # get from queue
        temp_dictionary = my_queue[index]
        # print(temp_dictionary)
        
        # get key and value
        for key in temp_dictionary:
            current_position = key
            current_step = temp_dictionary[key]
            # print(current_position)
            # print(current_step)
        
        # from big to small
        for item in fabonacci:
            
            next_position = current_position + item
            
            # reach the other side
            if next_position == len_river:
                current_step += 1
                return current_step
            
            # can not jump
            elif next_position > len_river:
                pass
            elif next_position < 0 :
                pass
            elif A[next_position] ==0:
                pass
            
            # jump to next position
            else:
                current_step += 1
                temp_dictionary = {next_position: current_step}
                my_queue.append(temp_dictionary)
                
                A[next_position] = 0 # important
            
        index += 1 # take "next element" from queue
        