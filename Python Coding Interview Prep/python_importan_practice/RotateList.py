"""
Given the head of a linked list, rotate the list to the right by k places.



Example 1:


Input: head = [1,2,3,4,5], k = 2
Output: [4,5,1,2,3]
Example 2:


Input: head = [0,1,2], k = 4
Output: [2,0,1]


Constraints:

The number of nodes in the list is in the range [0, 500].
-100 <= Node.val <= 100
0 <= k <= 2 * 109
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k == 0:
            return head

        # Find the length of the linked list and the last node
        length = 1
        current = head
        while current.next:
            current = current.next
            length += 1
        last_node = current

        # Calculate the effective rotations (k % length)
        k = k % length
        if k == 0:
            return head

        # Find the new tail (the node just before the new head)
        current = head
        for _ in range(length - k - 1):
            current = current.next

        # Update the pointers to rotate the list
        new_head = current.next
        current.next = None
        last_node.next = head

        return new_head


# Create nodes and linked list
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
head = node1

# Create an instance of the Solution class
solution = Solution()

# Rotate the linked list
k = 2
new_head = solution.rotateRight(head, k)

# Print the rotated linked list
current = new_head
while current:
    print(current.val, end=" -> ")
    current = current.next
print("None")





