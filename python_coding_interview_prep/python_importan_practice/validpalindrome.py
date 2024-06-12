"""
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.



Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
Example 3:

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.


Constraints:

1 <= s.length <= 2 * 105
s consists only of printable ASCII characters.
"""


class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Convert to lowercase and remove non-alphanumeric characters
        s = ''.join(c.lower() for c in s if c.isalnum())

        # Check if it's a palindrome
        return s == s[::-1]


# Example usage
if __name__ == "__main__":
    solution = Solution()
    s1 = "A man, a plan, a canal: Panama"
    s2 = "race a car"
    s3 = " "

    result1 = solution.isPalindrome(s1)
    result2 = solution.isPalindrome(s2)
    result3 = solution.isPalindrome(s3)

    print(result1)  # Output: True
    print(result2)  # Output: False
    print(result3)  # Output: True

