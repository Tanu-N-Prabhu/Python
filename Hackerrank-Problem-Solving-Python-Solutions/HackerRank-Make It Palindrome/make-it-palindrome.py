"""
Problem Statement  :

You’re given a string, you’ve to print additional characters needed to make that string a palindrome.

A Palindrome is a sequence of characters that has the property of reading the same in either direction.

Input :
abede
Output :
ba

Sample Input :
abcfe

Sample output :
fcba
"""


# it will check the string is palindrome or not
def is_palindrome(s):
    # if string is same as its reverse
    return s == s[::-1]


# find the string require to make this string a palindrome
def make_palindrome(s):
	# if already a palindrome
    if is_palindrome(s):
        return None

    # loop through all character
    for i in range(len(s)):
    	# take till the current index and then reverse
        x = s[:i][::-1]
        print(x)
        # concat main string and x check if it is a palindrome
        if is_palindrome(s + x):
        	# then return only the x string require to make it palindrome
            return x


# Test the function
s = "abede"
print(make_palindrome(s))  # Output: ba

s = "abcfe"
print(make_palindrome(s))  # Output: fcba
