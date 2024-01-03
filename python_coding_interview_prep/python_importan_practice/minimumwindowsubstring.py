"""
Given two strings s and t of lengths m and n respectively, return the minimum window
substring
 of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.



Example 1:

Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
Example 2:

Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.
Example 3:

Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.
"""
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""

        t_count = {}
        for char in t:
            t_count[char] = t_count.get(char, 0) + 1

        required_chars = len(t_count)
        left, right = 0, 0
        formed_chars = 0
        min_len = float('inf')
        result = ""

        while right < len(s):
            if s[right] in t_count:
                t_count[s[right]] -= 1
                if t_count[s[right]] == 0:
                    formed_chars += 1

            while formed_chars == required_chars and left <= right:
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    result = s[left:right + 1]

                if s[left] in t_count:
                    t_count[s[left]] += 1
                    if t_count[s[left]] > 0:
                        formed_chars -= 1

                left += 1

            right += 1

        return result


if __name__ == "__main__":
    solution = Solution()
    s = "ADOBECODEBANC"
    t = "ABC"
    result = solution.minWindow(s, t)
    print(result)  # Output: "BANC"
