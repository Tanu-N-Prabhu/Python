"""
Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.



Example 1:


Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).
Example 2:


Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.
Example 3:


Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.


Constraints:

The number of the nodes in the list is in the range [0, 104].
-105 <= Node.val <= 105
pos is -1 or a valid index in the linked-list.


Follow up: Can you solve it using O(1) (i.e. constant) memory?
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False

        tortoise = head
        hare = head

        while hare and hare.next:
            tortoise = tortoise.next
            hare = hare.next.next

            if tortoise == hare:
                return True

        return False


# Create a linked list with a cycle
values_with_cycle = [3, 2, 0, -4]
head_with_cycle = create_linked_list(values_with_cycle)
tail = head_with_cycle

while tail.next:
    tail = tail.next
tail.next = head_with_cycle.next  # Create a cycle

solution = Solution()
has_cycle = solution.hasCycle(head_with_cycle)
print("Linked list with cycle:", has_cycle)

# Create a linked list without a cycle
values_without_cycle = [1, 2]
head_without_cycle = create_linked_list(values_without_cycle)
no_cycle = solution.hasCycle(head_without_cycle)
print("Linked list without cycle:", no_cycle)
