"""
A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:

Every adjacent pair of words differs by a single letter.
Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
sk == endWord
Given two words, beginWord and endWord, and a dictionary wordList, return the number of words in the shortest transformation sequence from beginWord to endWord, or 0 if no such sequence exists.



Example 1:

Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
Output: 5
Explanation: One shortest transformation sequence is "hit" -> "hot" -> "dot" -> "dog" -> cog", which is 5 words long.
Example 2:

Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
Output: 0
Explanation: The endWord "cog" is not in wordList, therefore there is no valid transformation sequence.


Constraints:

1 <= beginWord.length <= 10
endWord.length == beginWord.length
1 <= wordList.length <= 5000
wordList[i].length == beginWord.length
beginWord, endWord, and wordList[i] consist of lowercase English letters.
beginWord != endWord
All the words in wordList are unique.
"""

from collections import deque


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet = set(wordList)  # Convert the wordList to a set for faster lookup
        if endWord not in wordSet:
            return 0  # If endWord is not in wordList, there's no valid sequence.

        queue = deque([(beginWord, 1)])  # Initialize a queue with the starting word and its level
        visited = set()  # Create a set to keep track of visited words

        while queue:
            word, level = queue.popleft()  # Dequeue the word and its level
            if word == endWord:
                return level  # If we've reached the endWord, return the level

            for i in range(len(word)):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    nextWord = word[:i] + c + word[i+1:]  # Generate all possible words
                    if nextWord in wordSet and nextWord not in visited:
                        visited.add(nextWord)
                        queue.append((nextWord, level + 1))  # Enqueue the nextWord with an increased level

        return 0  # If we exhausted all possibilities and couldn't reach endWord, return 0

# Example usage:
solution = Solution()
beginWord = "hit"
endWord = "cog"
wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
result = solution.ladderLength(beginWord, endWord, wordList)
print(result)  # Output: 5

