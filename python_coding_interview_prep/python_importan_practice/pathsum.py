"""
Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.

A leaf is a node with no children.



Example 1:


Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
Output: true
Explanation: The root-to-leaf path with the target sum is shown.
Example 2:


Input: root = [1,2,3], targetSum = 5
Output: false
Explanation: There two root-to-leaf paths in the tree:
(1 --> 2): The sum is 3.
(1 --> 3): The sum is 4.
There is no root-to-leaf path with sum = 5.
Example 3:

Input: root = [], targetSum = 0
Output: false
Explanation: Since the tree is empty, there are no root-to-leaf paths.


Constraints:

The number of nodes in the tree is in the range [0, 5000].
-1000 <= Node.val <= 1000
-1000 <= targetSum <= 1000
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        # Base case: If the root is None, return False.
        if not root:
            return False

        # Subtract the value of the current node from the targetSum.
        targetSum -= root.val

        # If it's a leaf node and targetSum becomes 0, return True.
        if not root.left and not root.right and targetSum == 0:
            return True

        # Recursively check the left and right subtrees.
        left_path = self.hasPathSum(root.left, targetSum)
        right_path = self.hasPathSum(root.right, targetSum)

        # Return True if there's a path in either the left or right subtree.
        return left_path or right_path


# Example 1
root1 = TreeNode(5, TreeNode(4, TreeNode(11, TreeNode(7), TreeNode(2))), TreeNode(8, TreeNode(13), TreeNode(4, None, TreeNode(1))))
solution = Solution()
print(solution.hasPathSum(root1, 22))  # Output should be True

# Example 2
root2 = TreeNode(1, TreeNode(2), TreeNode(3))
solution = Solution()
print(solution.hasPathSum(root2, 5))  # Output should be False

# Example 3
root3 = None
solution = Solution()
print(solution.hasPathSum(root3, 0))  # Output should be False
