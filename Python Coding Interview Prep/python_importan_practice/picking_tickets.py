"""
Picking tickets

Consider an array of n ticket prices, tickets.
A number, m is defined as the size of some subsequence of tickets, s
where each element covers an unbroken range of integers.
that is if the elements s are sorted, the absoulte difference between any elements j and
j + 1 is either 0 or 1.
Determine the max length of a subsequence chosen from the tickets array.

eg. tickets = [8,5,4,8,4]
valid subsequences sorted are {4, 4, 5} and {8, 8}
Theese subsequence have m values of 3 and 2, respectivly return 3.

input
maxtickets prices 1 <= n <= 10**5 and 1 <= tickets[i] <= 10**9
4
[4,13,2,3]
returns
max possible value of m
3
"""
def pickingNumbers(arr):
    result = 0
    checked = set()
    for i in range(len(arr)):
        if i not in checked:
            maxCount = max(arr.count(arr[i]) + arr.count(arr[i] + 1), arr.count(arr[i]) + arr.count(arr[i] - 1))
            if maxCount > result:
                result = maxCount
            checked.add(i)
    return result


n = int(input().strip())
arr = list(map(int, input().strip().split(' ')))
result = pickingNumbers(arr)
print(result)
