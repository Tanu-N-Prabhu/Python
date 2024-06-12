"""
Given a string s, return the longest
palindromic

substring
 in s.



Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"


Constraints:

1 <= s.length <= 1000
s consist of only digits and English letters.
"""


class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        start = 0
        max_len = 1

        # Create a table to store whether substrings are palindromes
        dp = [[False] * n for _ in range(n)]

        # All substrings of length 1 are palindromes
        for i in range(n):
            dp[i][i] = True

        # Check for substrings of length 2
        for i in range(n - 1):
            if s[i] == s[i + 1]:
                dp[i][i + 1] = True
                start = i
                max_len = 2

        # Check for longer substrings
        for curr_len in range(3, n + 1):
            for i in range(n - curr_len + 1):
                j = i + curr_len - 1

                if s[i] == s[j] and dp[i + 1][j - 1]:
                    dp[i][j] = True
                    if curr_len > max_len:
                        start = i
                        max_len = curr_len

        return s[start:start + max_len]


# Test code
solution = Solution()

# Test case 1
s1 = "babad"
result1 = solution.longestPalindrome(s1)
print("Test case 1 result:", result1)  # Expected output: "bab" or "aba"

# Test case 2
s2 = "cbbd"
result2 = solution.longestPalindrome(s2)
print("Test case 2 result:", result2)  # Expected output: "bb"
