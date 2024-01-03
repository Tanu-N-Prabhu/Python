"""
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).



Example 1:

Input: s = "abc", t = "ahbgdc"
Output: true
Example 2:

Input: s = "axc", t = "ahbgdc"
Output: false


Constraints:

0 <= s.length <= 100
0 <= t.length <= 104
s and t consist only of lowercase English letters.


Follow up: Suppose there are lots of incoming s, say s1, s2, ..., sk where k >= 109, and you want to check one by one to see if t has its subsequence. In this scenario, how would you change your code?
"""


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # Initialize pointers for s and t
        i, j = 0, 0

        # Iterate through both strings
        while i < len(s) and j < len(t):
            # If the current characters match, move the pointer for s
            if s[i] == t[j]:
                i += 1
            # Always move the pointer for t
            j += 1

        # If we reached the end of s, s is a subsequence of t
        return i == len(s)


# Example usage
if __name__ == "__main__":
    solution = Solution()
    s1 = "abc"
    t1 = "ahbgdc"
    s2 = "axc"
    t2 = "ahbgdc"

    result1 = solution.isSubsequence(s1, t1)
    result2 = solution.isSubsequence(s2, t2)

    print(result1)  # Output: True
    print(result2)  # Output: False
