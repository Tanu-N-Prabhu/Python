"""
Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:

Starting with any positive integer, replace the number by the sum of the squares of its digits.
Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy.
Return true if n is a happy number, and false if not.



Example 1:

Input: n = 19
Output: true
Explanation:
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1
Example 2:

Input: n = 2
Output: false


Constraints:

1 <= n <= 231 - 1
"""


class Solution:
    def isHappy(self, n: int) -> bool:
        def get_sum_of_squares(num):
            total = 0
            while num > 0:
                digit = num % 10
                total += digit * digit
                num //= 10
            return total

        seen_numbers = set()
        while n != 1:
            n = get_sum_of_squares(n)
            if n in seen_numbers:
                return False  # Detected a cycle
            seen_numbers.add(n)
        return True

# Create an instance of the Solution class
solution = Solution()

# Test cases
test_cases = [19, 2, 1, 100, 68]

for n in test_cases:
    is_happy = solution.isHappy(n)
    print(f"Number {n} is happy: {is_happy}")
    print(f"Number {n} is happy: {is_happy}")
