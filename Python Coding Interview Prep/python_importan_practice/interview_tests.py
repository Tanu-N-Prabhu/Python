# remove adjacent duplicate chars
def reduce_string(string):
    try:

        # make the string lower case
        string = string.lower()
        l = len(string)
        # no need to process if the string len is 0 or 1
        if l == 0 or l == 1:
            return string

        # make it a list
        ls = list(string)
        matched_pairs = []
        previous = None
        # loop thorugh all chars of string as list
        for i in range(0, l):
            if ls[i] == previous:
                # adjacent duplicate or pair
                matched_pairs.append(ls[(i-1)] + ls[i])
            else:
                previous = ls[i]

        # now need to remove duplicate pair chars from string
        for i in matched_pairs:
            string = string.replace(i, '')

        # if still
        if len(matched_pairs) > 0:
            string = reduce_string(string)

    except:
        return -1

    return string


# swap left right of middle number and sum all digits of number
def swap_sum(num):
    try:
        l = len(str(num))
        # check length and odd or not
        if l < 3 or l % 2 == 0:
            return -1

        # middle number index in list
        middle_index = l // 2
        num_as_list = [int(i) for i in str(num)]

        # swapping
        temp = num_as_list[(middle_index - 1)]
        num_as_list[(middle_index - 1)] = num_as_list[(middle_index + 1)]
        num_as_list[(middle_index + 1)] = temp

        # sum of the all digits of num
        sum_num = sum(num_as_list)
    except:
        return -1

    return sum_num


# how many chocolates can get against total money, price of each chocolate
# discount number of wrappers need for each chocolate
def get_chocolates(money, price, discount):
    if type(money) != int or type(price) != int or type(discount) != int:
        return -1
    elif money < 0 or price < 0 or discount < 0:
        return -1
    elif price > money:
        return 0

    chocolate_first = money // price
    wrappers_discount = chocolate_first // discount
    total_chocolates = chocolate_first + wrappers_discount

    print(chocolate_first)
    print(wrappers_discount)
    print(total_chocolates)


"""
k th largest element
input:
arr = [4,2,9,7,5,6,7,1,3]
k = 4
output:
6
explanation:
1st larget 9
2nd largest 7
3rd largest 7
4th largest 6

T(n,k) = O(n+k log n)

other way:
n = len(arr)
arr.sort()
arr[n-k]
"""
import heapq
def kth_largest(arr, k):
    arr = [-elem for elem in arr]
    heapq.heapify(arr)
    for i in range(k - 1):
        heapq.heappop(arr)
    return -heapq.heappop(arr)


"""
Symetric trees 
conditions: 
root1 = root2
root1.left_sub_tree = root2. right_sub_tree
root1.right_sub_tree = root2.left_sub_tree
T(n) = O(n)
S(n) = O(log n)
"""
def are_symmetric(root1, root2):
    if root1 is None or root2 is None:
        return True
    elif ((root1 is None) != (root2 is None)) or root1.val != root2.val:
        return False
    else:
        return are_symmetric(root1.left, root2.right) and are_symmetric(root1.right, root2.left)

def is_symmetric(root):
    if root is None:
        return True
    return are_symmetric(root.left, root.right)

"""
Generate parentheses
Given an integer n,
generate all the valid combinations of n
pairs of parentheses
by stack

Input:
n = 3
Output:
["((()))", "(()())", "(())()", "()(())", "()()()"]
T(n) = O(n * 2n)
S(n) = O(n * 2n)
"""
def generate(n):   
    # n = how many combinations
    # diff = differences between opening and closing parentheses
    # comb = one pair[open and close] of parentheses  
    # combs = main combinations stack
    def rec(n, diff, comb, combs):
        # it should not be - or > n
        if diff < 0 or diff > n:
            return False
        elif n == 0:
            if diff == 0:
                # one combination of parentheses created
                combs.append(''.join(comb))
        else:
            # add opening parentheses
            comb.append('(')
            # one combination less than current n 
            # diff increased as opening parentheses added
            rec(n - 1, diff + 1, comb, combs)
            comb.pop()
            comb.append(')')
            # one combination less than current n 
            # diff increased as closing parentheses added
            rec(n - 1, diff - 1, comb, combs)
            comb.pop()
    combs = []
    # number of pairs not the number of parentheses
    # that why 2 * n instead of n
    rec(2 * n, 0, [], combs)
    return combs

l = generate(3)
print(l)

def is_valid(combinations):
    """
    stack of parentheses are valid or not
    """
    stack = []
    for par in combinations:
        if par == '(':
            stack.append(par)
        else:
            # no pop from empty stack
            # otherwise means there is a ) without a (
            if len(stack) == 0:
                return False
            else:
                stack.pop()
    # stack must be empty
    # otherwise means it has ( without the )
    return len(stack) == 0
  
# driver code
for e in l:
    print(is_valid(e))



