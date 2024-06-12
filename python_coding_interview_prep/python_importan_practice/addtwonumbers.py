"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.



Example 1:


Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]
Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]


Constraints:

The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading zeros.
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1, l2):
        carry = 0
        dummy = ListNode()
        current = dummy

        while l1 or l2:
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0

            _sum = x + y + carry
            carry = _sum // 10

            current.next = ListNode(_sum % 10)
            current = current.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        if carry > 0:
            current.next = ListNode(carry)

        return dummy.next


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


# Helper function to convert a linked list to a list for easy printing
def linked_list_to_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result


if __name__ == "__main__":
    # Create linked lists representing the two numbers
    num1 = [2, 4, 3]
    num2 = [5, 6, 4]

    l1 = create_linked_list(num1)
    l2 = create_linked_list(num2)

    solution = Solution()
    result = solution.addTwoNumbers(l1, l2)

    # Convert the result linked list to a list
    result_list = linked_list_to_list(result)

    print(result_list)  # This should print the result of adding the two numbers.

