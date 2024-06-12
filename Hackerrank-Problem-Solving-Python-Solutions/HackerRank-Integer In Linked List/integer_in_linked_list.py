"""
2. Binary Number in a Linked List
A binary number is represented as a series of O's and 1's. In this challenge,
the series will be in the form of a singly-linked list. Each node instance, a LinkedListNode,
has a value, data, and a pointer to the next node, next. Given a reference to the head of
a singly-linked list, convert the binary number represented to a decimal number.
Example
Linked List
binary 0
0
null
Linked list corresponding to the binary number (010011)[2] or (19)[10].
Function Description
Complete the function getNumber in the editor below.
getNumber has the following parameter(s): binary: reference to the head of
a singly-linked list of binary digits
Returns:
int: a (long integer)[10] representation of the binary number

Constraints
• 1≤n≤64
• All LinkedListNode.data = {01}
• The described (integer)[2] < 264
▼Input Format for Custom Testing
Input from stdin will be processed as follows and passed to the function.
The first line contains an integer n, the size of the linked list binary.
Each of the next n lines contains an integer LinkedListNode.data[i] where 0 ≤ i<n.
▼Sample Case 0
Sample Input
STDIN
Function
7
→ binary[] size n = 7
Θ
→
binary LinkedListNode.data
[0, 0, 1, 1, 0, 1, 0]
0
1
1
0
1
0
Θ
Sample Output
26
Explanation
Linked List
binary 0 0
1
0
1
0
null
The linked list is given as input.
The linked list forms the binary number 0011010(0011010)[2] = (26) [10]
"""

import math
import os
import random
import re
import sys


class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node

        self.tail = node


def print_singly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)


class LinkedListNode():
    def __init__(self, value=0, next_node=None):
        self.val = value
        self.next = next_node


def getNumber(binary):
    """
# Complete the 'getNumber' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts INTEGER_SINGLY_LINKED_LIST binary as parameter.
#

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
    """
    decimal_number = 0
    current_node = binary

    # Traverse the linked list and calculate the decimal number
    while current_node is not None:
        # Multiply the current decimal number by 2 and add the value of the current node
        decimal_number = decimal_number * 2 + current_node.data
        current_node = current_node.next

    return decimal_number


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    binary_count = int(input().strip())

    binary = SinglyLinkedList()

    for _ in range(binary_count):
        binary_item = int(input().strip())
        binary.insert_node(binary_item)

    result = getNumber(binary.head)

    fptr.write(str(result) + '\n')

    fptr.close()
