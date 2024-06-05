from typing import List
"""
Anagram Groups
Given an array of strings strs, group all anagrams together into sublists. You may return the output in any order.

An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

Example 1:

Input: strs = ["act","pots","tops","cat","stop","hat"]

Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]
Example 2:

Input: strs = ["x"]

Output: [["x"]]
Example 3:

Input: strs = [""]

Output: [[""]]
Constraints:

1 <= strs.length <= 1000.
0 <= strs[i].length <= 100
strs[i] is made up of lowercase English letters.
"""


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # create a dictionary to store the anagrams
        anagram_dict = {}

        # loop over all strs
        for word in strs:
            # sort the word and add it to the dictionary
            sorted_word = ''.join(sorted(word))
            # check if the sorted word is already in the dictionary
            if sorted_word in anagram_dict:
                # if it is, append the word to the list of anagrams
                anagram_dict[sorted_word].append(word)
            else:
                # if it is not, create a new list with the word
                anagram_dict[sorted_word] = [word]
        # return the list of anagrams
        return anagram_dict.values()


if __name__ == '__main__':
    s = Solution()
    strs = ["act", "pots", "tops", "cat", "stop", "hat"]
    print(s.groupAnagrams(strs))
