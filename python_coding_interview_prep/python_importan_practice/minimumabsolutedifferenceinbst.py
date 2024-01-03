"""
Given the root of a Binary Search Tree (BST), return the minimum absolute difference between the values of any two different nodes in the tree.



Example 1:


Input: root = [4,2,6,1,3]
Output: 1
Example 2:


Input: root = [1,0,48,null,null,12,49]
Output: 1


Constraints:

The number of nodes in the tree is in the range [2, 104].
0 <= Node.val <= 105
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        def in_order_traversal(node):
            nonlocal prev, min_diff
            if not node:
                return
            in_order_traversal(node.left)
            if prev is not None:
                min_diff = min(min_diff, abs(node.val - prev))
            prev = node.val
            in_order_traversal(node.right)

        prev = None
        min_diff = float('inf')
        in_order_traversal(root)
        return min_diff


# Example 1
root1 = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(6))
solution = Solution()
print(solution.getMinimumDifference(root1))  # Output should be 1

# Example 2
root2 = TreeNode(1, TreeNode(0), TreeNode(48, None, TreeNode(12, None, TreeNode(49))))
solution = Solution()
print(solution.getMinimumDifference(root2))  # Output should be 1
