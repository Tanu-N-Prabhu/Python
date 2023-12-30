"""
Given a string s consisting of words and spaces, return the length of the last word in the string.

A word is a maximal
substring
 consisting of non-space characters only.



Example 1:

Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5.
Example 2:

Input: s = "   fly me   to   the moon  "
Output: 4
Explanation: The last word is "moon" with length 4.
Example 3:

Input: s = "luffy is still joyboy"
Output: 6
Explanation: The last word is "joyboy" with length 6.


Constraints:

1 <= s.length <= 104
s consists of only English letters and spaces ' '.
There will be at least one word in s.
"""


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # Split the string into words
        words = s.split()

        # Check if there are any words
        if words:
            # Return the length of the last word
            return len(words[-1])
        else:
            return 0


# Example usage
if __name__ == "__main__":
    solution = Solution()
    s1 = "Hello World"
    s2 = "   fly me   to   the moon  "
    s3 = "luffy is still joyboy"
    print(solution.lengthOfLastWord(s1))  # Expected output: 5
    print(solution.lengthOfLastWord(s2))  # Expected output: 4
    print(solution.lengthOfLastWord(s3))  # Expected output: 6

