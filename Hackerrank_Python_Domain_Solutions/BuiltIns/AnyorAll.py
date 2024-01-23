"""
In summary, the entire expression evaluates to True if all elements in ar are positive integers and 
there is at least one palindrome in ar. Otherwise, it evaluates to False.
Problem   : https://www.hackerrank.com/challenges/any-or-all/problem
"""

n = input()
ar = input().split()
# This condition checks if all elements in the iterable ar are greater than 0 when converted to integers. 
# It returns True if this condition is satisfied for all elements; otherwise, it returns False.
# This condition checks if there is at least one element in the iterable ar that is a palindrome 
# (reads the same backward as forward). It returns True if there is at least one palindrome; 
# otherwise, it returns False.
print(all(int(i) > 0 for i in ar) and any(i == i[::-1] for i in ar))
