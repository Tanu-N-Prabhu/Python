"""
Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.



Example 1:


Input: root = [3,1,4,null,2], k = 1
Output: 1
Example 2:


Input: root = [5,3,6,2,4,null,null,1], k = 3
Output: 3


Constraints:

The number of nodes in the tree is n.
1 <= k <= n <= 104
0 <= Node.val <= 104


Follow up: If the BST is modified often (i.e., we can do insert and delete operations) and you need to find the kth smallest frequently, how would you optimize?
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        def in_order_traversal(node):
            nonlocal count, result
            if not node:
                return
            in_order_traversal(node.left)
            count += 1
            if count == k:
                result = node.val
                return
            in_order_traversal(node.right)

        count = 0
        result = None
        in_order_traversal(root)
        return result


# Example 1
root1 = TreeNode(3, TreeNode(1, None, TreeNode(2)), TreeNode(4))
solution = Solution()
print(solution.kthSmallest(root1, 1))  # Output should be 1

# Example 2
root2 = TreeNode(5, TreeNode(3, TreeNode(2, TreeNode(1)), TreeNode(4)), TreeNode(6))
solution = Solution()
print(solution.kthSmallest(root2, 3))  # Output should be 3
