"""
Reverse Linked list in group of k 
"""

class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next

def reverse_k_group(head, k):
  """
  Reverses a linked list in groups of k elements and returns the new head.

  Args:
      head: The head node of the linked list.
      k: The group size for reversal.

  Returns:
      The head node of the reversed linked list.
  """

  curr = head
  prev = None

  while curr:
    count = 0
    temp_prev = None
    temp_next = None

    # Reverse the next k nodes
    while curr and count < k:
      temp_next = curr.next
      curr.next = temp_prev
      temp_prev = curr
      curr = temp_next
      count += 1

    # Connect the previous group with the reversed group
    if prev:
      prev.next = temp_prev
    else:
      head = temp_prev

    # Update pointers for the next iteration
    prev = temp_prev
    curr = temp_next

  return head

# Example usage
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
k = 2
new_head = reverse_k_group(head, k)

while new_head:
  print(new_head.val, end=" -> ")
  new_head = new_head.next
print("None")

