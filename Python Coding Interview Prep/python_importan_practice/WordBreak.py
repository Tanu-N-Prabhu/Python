"""
Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in the segmentation.



Example 1:

Input: s = "leetcode", wordDict = ["leet","code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
Example 2:

Input: s = "applepenapple", wordDict = ["apple","pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
Note that you are allowed to reuse a dictionary word.
Example 3:

Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: false


Constraints:

1 <= s.length <= 300
1 <= wordDict.length <= 1000
1 <= wordDict[i].length <= 20
s and wordDict[i] consist of only lowercase English letters.
All the strings of wordDict are unique.
"""


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True

        word_set = set(wordDict)

        for i in range(1, n + 1):
            for j in range(i):
                if dp[j] and s[j:i] in word_set:
                    dp[i] = True
                    break

        return dp[n]


# Test code
solution = Solution()

# Test case 1
s1 = "leetcode"
wordDict1 = ["leet", "code"]
result1 = solution.wordBreak(s1, wordDict1)
print("Test case 1 result:", result1)  # Expected output: True

# Test case 2
s2 = "applepenapple"
wordDict2 = ["apple", "pen"]
result2 = solution.wordBreak(s2, wordDict2)
print("Test case 2 result:", result2)  # Expected output: True

# Test case 3
s3 = "catsandog"
wordDict3 = ["cats", "dog", "sand", "and", "cat"]
result3 = solution.wordBreak(s3, wordDict3)
print("Test case 3 result:", result3)  # Expected output: False

