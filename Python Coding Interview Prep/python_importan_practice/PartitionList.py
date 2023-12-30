"""
Given the head of a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.



Example 1:


Input: head = [1,4,3,2,5,2], x = 3
Output: [1,2,2,4,3,5]
Example 2:

Input: head = [2,1], x = 2
Output: [1,2]


Constraints:

The number of nodes in the list is in the range [0, 200].
-100 <= Node.val <= 100
-200 <= x <= 200
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        # Create two dummy nodes for the two partitions
        less_head = ListNode(0)
        greater_head = ListNode(0)
        less = less_head
        greater = greater_head

        current = head

        while current:
            if current.val < x:
                less.next = current
                less = less.next
            else:
                greater.next = current
                greater = greater.next
            current = current.next

        # Connect the two partitions
        less.next = greater_head.next
        greater.next = None

        return less_head.next


# Create a linked list
node1 = ListNode(1)
node2 = ListNode(4)
node3 = ListNode(3)
node4 = ListNode(2)
node5 = ListNode(5)
node6 = ListNode(2)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6

# Create an instance of the Solution class
solution = Solution()

# Partition the linked list with x = 3
x = 3
new_head = solution.partition(node1, x)

# Print the partitioned linked list
current = new_head
while current:
    print(current.val, end=" -> ")
    current = current.next
print("None")
