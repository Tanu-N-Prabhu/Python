# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

import math

def solution(N, P, Q):
    # write your code in Python 3.6
    
    # 1
    # find primes: use 'Sieve of Eratosthenes'
    prime_list = []
    # put all values
    # be careful about the range
    for index in range( 2, N+1 ):
        prime_list.append(index)
    #print(prime_list)

    # 2
    # remove 'not prime'
    # be careful about the range
    for item in range( 2, math.floor(math.sqrt(N))+1 ):
        not_prime_first = item + item
        for not_prime in range( not_prime_first, N+1, item ):
            if not_prime in prime_list:
                prime_list.remove(not_prime)
    #print(prime_list)

    # 3
    # find semi-primes
    semiprime_list = []
    for i in range( len(prime_list) ):
        for j in range( i, len(prime_list) ):
            semiprime = prime_list[i] * prime_list[j] 
            if semiprime <= N:
                semiprime_list.append(semiprime)
    semiprime_list.sort()
    #print(semiprime_list)
    
    # 4
    # count the number of semi-primes
    count_semiprime_list = [0] * (N+1)
    num_semiprime_so_far = 0
    for i in range(N+1):
        if i in semiprime_list:
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
