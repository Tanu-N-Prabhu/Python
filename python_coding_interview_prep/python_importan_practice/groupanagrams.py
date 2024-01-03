"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.



Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Example 2:

Input: strs = [""]
Output: [[""]]
Example 3:

Input: strs = ["a"]
Output: [["a"]]


Constraints:

1 <= strs.length <= 104
0 <= strs[i].length <= 100
strs[i] consists of lowercase English letters.
"""


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_groups = {}

        for word in strs:
            sorted_word = ''.join(sorted(word))
            if sorted_word in anagram_groups:
                anagram_groups[sorted_word].append(word)
            else:
                anagram_groups[sorted_word] = [word]

        return list(anagram_groups.values())


# Instantiate the Solution class
solution = Solution()

# Test case 1
strs1 = ["eat", "tea", "tan", "ate", "nat", "bat"]
result1 = solution.groupAnagrams(strs1)
print(result1)  # Should print [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]

# Test case 2
strs2 = [""]
result2 = solution.groupAnagrams(strs2)
print(result2)  # Should print [[""]]

# Test case 3
strs3 = ["a"]
result3 = solution.groupAnagrams(strs3)
print(result3)  # Should print [["a"]]
