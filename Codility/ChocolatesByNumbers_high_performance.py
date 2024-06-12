# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N, M):
    # write your code in Python 3.6
    
    # key:
    # meet in the circle = number of chocolates that you will eat
    #  number of chocolates = N / gcd(N, M)
    num_chocolates = N // gcd(N,M)
    
    return num_chocolates

# find gcd (greatest common divisor)
def gcd(a, b):
    if a % b == 0:
        return b
    else:
        return gcd(b, a%b)
