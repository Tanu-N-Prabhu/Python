"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".



Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.


Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters.
"""


class Solution:
    def longestCommonPrefix(self, strs):
        # Check for empty input
        if not strs:
            return ""

        # Find the shortest string in the list
        min_len = min(len(s) for s in strs)

        # Initialize the common prefix
        common_prefix = ""

        for i in range(min_len):
            char = strs[0][i]

            # Check if the character is common to all strings
            if all(s[i] == char for s in strs):
                common_prefix += char
            else:
                break

        return common_prefix


# Example usage
if __name__ == "__main__":
    solution = Solution()
    strs1 = ["flower", "flow", "flight"]
    strs2 = ["dog", "racecar", "car"]
    print(solution.longestCommonPrefix(strs1))  # Expected output: "fl"
    print(solution.longestCommonPrefix(strs2))  # Expected output: ""
