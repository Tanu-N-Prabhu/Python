"""
Given the head of a singly linked list and two integers left and right where left <= right, reverse the nodes of the list from position left to position right, and return the reversed list.



Example 1:


Input: head = [1,2,3,4,5], left = 2, right = 4
Output: [1,4,3,2,5]
Example 2:

Input: head = [5], left = 1, right = 1
Output: [5]


Constraints:

The number of nodes in the list is n.
1 <= n <= 500
-500 <= Node.val <= 500
1 <= left <= right <= n


Follow up: Could you do it in one pass?
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        if not head or left == right:
            return head

        dummy = ListNode(0)  # Create a dummy node to simplify the edge cases
        dummy.next = head
        prev = dummy  # The node before the left node

        # Move the pointer to the left position
        for i in range(left - 1):
            prev = prev.next

        # Initialize pointers for the sublist
        current = prev.next
        next_node = None

        # Reverse the sublist from left to right
        for i in range(right - left + 1):
            next_temp = current.next
            current.next = next_node
            next_node = current
            current = next_temp

        # Connect the reversed sublist with the surrounding nodes
        prev.next.next = current
        prev.next = next_node

        return dummy.next


# Function to create a linked list from a list of values
def create_linked_list(values):
    dummy = ListNode(0)
    current = dummy
    for val in values:
        current.next = ListNode(val)
        current = current.next
    return dummy.next


# Function to convert a linked list to a list
def linked_list_to_list(head):
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result


# Test cases
solution = Solution()

# Test case 1
head1 = create_linked_list([1, 2, 3, 4, 5])
left1, right1 = 2, 4
result1 = solution.reverseBetween(head1, left1, right1)
assert linked_list_to_list(result1) == [1, 4, 3, 2, 5]

# Test case 2
head2 = create_linked_list([5])
left2, right2 = 1, 1
result2 = solution.reverseBetween(head2, left2, right2)
assert linked_list_to_list(result2) == [5]

print("All test cases passed!")





