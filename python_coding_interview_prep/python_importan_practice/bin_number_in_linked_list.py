"""
Binary number in a linked list
should be 2**64
Binary number will be in the form of a single linked list
Each node instance is a linkedlistnode, has a value, data, and a pointer to the next node next.
Given a reference to the head of a singly linked list, convert the binary number
represented to a decimal number.
eg. 0->1->0->0->1->1->null will be 19[10] decimal

input
7
[0,0,1,1,0,1,0]
output
26
"""

class ListNode:
   def __init__(self, data, next = None):
      self.val = data
      self.next = next

def make_list(elements):
   head = ListNode(elements[0])
   for element in elements[1:]:
      ptr = head
      while ptr.next:
         ptr = ptr.next
      ptr.next = ListNode(element)
   return head

class Solution:
   def solve(self, node):
      l = []
      while node:
         l.append(node.val)
         node=node.next
      k = 0
      v=0
      for i in range(len(l)-1,-1,-1):
         if (l[i]==1):
            v += (2**k)
         k+=1
      return v
      
ob = Solution()
head = make_list([1,0,1,1,0])
print(ob.solve(head))