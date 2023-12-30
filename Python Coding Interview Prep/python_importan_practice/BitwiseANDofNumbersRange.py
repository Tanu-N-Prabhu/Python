"""
Given two integers left and right that represent the range [left, right], return the bitwise AND of all numbers in this range, inclusive.



Example 1:

Input: left = 5, right = 7
Output: 4
Example 2:

Input: left = 0, right = 0
Output: 0
Example 3:

Input: left = 1, right = 2147483647
Output: 0


Constraints:

0 <= left <= right <= 231 - 1
"""


class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        shift = 0
        while left < right:
            left >>= 1
            right >>= 1
            shift += 1
        return left << shift


# Test cases
sol = Solution()
print(sol.rangeBitwiseAnd(5, 7))            # Output: 4
print(sol.rangeBitwiseAnd(0, 0))            # Output: 0
print(sol.rangeBitwiseAnd(1, 2147483647))   # Output: 0
