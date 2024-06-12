"""
A linked list of length n is given such that each node contains an additional random pointer, which could point to any node in the list, or null.

Construct a deep copy of the list. The deep copy should consist of exactly n brand new nodes, where each new node has its value set to the value of its corresponding original node. Both the next and random pointer of the new nodes should point to new nodes in the copied list such that the pointers in the original list and copied list represent the same list state. None of the pointers in the new list should point to nodes in the original list.

For example, if there are two nodes X and Y in the original list, where X.random --> Y, then for the corresponding two nodes x and y in the copied list, x.random --> y.

Return the head of the copied linked list.

The linked list is represented in the input/output as a list of n nodes. Each node is represented as a pair of [val, random_index] where:

val: an integer representing Node.val
random_index: the index of the node (range from 0 to n-1) that the random pointer points to, or null if it does not point to any node.
Your code will only be given the head of the original linked list.



Example 1:


Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]
Example 2:


Input: head = [[1,1],[2,1]]
Output: [[1,1],[2,1]]
Example 3:



Input: head = [[3,null],[3,0],[3,null]]
Output: [[3,null],[3,0],[3,null]]


Constraints:

0 <= n <= 1000
-104 <= Node.val <= 104
Node.random is null or is pointing to some node in the linked list.
"""


# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return None

        # Step 1: Create a new node for each original node and append it to the original list.
        current = head
        while current:
            new_node = Node(current.val)
            new_node.next = current.next
            current.next = new_node
            current = new_node.next

        # Step 2: Update the random pointers in the new list.
        current = head
        while current:
            if current.random:
                current.next.random = current.random.next
            current = current.next.next

        # Step 3: Separate the original list and the new list.
        current = head
        new_head = head.next
        new_current = new_head
        while new_current.next:
            current.next = new_current.next
            current = current.next
            new_current.next = current.next
            new_current = new_current.next

        current.next = None  # Set the next pointer of the last node in the original list to None.

        return new_head


# Helper function to create a sample linked list with random pointers
def create_sample_linked_list():
    # Create nodes
    node1 = Node(7)
    node2 = Node(13)
    node3 = Node(11)
    node4 = Node(10)
    node5 = Node(1)

    # Set next pointers
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5

    # Set random pointers
    node1.random = None
    node2.random = node1
    node3.random = node5
    node4.random = node3
    node5.random = node1

    return node1


# Helper function to print the linked list
def print_linked_list(head):
    current = head
    while current:
        random_val = current.random.val if current.random else None
        print(f"Value: {current.val}, Random: {random_val}")
        current = current.next


solution = Solution()
original_list = create_sample_linked_list()
copied_list = solution.copyRandomList(original_list)

print("Original List:")
print_linked_list(original_list)

print("\nCopied List:")
print_linked_list(copied_list)
