"""
Given the head of a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list. Return the linked list sorted as well.



Example 1:


Input: head = [1,2,3,3,4,4,5]
Output: [1,2,5]
Example 2:


Input: head = [1,1,1,2,3]
Output: [2,3]


Constraints:

The number of nodes in the list is in the range [0, 300].
-100 <= Node.val <= 100
The list is guaranteed to be sorted in ascending order.
"""
import unittest

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Create a dummy node to serve as the new head
        dummy = ListNode(0)
        dummy.next = head
        current = dummy

        while current.next and current.next.next:
            if current.next.val == current.next.next.val:
                # Remove nodes with duplicate values
                val = current.next.val
                while current.next and current.next.val == val:
                    current.next = current.next.next
            else:
                current = current.next

        return dummy.next


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Helper function to create a linked list from a list of values
def create_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head


# Helper function to convert a linked list to a list of values
def linked_list_to_list(head):
    values = []
    current = head
    while current:
        values.append(current.val)
        current = current.next
    return values


class TestDeleteDuplicates(unittest.TestCase):
    def test_case1(self):
        solution = Solution()
        input_head = create_linked_list([1, 2, 3, 3, 4, 4, 5])
        expected_output = create_linked_list([1, 2, 5])
        result = solution.deleteDuplicates(input_head)
        self.assertEqual(linked_list_to_list(result), linked_list_to_list(expected_output))

    def test_case2(self):
        solution = Solution()
        input_head = create_linked_list([1, 1, 1, 2, 3])
        expected_output = create_linked_list([2, 3])
        result = solution.deleteDuplicates(input_head)
        self.assertEqual(linked_list_to_list(result), linked_list_to_list(expected_output))


if __name__ == '__main__':
    unittest.main()
