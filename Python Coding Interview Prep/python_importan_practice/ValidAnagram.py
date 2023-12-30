"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.



Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false


Constraints:

1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.


Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?
"""


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        char_count = [0] * 26  # Assuming lowercase English letters

        for char in s:
            char_count[ord(char) - ord('a')] += 1

        for char in t:
            char_count[ord(char) - ord('a')] -= 1
            if char_count[ord(char) - ord('a')] < 0:
                return False

        return True


# Create an instance of the Solution class
solution = Solution()

# Test case 1
s1 = "anagram"
t1 = "nagaram"
result1 = solution.isAnagram(s1, t1)
print(f"Test case 1: {result1} (Expected: True)")

# Test case 2
s2 = "rat"
t2 = "car"
result2 = solution.isAnagram(s2, t2)
print(f"Test case 2: {result2} (Expected: False)")

# Additional test cases
s3 = "listen"
t3 = "silent"
result3 = solution.isAnagram(s3, t3)
print(f"Test case 3: {result3} (Expected: True)")

s4 = "hello"
t4 = "world"
result4 = solution.isAnagram(s4, t4)
print(f"Test case 4: {result4} (Expected: False)")

s5 = "abcde"
t5 = "edcba"
result5 = solution.isAnagram(s5, t5)
print(f"Test case 5: {result5} (Expected: True)")
