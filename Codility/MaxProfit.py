# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    
    # key point: try to use only one for-loop O(n)
    
    if len(A)==0:
        return 0
    
    max_profit = 0
    min_price = A[0]
    
    for item in A:
        max_profit = max( max_profit, item - min_price )
        min_price = min( min_price, item )

    return max_profit
