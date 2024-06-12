
from collections import *

# how many pile 
T = int(input())

for i in range(T):
    # how long the pile
    n=int(input())
    # create list/pile from the input
    l = deque(map(int,input().split()))
    flag=0
    pile = None

    for i in range(n):
        last = l[len(l) - 1]
        if i == 0:
            # first one is >= last one
            max_index = 0
            if l[max_index] >= last:
                max = l[max_index]
                min = last
            else:
                max_index = len(l) - 1
                max = last
                min = l[0]
        else:
            if l[0] >= last and l[0] <= pile:
                max_index = 0
                max = l[max_index]
                min = last
            elif last >= l[0] and last <= pile:
                max_index = len(l) - 1
                max = last
                min = l[0]
            else:
                flag = 1
                break

        # current pile stack
        pile = max
        del l[max_index]
        print(l)

    if flag==1:
        print("No")
    else:
        print("Yes")