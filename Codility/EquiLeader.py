# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    
    # key point: 
    # the equi-leader 'must' be leader in A

    # step 1: find the leader in A
    
    my_dictionary = {}
    
    for item in A:
        my_dictionary[item] = 0
        
    for item in A:
        my_dictionary[item] += 1 
    
    have_leader = False
    leader_value = -1
    
    for item in A:
        if my_dictionary[item] > float( len(A) / 2):
            have_leader = True
            leader_value = item
    
    if have_leader == False:
        return 0
    
    # step 2: number of equi-leaders
    
    leader_count = []
    num_leader = 0
    
    for item in A:
        if item == leader_value:
            num_leader += 1
            leader_count.append(num_leader)
        else:
            leader_count.append(num_leader)
    
    # print(leader_count)
    
    num_equi_leader = 0
    
    for index in range( len(A) ):
        total_num_leader = leader_count[len(A)-1]
        left_num_leader = leader_count[index]
        right_num_leader = total_num_leader - left_num_leader
        left_leader_threshold = float( (index+1) / 2)
        right_leader_threshold = float( (len(A)-index-1) / 2)
        if left_num_leader > left_leader_threshold and right_num_leader > right_leader_threshold:
            num_equi_leader += 1
    
    return num_equi_leader
    