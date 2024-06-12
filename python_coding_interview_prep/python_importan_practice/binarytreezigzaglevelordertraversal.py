"""
Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. (i.e., from left to right, then right to left for the next level and alternate between).



Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: [[3],[20,9],[15,7]]
Example 2:

Input: root = [1]
Output: [[1]]
Example 3:

Input: root = []
Output: []


Constraints:

The number of nodes in the tree is in the range [0, 2000].
-100 <= Node.val <= 100
"""
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []

        result = []
        queue = deque([root])
        level_number = 0  # To keep track of the level number

        while queue:
            level_size = len(queue)
            level_values = []

            for i in range(level_size):
                node = queue.popleft()

                if level_number % 2 == 0:
                    # For even levels, append values in the regular order
                    level_values.append(node.val)
                else:
                    # For odd levels, insert values at the beginning of the list
                    level_values.insert(0, node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            result.append(level_values)
            level_number += 1

        return result


# Example 1
root1 = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
solution = Solution()
print(solution.zigzagLevelOrder(root1))  # Output should be [[3], [20, 9], [15, 7]]

# Example 2
root2 = TreeNode(1)
solution = Solution()
print(solution.zigzagLevelOrder(root2))  # Output should be [[1]]

# Example 3
root3 = None
solution = Solution()
print(solution.zigzagLevelOrder(root3))  # Output should be []
