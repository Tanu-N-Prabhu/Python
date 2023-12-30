"""
Given the root of a complete binary tree, return the number of the nodes in the tree.

According to Wikipedia, every level, except possibly the last, is completely filled in a complete binary tree, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

Design an algorithm that runs in less than O(n) time complexity.



Example 1:


Input: root = [1,2,3,4,5,6]
Output: 6
Example 2:

Input: root = []
Output: 0
Example 3:

Input: root = [1]
Output: 1


Constraints:

The number of nodes in the tree is in the range [0, 5 * 104].
0 <= Node.val <= 5 * 104
The tree is guaranteed to be complete.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0

        left_height = self.get_height(root.left)
        right_height = self.get_height(root.right)

        if left_height == right_height:
            # Left subtree is perfect, use the formula to calculate total nodes
            return 2 ** left_height + self.countNodes(root.right)
        else:
            # Left subtree is not perfect, recursively count nodes in left and right subtrees
            return 2 ** right_height + self.countNodes(root.left)

    def get_height(self, node):
        height = 0
        while node:
            height += 1
            node = node.left
        return height


# Example 1
root1 = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, TreeNode(6)))
solution = Solution()
print(solution.countNodes(root1))  # Output should be 6

# Example 2
root2 = None
solution = Solution()
print(solution.countNodes(root2))  # Output should be 0

# Example 3
root3 = TreeNode(1)
solution = Solution()
print(solution.countNodes(root3))  # Output should be 1
