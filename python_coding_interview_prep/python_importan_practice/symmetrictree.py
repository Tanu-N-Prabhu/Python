"""
Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).



Example 1:


Input: root = [1,2,2,3,4,4,3]
Output: true
Example 2:


Input: root = [1,2,2,null,3,null,3]
Output: false


Constraints:

The number of nodes in the tree is in the range [1, 1000].
-100 <= Node.val <= 100


Follow up: Could you solve it both recursively and iteratively?
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def isMirror(left, right):
            # Base case: if both nodes are None, they are symmetric
            if not left and not right:
                return True
            # If only one node is None or their values are different, not symmetric
            if not left or not right or left.val != right.val:
                return False
            # Check recursively if subtrees are symmetric
            return isMirror(left.left, right.right) and isMirror(left.right, right.left)

        if not root:
            return True  # An empty tree is considered symmetric
        return isMirror(root.left, root.right)


# Example usage:
# Create a symmetric binary tree
symmetric_tree = TreeNode(1)
symmetric_tree.left = TreeNode(2)
symmetric_tree.right = TreeNode(2)
symmetric_tree.left.left = TreeNode(3)
symmetric_tree.left.right = TreeNode(4)
symmetric_tree.right.left = TreeNode(4)
symmetric_tree.right.right = TreeNode(3)

solution = Solution()
print(solution.isSymmetric(symmetric_tree))  # Output: True

# You can create your own tree or modify the 'symmetric_tree' for testing.
