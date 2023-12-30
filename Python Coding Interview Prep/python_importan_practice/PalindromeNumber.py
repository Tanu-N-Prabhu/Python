"""
Given an integer x, return true if x is a
palindrome
, and false otherwise.



Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.


Constraints:

-231 <= x <= 231 - 1


Follow up: Could you solve it without converting the integer to a string?
"""


class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Negative numbers and numbers ending with 0 are not palindromes
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        reversed_half = 0
        while x > reversed_half:
            reversed_half = reversed_half * 10 + x % 10
            x //= 10

        # If the number has an odd number of digits, we need to remove the middle digit
        return x == reversed_half or x == reversed_half // 10


# Test cases
sol = Solution()
print(sol.isPalindrome(121))    # Output: True
print(sol.isPalindrome(-121))   # Output: False
print(sol.isPalindrome(10))     # Output: False
