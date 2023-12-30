"""
Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

The left
subtree
 of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.


Example 1:


Input: root = [2,1,3]
Output: true
Example 2:


Input: root = [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.


Constraints:

The number of nodes in the tree is in the range [1, 104].
-231 <= Node.val <= 231 - 1
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def in_order_traversal(node):
            nonlocal prev
            if not node:
                return True
            if not in_order_traversal(node.left):
                return False
            if prev is not None and node.val <= prev:
                return False
            prev = node.val
            return in_order_traversal(node.right)

        prev = None
        return in_order_traversal(root)


# Example 1
root1 = TreeNode(2, TreeNode(1), TreeNode(3))
solution = Solution()
print(solution.isValidBST(root1))  # Output should be True

# Example 2
root2 = TreeNode(5, TreeNode(1), TreeNode(4, TreeNode(3), TreeNode(6)))
solution = Solution()
print(solution.isValidBST(root2))  # Output should be False
