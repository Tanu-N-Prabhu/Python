"""
Given the head of a linked list, remove the nth node from the end of the list and return its head.



Example 1:


Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
Example 2:

Input: head = [1], n = 1
Output: []
Example 3:

Input: head = [1,2], n = 1
Output: [1]


Constraints:

The number of nodes in the list is sz.
1 <= sz <= 30
0 <= Node.val <= 100
1 <= n <= sz


Follow up: Could you do this in one pass?
"""
import unittest

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        fast = slow = dummy

        # Move the fast pointer n nodes ahead
        for i in range(n + 1):
            fast = fast.next

        # Move both fast and slow pointers until fast reaches the end
        while fast:
            fast = fast.next
            slow = slow.next

        # Remove the nth node from the end
        slow.next = slow.next.next

        return dummy.next


# Define a helper function to create a linked list from a list of values
def create_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

# Define a helper function to convert a linked list to a list of values
def linked_list_to_list(head):
    values = []
    current = head
    while current:
        values.append(current.val)
        current = current.next
    return values

class TestRemoveNthFromEnd(unittest.TestCase):
    def test_case1(self):
        solution = Solution()
        input_head = create_linked_list([1, 2, 3, 4, 5])
        n = 2
        expected_output = create_linked_list([1, 2, 3, 5])
        result = solution.removeNthFromEnd(input_head, n)
        self.assertEqual(linked_list_to_list(result), linked_list_to_list(expected_output))

    def test_case2(self):
        solution = Solution()
        input_head = create_linked_list([1])
        n = 1
        expected_output = None  # Removing the only node
        result = solution.removeNthFromEnd(input_head, n)
        self.assertEqual(linked_list_to_list(result), linked_list_to_list(expected_output))

    def test_case3(self):
        solution = Solution()
        input_head = create_linked_list([1, 2])
        n = 1
        expected_output = create_linked_list([1])
        result = solution.removeNthFromEnd(input_head, n)
        self.assertEqual(linked_list_to_list(result), linked_list_to_list(expected_output))

if __name__ == '__main__':
    unittest.main()
