"""
Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.

You may not alter the values in the list's nodes, only nodes themselves may be changed.



Example 1:


Input: head = [1,2,3,4,5], k = 2
Output: [2,1,4,3,5]
Example 2:


Input: head = [1,2,3,4,5], k = 3
Output: [3,2,1,4,5]


Constraints:

The number of nodes in the list is n.
1 <= k <= n <= 5000
0 <= Node.val <= 1000


Follow-up: Can you solve the problem in O(1) extra memory space?
"""
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        def reverse(head, k):
            prev = None
            current = head
            while k > 0:
                next_node = current.next
                current.next = prev
                prev = current
                current = next_node
                k -= 1
            return prev

        def get_length(head):
            length = 0
            while head:
                length += 1
                head = head.next
            return length

        length = get_length(head)
        if length < k:
            return head

        dummy = ListNode(0)
        dummy.next = head
        prev_group_tail = dummy

        while length >= k:
            group_head = head
            group_tail = head
            for _ in range(k):
                group_tail = group_tail.next
            new_head = reverse(group_head, k)
            prev_group_tail.next = new_head
            group_head.next = group_tail
            head = group_tail
            prev_group_tail = group_head
            length -= k

        return dummy.next


# Sample usage
solution = Solution()
head1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))
k1 = 2
result1 = solution.reverseKGroup(head1, k1)
while result1:
    print(result1.val, end=" -> ")
    result1 = result1.next

