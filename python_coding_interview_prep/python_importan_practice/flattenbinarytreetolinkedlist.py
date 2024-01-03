"""
Given the root of a binary tree, flatten the tree into a "linked list":

The "linked list" should use the same TreeNode class where the right child pointer points to the next node in the list and the left child pointer is always null.
The "linked list" should be in the same order as a pre-order traversal of the binary tree.


Example 1:


Input: root = [1,2,5,3,4,null,6]
Output: [1,null,2,null,3,null,4,null,5,null,6]
Example 2:

Input: root = []
Output: []
Example 3:

Input: root = [0]
Output: [0]


Constraints:

The number of nodes in the tree is in the range [0, 2000].
-100 <= Node.val <= 100


Follow up: Can you flatten the tree in-place (with O(1) extra space)?
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return

        if root.left:
            # Flatten the left subtree
            self.flatten(root.left)

            # Store the original right subtree
            right_subtree = root.right

            # Set the right subtree to be the left subtree and make the left subtree None
            root.right = root.left
            root.left = None

            # Traverse to the end of the new right subtree
            while root.right:
                root = root.right

            # Append the original right subtree
            root.right = right_subtree

        # Continue with the original right subtree
        self.flatten(root.right)


# Function to print the flattened linked list
def print_flattened_linked_list(head):
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.right
    print("None")

# Example 1
root1 = TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(4)), TreeNode(5, None, TreeNode(6)))
solution = Solution()
solution.flatten(root1)
print_flattened_linked_list(root1)  # Output should be [1 -> 2 -> 3 -> 4 -> 5 -> 6 -> None]

# Example 2
root2 = None
solution = Solution()
solution.flatten(root2)
print_flattened_linked_list(root2)  # Output should be []

# Example 3
root3 = TreeNode(0)
solution = Solution()
solution.flatten(root3)
print_flattened_linked_list(root3)  # Output should be [0 -> None]
