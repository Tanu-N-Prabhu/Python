# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

import math

def solution(N, P, Q):
    # write your code in Python 3.6
    
    # 1
    # find primes: use 'Sieve of Eratosthenes'
    prime_list_boolean = [True] * (N+1) # note: plus one for "0"
    prime_list_boolean[0] = False   
    prime_list_boolean[1] = False
    for i in range( 2, math.floor(math.sqrt(N))+1 ):
        if prime_list_boolean[i] == True:
            j = i + i
            for not_prime in range( j, N+1, i ):
                prime_list_boolean[not_prime] = False
    
    # 2
    # append 'prime' to list
    prime_list = []
    for index in range( N+1 ):
        if prime_list_boolean[index] == True:
            prime_list.append(index)
    # print(prime_list)
    
    # 3
    # find semi-primes
    semiprime_list_boolean = [False] * (N+1) # note: plus one for "0"
    for i in range( len(prime_list) ):
        for j in range(i, len(prime_list), 1):
            semiprime_temp = prime_list[i] * prime_list[j] 
            if semiprime_temp > N:
                break
            else:
                semiprime_list_boolean[semiprime_temp] = True

    # 4
    # count the number of semi-primes
    count_semiprime_list = [0] * (N+1)
    num_semiprime_so_far = 0
    for i in range(N+1):
        if semiprime_list_boolean[i]==True:
            num_semiprime_so_far += 1
        count_semiprime_list[i] = num_semiprime_so_far
    #print(count_semiprime_list)
    
    # 5
    # return answers to all the queries
    answer_list = [0] * len(P)
    for i in range( len(P) ):
        begin_value = P[i]
        end_value = Q[i]
        #print(count_semiprime_list[end_value])
        #print(count_semiprime_list[begin_value])
        # be very careful about the 'begin_value' (not included)
        answer_list[i] = count_semiprime_list[end_value] - count_semiprime_list[ (begin_value-1) ]
    #print(answer_list)
    
    return answer_list
