"""
Given a pattern and a string s, find if s follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.



Example 1:

Input: pattern = "abba", s = "dog cat cat dog"
Output: true
Example 2:

Input: pattern = "abba", s = "dog cat cat fish"
Output: false
Example 3:

Input: pattern = "aaaa", s = "dog cat cat dog"
Output: false


Constraints:

1 <= pattern.length <= 300
pattern contains only lower-case English letters.
1 <= s.length <= 3000
s contains only lowercase English letters and spaces ' '.
s does not contain any leading or trailing spaces.
All the words in s are separated by a single space.
"""


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()

        if len(pattern) != len(words):
            return False

        pattern_to_word = {}
        word_to_pattern = {}

        for char, word in zip(pattern, words):
            if char in pattern_to_word and pattern_to_word[char] != word:
                return False
            if word in word_to_pattern and word_to_pattern[word] != char:
                return False

            pattern_to_word[char] = word
            word_to_pattern[word] = char

        return True


# Create an instance of the Solution class
solution = Solution()

# Test case 1
pattern1 = "abba"
s1 = "dog cat cat dog"
result1 = solution.wordPattern(pattern1, s1)
print(f"Test case 1: {result1} (Expected: True)")

# Test case 2
pattern2 = "abba"
s2 = "dog cat cat fish"
result2 = solution.wordPattern(pattern2, s2)
print(f"Test case 2: {result2} (Expected: False)")

# Test case 3
pattern3 = "aaaa"
s3 = "dog cat cat dog"
result3 = solution.wordPattern(pattern3, s3)
print(f"Test case 3: {result3} (Expected: False)")
