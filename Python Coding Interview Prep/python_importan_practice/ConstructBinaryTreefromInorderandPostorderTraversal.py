"""
Given two integer arrays inorder and postorder where inorder is the inorder traversal of a binary tree and postorder is the postorder traversal of the same tree, construct and return the binary tree.



Example 1:


Input: inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]
Output: [3,9,20,null,null,15,7]
Example 2:

Input: inorder = [-1], postorder = [-1]
Output: [-1]


Constraints:

1 <= inorder.length <= 3000
postorder.length == inorder.length
-3000 <= inorder[i], postorder[i] <= 3000
inorder and postorder consist of unique values.
Each value of postorder also appears in inorder.
inorder is guaranteed to be the inorder traversal of the tree.
postorder is guaranteed to be the postorder traversal of the tree.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, inorder, postorder):
        if not inorder or not postorder:
            return None

        root_val = postorder.pop()
        root = TreeNode(root_val)
        inorder_idx = inorder.index(root_val)

        root.right = self.buildTree(inorder[inorder_idx + 1:], postorder)
        root.left = self.buildTree(inorder[:inorder_idx], postorder)

        return root


# Example usage:
inorder = [9, 3, 15, 20, 7]
postorder = [9, 15, 7, 20, 3]
solution = Solution()
tree = solution.buildTree(inorder, postorder)

# You can traverse the 'tree' and check the result.
