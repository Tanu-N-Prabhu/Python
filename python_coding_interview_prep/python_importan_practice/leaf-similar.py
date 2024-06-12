"""
Consider all the leaves of a binary tree, from left to right order, the values of those leaves form a leaf value sequence.



For example, in the given tree above, the leaf value sequence is (6, 7, 4, 9, 8).

Two binary trees are considered leaf-similar if their leaf value sequence is the same.

Return true if and only if the two given trees with head nodes root1 and root2 are leaf-similar.



Example 1:


Input: root1 = [3,5,1,6,2,9,8,null,null,7,4], root2 = [3,5,1,6,7,4,2,null,null,null,null,null,null,9,8]
Output: true
Example 2:


Input: root1 = [1,2,3], root2 = [1,3,2]
Output: false
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    @staticmethod
    def leafSimilar(root1, root2):
        # Helper function to perform DFS and collect leaf nodes
        def collect_leaf_nodes(node, leaf_sequence):
            if node:
                if not node.left and not node.right:
                    leaf_sequence.append(node.val)
                collect_leaf_nodes(node.left, leaf_sequence)
                collect_leaf_nodes(node.right, leaf_sequence)

        # Collect leaf sequences for both trees
        leaf_sequence1 = []
        collect_leaf_nodes(root1, leaf_sequence1)

        leaf_sequence2 = []
        collect_leaf_nodes(root2, leaf_sequence2)

        # Compare the leaf sequences
        return leaf_sequence1 == leaf_sequence2


