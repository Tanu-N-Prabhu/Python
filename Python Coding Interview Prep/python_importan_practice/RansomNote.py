"""
Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.



Example 1:

Input: ransomNote = "a", magazine = "b"
Output: false
Example 2:

Input: ransomNote = "aa", magazine = "ab"
Output: false
Example 3:

Input: ransomNote = "aa", magazine = "aab"
Output: true


Constraints:

1 <= ransomNote.length, magazine.length <= 105
ransomNote and magazine consist of lowercase English letters.
"""
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # Create a dictionary to count character occurrences in magazine
        char_count = {}
        for char in magazine:
            char_count[char] = char_count.get(char, 0) + 1

        # Check if we can construct ransomNote
        for char in ransomNote:
            if char_count.get(char, 0) > 0:
                char_count[char] -= 1
            else:
                return False

        return True

# Create a Solution instance
solution = Solution()

# Test cases
print(solution.canConstruct("a", "b"))  # Output: False
print(solution.canConstruct("aa", "ab"))  # Output: False
print(solution.canConstruct("aa", "aab"))  # Output: True
