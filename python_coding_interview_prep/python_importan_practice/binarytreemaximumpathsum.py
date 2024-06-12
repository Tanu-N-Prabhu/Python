"""
A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.

The path sum of a path is the sum of the node's values in the path.

Given the root of a binary tree, return the maximum path sum of any non-empty path.



Example 1:


Input: root = [1,2,3]
Output: 6
Explanation: The optimal path is 2 -> 1 -> 3 with a path sum of 2 + 1 + 3 = 6.
Example 2:


Input: root = [-10,9,20,null,null,15,7]
Output: 42
Explanation: The optimal path is 15 -> 20 -> 7 with a path sum of 15 + 20 + 7 = 42.


Constraints:

The number of nodes in the tree is in the range [1, 3 * 104].
-1000 <= Node.val <= 1000
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        # Initialize the maximum path sum as negative infinity
        max_path_sum = float('-inf')

        def find_max_path_sum(node):
            nonlocal max_path_sum

            if not node:
                return 0

            # Calculate the maximum path sum starting from the left and right subtrees
            left_sum = max(find_max_path_sum(node.left), 0)
            right_sum = max(find_max_path_sum(node.right), 0)

            # Calculate the maximum path sum starting from the current node
            node_sum = node.val + left_sum + right_sum

            # Update the global maximum path sum
            max_path_sum = max(max_path_sum, node_sum)

            # Return the maximum path sum starting from the current node
            return node.val + max(left_sum, right_sum)

        find_max_path_sum(root)
        return max_path_sum


# Example 1
root1 = TreeNode(1, TreeNode(2), TreeNode(3))
solution = Solution()
print(solution.maxPathSum(root1))  # Output should be 6

# Example 2
root2 = TreeNode(-10, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
solution = Solution()
print(solution.maxPathSum(root2))  # Output should be 42
