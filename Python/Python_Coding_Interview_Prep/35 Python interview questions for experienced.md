# Python Coding Interview Questions And Answers - Experienced

Here Coding compiler sharing a list of 35 Python interview questions for experienced. These Python questions are prepared by expert Python developers. This list of interview questions on Python will help you to crack your next Python job interview. All the best for your future and happy [python learning](https://codingcompiler.com/python-coding-interview-questions-answers/)

[![Hits](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2FTanu-N-Prabhu%2FPython%2Fblob%2Feb5b22ff1e660645bad4f88c89bed8dcba9388c4%2FPython%2520Coding%2520Interview%2520Prep%2F35%2520Python%2520interview%2520questions%2520for%2520experienced.md&count_bg=%2379C83D&title_bg=%23555555&icon=&icon_color=%23E7E7E7&title=hits&edge_flat=false)](https://hits.seeyoufarm.com)


## 1. Debugging a Python Program

```python
# By using this command we can debug a python program
python -m pdb python-script.py
```

---

## 2. Yield Keyword in Python
### The keyword in Python can turn any function into a generator. Yields work like a standard return keyword.

```python
def days(index):
    day = ['S','M','T','W','Tr','F','St']            
    yield day[index]    
    yield day[index+1]  
  
res = days(0)
print(next(res), next(res))

> S M
```
----

## 3. Converting a List into a String
### When we want to convert a list into a string, we can use the `<.join()>` method which joins all the elements into one and returns as a string.

```python
days = ['S','M','T','W','Tr','F','St'] 
ltos = ' '.join(days)
print(ltos)

> S M T W Tr F St
```
---

## 4. Converting a List into a Tuple
### By using Python `<tuple()>` function we can convert a list into a tuple. But we can’t change the list after turning it into tuple, because it becomes immutable.

```python
days = ['S','M','T','W','Tr','F','St'] 
ltos = tuple(days)
print(ltos)

> ('S', 'M', 'T', 'W', 'Tr', 'F', 'St')
```
---


## 5. Converting a List into a Set
### User can convert list into set by using `<set()>` function.

```python
days = ['S','M','T','W','Tr','F','St'] 
ltos = set(days)
print(ltos)

> {'T', 'W', 'M', 'F', 'S', 'Tr', 'St'}
```
---

## 6. Counting the occurrences of a particular element in the list
### We can count the occurrences of an individual element by using a `<count()>` function.

```python
days = ['S','M','W', 'M','M','F','S']

print(days.count('M'))

> 3
```
---

### 6.1. Counting the occurrences of elements in the list

```python
days = ['S','M','M','M','F','S']
y = set(days)

print([[x,days.count(x)] for x in y])

> [['M', 3], ['S', 2], ['F', 1]]
```

---

## 7. Creating a NumPy Array in Python
### NumPy arrays are more flexible then lists in Python.

```python
import numpy as np

arr = np.array([1, 2, 3, 4, 5])

print(arr)
print(type(arr))

> [1 2 3 4 5]
  <class 'numpy.ndarray'>
  
  ```
  ---

## 8. Implement a LRU (Least Recently Used) Cache

```python
from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity: int):
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        else:
            self.cache.move_to_end(key)
            return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)

# Example usage:
lru = LRUCache(2)
lru.put(1, 1)
lru.put(2, 2)
print(lru.get(1)) 
lru.put(3, 3)

> 1
```
---

## 9. Find the Longest Substring Without Repeating Characters

```python
def length_of_longest_substring(s: str) -> int:
    char_index_map = {}
    start = max_length = 0

    for i, char in enumerate(s):
        if char in char_index_map and char_index_map[char] >= start:
            start = char_index_map[char] + 1
        char_index_map[char] = i
        max_length = max(max_length, i - start + 1)

    return max_length

# Example usage:
print(length_of_longest_substring("abcabcbb"))

> 3

```
---

## 10. Find the Kth Largest Element in an Array

```python
import heapq

def find_kth_largest(nums: list, k: int) -> int:
    return heapq.nlargest(k, nums)[-1]

# Example usage:
print(find_kth_largest([3, 2, 1, 5, 6, 4], 2))

> 5

```

---

## 11. Detect a Cycle in a Linked List

```python

class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def has_cycle(head: ListNode) -> bool:
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False

# Example usage:
# Creating a linked list with a cycle for demonstration:
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node1.next = node2
node2.next = node3
node3.next = node1  # Cycle here
print(has_cycle(node1))

> True

```
---

## 12. Serialize and Deserialize a Binary Tree

```python

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Codec:
    def serialize(self, root: TreeNode) -> str:
        def dfs(node):
            if not node:
                result.append("None")
            else:
                result.append(str(node.val))
                dfs(node.left)
                dfs(node.right)
        result = []
        dfs(root)
        return ','.join(result)

    def deserialize(self, data: str) -> TreeNode:
        def dfs():
            val = next(values)
            if val == "None":
                return None
            node = TreeNode(int(val))
            node.left = dfs()
            node.right = dfs()
            return node
        values = iter(data.split(','))
        return dfs()

# Example usage:
codec = Codec()
tree = TreeNode(1, TreeNode(2), TreeNode(3, TreeNode(4), TreeNode(5)))
serialized = codec.serialize(tree)
print(serialized) 
deserialized = codec.deserialize(serialized)

> "1,2,None,None,3,4,None,None,5,None,None"

```
---


<br>
<br>

[![Open Source](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://opensource.org/)
[![Maintened by - Tanu Nanda Prabhu](https://img.shields.io/badge/Maintained%20by-Tanu%20Nanda%20Prabhu-red)](https://tanu-n-prabhu.github.io/myWebsite.io/)
[![made-with-Markdown](https://img.shields.io/badge/Made%20with-Markdown-1f425f.svg)](http://commonmark.org)




