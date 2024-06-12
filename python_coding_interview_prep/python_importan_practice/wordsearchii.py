"""
Given an m x n board of characters and a list of strings words, return all words on the board.

Each word must be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.



Example 1:


Input: board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], words = ["oath","pea","eat","rain"]
Output: ["eat","oath"]
Example 2:


Input: board = [["a","b"],["c","d"]], words = ["abcb"]
Output: []


Constraints:

m == board.length
n == board[i].length
1 <= m, n <= 12
board[i][j] is a lowercase English letter.
1 <= words.length <= 3 * 104
1 <= words[i].length <= 10
words[i] consists of lowercase English letters.
All the strings of words are unique.
"""


class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        def build_trie(words):
            root = TrieNode()
            for word in words:
                node = root
                for char in word:
                    if char not in node.children:
                        node.children[char] = TrieNode()
                    node = node.children[char]
                node.is_end_of_word = True
            return root

        def dfs(node, i, j, path):
            char = board[i][j]
            curr_node = node.children.get(char)
            if not curr_node:
                return

            path.append(char)
            board[i][j] = '#'  # Mark the cell as visited

            if curr_node.is_end_of_word:
                found_words.add("".join(path))

            for x, y in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                if 0 <= x < m and 0 <= y < n and board[x][y] in curr_node.children:
                    dfs(curr_node, x, y, path)

            board[i][j] = char  # Restore the cell
            path.pop()

        m, n = len(board), len(board[0])
        root = build_trie(words)
        found_words = set()

        for i in range(m):
            for j in range(n):
                if board[i][j] in root.children:
                    dfs(root, i, j, [])

        return list(found_words)


# Example usage
board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]
words = ["oath","pea","eat","rain"]

solution = Solution()
result = solution.findWords(board, words)
print(result)  # Output: ["eat", "oath"]
