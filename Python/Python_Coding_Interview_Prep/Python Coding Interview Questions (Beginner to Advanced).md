# Python & Machine Learning Interview Questions with Answers - 2025
## Master Essential Python Concepts and Machine Learning Techniques to Ace Your Next Technical Interview
<!-- Feature Image -->
| ![Interview Photo](https://github.com/Tanu-N-Prabhu/Python/blob/f00cc0bfb9fbbf7482559d0ea19ae4b1d284e5af/Img/sebastian-herrmann-O2o1hzDA7iE-unsplash.jpg) | 
|:--:| 
| Photo by <a href="https://unsplash.com/@officestock?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash">Sebastian Herrmann</a> on <a href="https://unsplash.com/photos/four-men-looking-to-the-paper-on-table-O2o1hzDA7iE?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash">Unsplash</a>|

![Views Counter](https://views-counter.vercel.app/badge?pageId=Tanu-N-Prabhu%2FViews-Counter)

<!-- Content-->

# Stay Connected

- Follow me on [LinkedIn](https://ca.linkedin.com/in/tanu-nanda-prabhu-a15a091b5) for daily Python and Machine Learning interview questions & insights!   
- Read my articles on [Medium](https://medium.com/@tanunprabhu95) for in-depth explanations & tutorials!   
- Got a different solution? Drop your thoughts in the discussions! Let’s learn together!


# Table of Contents

➡ [Introduction](https://github.com/Tanu-N-Prabhu/Python/blob/master/Python%20Coding%20Interview%20Prep/Python%20Coding%20Interview%20Questions%20(Beginner%20to%20Advanced).md#introduction)


➡ [Beginner Level](https://github.com/Tanu-N-Prabhu/Python/blob/master/Python%20Coding%20Interview%20Prep/Python%20Coding%20Interview%20Questions%20(Beginner%20to%20Advanced).md#beginner-level)

➡ [Advanced Level](https://github.com/Tanu-N-Prabhu/Python/blob/master/Python%20Coding%20Interview%20Prep/Python%20Coding%20Interview%20Questions%20(Beginner%20to%20Advanced).md#advanced-level)

➡ [Most Frequently Asked Questions by Big Tech Companies](https://github.com/Tanu-N-Prabhu/Python/blob/master/Python%20Coding%20Interview%20Prep/Python%20Coding%20Interview%20Questions%20(Beginner%20to%20Advanced).md#most-frequently-asked-python-questions-by-big-tech-companies)

➡ [Python Projects That Can Land You Your Dream Job](https://github.com/Tanu-N-Prabhu/Python/blob/master/Python%20Coding%20Interview%20Prep/Python%20Coding%20Interview%20Questions%20(Beginner%20to%20Advanced).md#python-projects-that-can-land-you-your-dream-job)

➡ [Machine Learning Interview Prep Questions](https://github.com/Tanu-N-Prabhu/Python/tree/master/Machine%20Learning%20Interview%20Prep%20Questions)

➡ [Credits](https://github.com/Tanu-N-Prabhu/Python/blob/master/Python%20Coding%20Interview%20Prep/Python%20Coding%20Interview%20Questions%20(Beginner%20to%20Advanced).md#credits)




# Introduction

Python is a versatile and widely used programming language, celebrated for its simplicity and readability. As one of the top choices in the tech industry, Python frequently appears in technical interviews across various roles, including software development, data science, and automation.

In this guide, we’ll dive into a wide array of Python interview questions and answers, covering essential topics such as:

* Data Structures: Master lists, dictionaries, sets, and more.
* Algorithms: Understand sorting, searching, and optimization techniques.
* Problem-solving: Sharpen your skills with real-world coding challenges.

These questions are designed to test your grasp of Python's core features, including:

* String Manipulation
* List Operations
* Recursion
* And much more!

Whether you're a beginner just starting your coding journey or an experienced developer brushing up on your skills, this guide will help you prepare effectively for your next Python interview.

Get ready to boost your confidence and showcase your Python prowess!



---


# Beginner Level

In this section, we cover the basics of Python, which is ideal for those just starting their programming journey. You'll explore:

* Basic Syntax: Understand Python's simple and intuitive syntax.
* Data Types: Understand integers, strings, lists, and more.
* Basic Operations: Learn arithmetic operations, string manipulations, and list handling.
* Control Structures: Master loops, conditionals, and basic flow control.
* Simple Functions: Start writing your functions to organize and reuse code.
  
This level builds a strong foundation, ensuring you're well-prepared to move on to more advanced topics.

## 1. What is Python?

Python is an interpreted, high-level, general-purpose programming language. It emphasizes code readability with its use of significant indentation. Python supports multiple programming paradigms, including structured (particularly procedural), object-oriented, and functional programming.

---

## 2. How is Python interpreted?


Python code is executed line by line at runtime. Python internally converts the source code into an intermediate form called bytecode, which is then executed by the Python virtual machine (PVM).

---

## 3. What are Python's key features?

* Easy to learn and use
* Interpreted language
* Dynamically typed
* Extensive libraries
* Object-oriented
* Portable

---

## 4. What is PEP 8?

PEP 8 is the Python Enhancement Proposal that provides guidelines and best practices for writing Python code. It covers various aspects such as naming conventions, code layout, and indentation.

---

## 5. How do you manage memory in Python?

Python uses automatic memory management and a garbage collector to handle memory. The garbage collector recycles memory when objects are no longer in use.

---

## 6. What are Python's data types?

* Numeric types: `int`, `float`, `complex`
* Sequence types: `list`, `tuple`, `range`
* Text type: `str`
* Set types: `set`, `frozenset`
* Mapping type: `dict`
* Boolean type: `bool`
* Binary types: `bytes`, `bytearray`, `memoryview`

---

## 7. What is the difference between a list and a tuple?

* List: Mutable, can be changed after creation.
* Tuple: Immutable, cannot be changed after creation.

---

## 8. How do you handle exceptions in Python?

Using the `try-except` block:

```python
try:
    # code that may raise an exception
except SomeException as e:
    # code to handle the exception

```

---

## 9. Converting an Integer into Decimals

```python
import decimal
integer = 10
print(decimal.Decimal(integer))
print(type(decimal.Decimal(integer)))

> 10
> <class 'decimal.Decimal'>

```
---

## 10. Converting a String of Integers into Decimals

```python
import decimal
string = '12345'
print(decimal.Decimal(string))
print(type(decimal.Decimal(string)))

> 12345
> <class 'decimal.Decimal'>

```

---

## 11. Reversing a String using an Extended Slicing Technique

```python
string = "Python Programming"
print(string[::-1])

> gnimmargorP nohtyP

```

---


## 12. Counting Vowels in a Given Word

```python
vowel = ['a', 'e', 'i', 'o', 'u']
word = "programming"
count = 0
for character in word:
    if character in vowel:
        count += 1
print(count)

> 3
```


---

## 13. Counting Consonants in a Given Word

```python
vowel = ['a', 'e', 'i', 'o', 'u']
word = "programming"
count = 0
for character in word:
    if character not in vowel:
        count += 1
print(count)

> 8
```

---


## 14. Counting the Number of Occurrences of a Character in a String

```python
word = "python"
character = "p"
count = 0
for letter in word:
    if letter == character:
        count += 1
print(count)

> 1
```

---

## 15. Writing Fibonacci Series

```python
fib = [0,1]
# Range starts from 0 by default
for i in range(5):  
    fib.append(fib[-1] + fib[-2]) 

# Converting the list of integers to string
print(', '.join(str(e) for e in fib))

> 0, 1, 1, 2, 3, 5, 8

```

---

## 16. Finding the Maximum Number in a List

```python
numberList = [15, 85, 35, 89, 125]

maxNum = numberList[0]
for num in numberList:
    if maxNum < num:
        maxNum = num
print(maxNum)

> 125

```

---

## 17. Finding the Minimum Number in a List

```python
numberList = [15, 85, 35, 89, 125, 2]

minNum = numberList[0]
for num in numberList:
    if minNum > num:
        minNum = num
print(minNum)

> 2

```

---


## 18. Finding the Middle Element in a List

```python
numList = [1, 2, 3, 4, 5]
midElement = int((len(numList)/2)) 

print(numList[midElement])

> 3
```

---


## 19. Converting a List into a String

```python
lst = ["P", "Y", "T", "H", "O", "N"]
string = ''.join(lst)

print(string)
print(type(string))

> PYTHON
> <class 'str'>
```

---


## 20. Adding Two List Elements Together

```python
lst1 = [1, 2, 3]
lst2 = [4, 5, 6] 

res_lst = [] 
for i in range(0, len(lst1)):
    res_lst.append(lst1[i] + lst2[i]) 
print(res_lst)

> [5, 7, 9]

Another approach 
a = [1, 2, 3]
b = [4, 5, 6]

c = [x + y for x, y in zip(a, b)]
print(c)

> [5, 7, 9]
```

---

## 21. Comparing Two Strings for Anagrams

```python
str1 = "Listen"
str2 = "Silent"

str1 = list(str1.upper())
str2 = list(str2.upper())
str1.sort(), str2.sort()

if(str1 == str2):
    print("True")
else:
    print("False")

> True

```

## 22. Checking for Palindrome Using Extended Slicing Technique

```python
str1 = "Kayak".lower()
str2 = "kayak".lower()

if(str1 == str2[::-1]):
    print("True")
else:
    print("False")
    
> True

```

---

## 23. Counting the White Spaces in a String

```python
string = "P r ogramm in g "
print(string.count(' '))
    
> 5
```

---

## 24. Counting Digits, Letters, and Spaces in a String

```python
# Importing Regular Expressions Library
import re

name = 'Python is 1'

digitCount = re.sub("[^0-9]", "", name)
letterCount = re.sub("[^a-zA-Z]", "", name)
spaceCount = re.findall("[ \n]", name)

print(len(digitCount))
print(len(letterCount))
print(len(spaceCount))
    
> 1
> 8
> 2
```

---

## 25. Counting Special Characters in a String

```python
# Importing Regular Expressions Library
import re
spChar = "!@#$%^&*()"

count = re.sub('[\w]+', '', spChar)
print(len(count))
    
> 10
```

---


## 26. Removing All Whitespace in a String

```python
import re

string = "C O D E"
spaces = re.compile(r'\s+')
result = re.sub(spaces, '', string)
print(result)

> CODE

```

---


## 27. Building a Pyramid in Python

```python
floors = 3
h = 2*floors-1
for i in range(1, 2*floors, 2):
    print('{:^{}}'.format('*'*i, h))

>  *  
  *** 
 *****

```

---

## 28. Randomizing the Items of a List in Python

```python

from random import shuffle

lst = ['Python', 'is', 'Easy']
shuffle(lst)
print(lst)

> ['Easy', 'is', 'Python']


```

---

## 29. Find the Largest Element in a List

```python
def find_largest_element(lst):
    return max(lst)

# Example usage:
print(find_largest_element([1, 2, 3, 4, 5]))

> 5
```

---

## 30. Remove Duplicates from a List

```python
def remove_duplicates(lst):
    return list(set(lst))

# Example usage:
print(remove_duplicates([1, 2, 2, 3, 4, 4, 5]))

> [1, 2, 3, 4, 5]

```
---

## 31. Factorial of a Number

```python
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

# Example usage:
print(factorial(5))

> 120

```

---

## 32. Merge Two Sorted Lists

```python
def merge_sorted_lists(lst1, lst2):
    return sorted(lst1 + lst2)

# Example usage:
print(merge_sorted_lists([1, 3, 5], [2, 4, 6]))

> [1, 2, 3, 4, 5, 6]

```

---

## 33. Find the First Non-Repeating Character

```python
def first_non_repeating_character(s):
    for i in s:
        if s.count(i) == 1:
            return i
    return None

# Example usage:
print(first_non_repeating_character("swiss"))

> w

```
---

#  Advanced Level

In this section, we dive into more complex Python topics, aimed at those looking to deepen their expertise. You’ll tackle:

* Advanced Data Structures: Work with sets, tuples, and more complex data types.
* Recursion and Iteration: Solve problems using advanced looping and recursive techniques.
* Algorithms: Explore sorting, searching, and optimization algorithms in depth.
* Modules and Libraries: Leverage powerful Python libraries for various applications.
* Error Handling and Debugging: Learn to write robust code with effective error handling and debugging techniques.
* Web Scraping and APIs: Gain experience in extracting data from websites and interacting with APIs.
* Advanced Object-Oriented Programming (OOP): Master OOP concepts like inheritance, polymorphism, and design patterns.

This level will challenge you to think critically and apply your knowledge to complex problems, preparing you for high-level Python applications and interviews.

## 34. What are Python metaclasses?

Metaclasses are classes of classes that define how classes behave. A class is an instance of a metaclass. They allow customization of class creation.

---
## 35. Explain the difference between `is` and `==`.


`is`: Checks if two references point to the same object.

`==`: Checks if the values of two objects are equal.

---

## 36. How does Python's memory management work?

Python uses reference counting and garbage collection. Objects with a reference count of zero are automatically cleaned up by the garbage collector.

---

## 37. What is the purpose of Python's `with` statement?

The with statement simplifies exception handling by encapsulating common preparation and cleanup tasks in so-called context managers.

```python
with open('file.txt', 'r') as file:
    data = file.read()
```
---

## 38. What are Python's `@staticmethod` and `@classmethod?`

`@staticmethod`: Defines a method that does not operate on an instance or class; no access to self or cls.

`@classmethod`: Defines a method that operates on the class itself; it receives the class as an implicit first argument (cls).

---

## 39. How do you implement a singleton pattern in Python?

Using a metaclass

```python
class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class MyClass(metaclass=Singleton):
    pass

```

---

## 40. Explain Python's garbage collection mechanism

Python uses a garbage collection mechanism based on reference counting and a cyclic garbage collector to detect and collect cycles (groups of objects that reference each other but are not accessible from any other object).

---

## 41. What are Python's magic methods?

Magic methods (or dunder methods) are special methods with double underscores at the beginning and end. They enable the customization of behavior for standard operations

* `__init__`: Constructor
* `__str__`: String representation
* `__add__`: Addition operator

---

## 42. How do you handle multi-threading in Python?

Using the `threading` module:

```python
import threading

def print_numbers():
    for i in range(10):
        print(i)

thread = threading.Thread(target=print_numbers)
thread.start()
thread.join()

```
---

## 43. What are Python's coroutine functions?

Coroutines are a type of function that can pause and resume their execution. They are defined with `async def` and use `await` to yield control back to the event loop.

```python
import asyncio

async def say_hello():
    await asyncio.sleep(1)
    print("Hello")

asyncio.run(say_hello())
```

---

## 44. Explain Python's Global Interpreter Lock (GIL). How does it affect multithreading?

The Global Interpreter Lock (GIL) is a mutex that protects access to Python objects, preventing multiple native threads from executing Python bytecodes simultaneously in CPython. This lock simplifies memory management and ensures thread safety, but it limits the performance of multi-threaded Python programs by allowing only one thread to execute at a time. As a result, Python multithreading is more suitable for I/O-bound tasks than CPU-bound tasks. Multiprocessing or other Python implementations, like Jython or IronPython, may be preferred for CPU-bound tasks.

---

## 45. What are metaclasses in Python, and how are they used?

A metaclass in Python is a class of a class that defines how a class behaves. Classes themselves are instances of metaclasses. You can customize class creation by defining a metaclass, such as modifying class properties, adding methods, or implementing design patterns. A common use case for metaclasses is enforcing coding standards or design patterns, such as singleton, or auto-registering classes.

---

## 46. Can you explain the difference between `deepcopy` and `copy` in Python?

The `copy` module in Python provides two methods: `copy()` and `deepcopy()`.

* `copy.copy()` creates a shallow copy of an object. It copies the object's structure but not the elements themselves, meaning it only copies references for mutable objects.

* `copy.deepcopy()` creates a deep copy of the object, including recursively copying all objects contained within the original object. Changes made to the deep-copied object do not affect the original object.


---

## 47. Describe Python’s `__slots__` and its benefits.

`__slots__` is a special attribute in Python that allows you to explicitly declare data members (slots) and prevent the creation of `__dict__`, thereby reducing memory overhead. By using `__slots__`, you can limit the attributes of a class to a fixed set of fields and reduce the per-instance memory consumption. This is particularly beneficial when creating a large number of instances of a class.

---

## 48. What is the difference between `is` and `==` in Python?

* `is` checks for identity, meaning it returns `True` if two references point to the same object in memory.

* `==` checks for equality, meaning it returns `True` if the values of the objects are equal, even if they are different objects in memory.

```python

a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(a is b)  # True, because both a and b refer to the same object
print(a is c)  # False, because a and c refer to different objects
print(a == c)  # True, because a and c have the same values

```

## 49. Find the Longest Consecutive Sequence in an Unsorted List

#### Problem: Given an unsorted list of integers, find the length of the longest consecutive sequence.

#### Example:

```
Input: [100, 4, 200, 1, 3, 2]
Output: 4  # (Sequence: [1, 2, 3, 4])
```
#### Solution:

```
def longest_consecutive(nums):
    num_set = set(nums)  # Convert list to set for O(1) lookups
    longest = 0

    for num in num_set:
        if num - 1 not in num_set:  # Start of a new sequence
            length = 1
            while num + length in num_set:
                length += 1
            longest = max(longest, length)

    return longest

# Example usage:
print(longest_consecutive([100, 4, 200, 1, 3, 2]))  # Output: 4
```

> Complexity: `O(N)`, where `N` is the number of elements.

---


# Most Frequently Asked Python Questions by Big Tech Companies

As we gear up for technical interviews, it’s essential to be prepared for the toughest Python questions.
If you're preparing for high-level technical interviews, you'll want to master these complex Python problems.
Here’s a list of coding questions that have been asked by top-tier companies!

---

## 1. Longest Substring Without Repeating Characters

**Problem**  
Given a string, find the length of the longest substring without repeating characters.

```python
def length_of_longest_substring(s: str) -> int:
    char_set = set()
    left = 0
    max_len = 0

    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        char_set.add(s[right])
        max_len = max(max_len, right - left + 1)

    return max_len

# Example usage
print(length_of_longest_substring("abcabcbb"))  # Output: 3
```

**Explanation**  
Sliding window approach with a set to track unique characters.

> **Asked by:** Meta (Phone Interview, 2022) — Source: LeetCode Discuss

---

## 2. Merge Intervals

**Problem**  
Merge overlapping intervals in a list.

```python
from typing import List

def merge(intervals: List[List[int]]) -> List[List[int]]:
    if not intervals:
        return []

    intervals.sort(key=lambda x: x[0])
    merged = [intervals[0]]

    for current in intervals[1:]:
        prev = merged[-1]
        if current[0] <= prev[1]:
            prev[1] = max(prev[1], current[1])
        else:
            merged.append(current)

    return merged

# Example usage
print(merge([[1,3],[2,6],[8,10],[15,18]]))  # Output: [[1,6],[8,10],[15,18]]
```

**Explanation**  
Sort intervals and merge overlapping ones.

> **Asked by:** Google (Onsite Interview, 2021) — Source: GeeksforGeeks

---

## 3. Two Sum

**Problem**  
Return indices of two numbers that add up to a target.

```python
def two_sum(nums, target):
    hashmap = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in hashmap:
            return [hashmap[complement], i]
        hashmap[num] = i
    return []

# Example usage
print(two_sum([2, 7, 11, 15], 9))  # Output: [0, 1]
```

**Explanation**  
Hashmap tracks complements during traversal.

> **Asked by:** Amazon (OA, 2023) — Source: LeetCode Discuss

---

## 4. Group Anagrams

**Problem**  
Group words that are anagrams.

```python
from collections import defaultdict

def group_anagrams(strs):
    anagram_map = defaultdict(list)
    for word in strs:
        sorted_word = ''.join(sorted(word))
        anagram_map[sorted_word].append(word)
    return list(anagram_map.values())

# Example usage
print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
```

**Explanation**  
Sorted word acts as key in a hashmap.

> **Asked by:** Microsoft (Interview, 2022) — Source: LeetCode Premium

---

## 5. Valid Parentheses

**Problem**  
Determine if a string has valid parentheses.

```python
def is_valid(s):
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}
    for char in s:
        if char in mapping.values():
            stack.append(char)
        elif char in mapping:
            if not stack or stack[-1] != mapping[char]:
                return False
            stack.pop()
        else:
            return False
    return not stack

# Example usage
print(is_valid("()[]{}"))  # Output: True
```

**Explanation**  
Stack checks for balanced brackets.

> **Asked by:** Apple (Onsite, 2021) — Source: Glassdoor

---

## 6. Top K Frequent Elements

```python
from collections import Counter
import heapq

def top_k_frequent(nums, k):
    count = Counter(nums)
    return heapq.nlargest(k, count.keys(), key=count.get)

# Example usage
print(top_k_frequent([1,1,1,2,2,3], 2))  # Output: [1, 2]
```

> **Asked by:** Google (2022) — Source: LeetCode Discuss

---

## 7. Product of Array Except Self

```python
def product_except_self(nums):
    res = [1] * len(nums)
    prefix = 1
    for i in range(len(nums)):
        res[i] = prefix
        prefix *= nums[i]

    suffix = 1
    for i in reversed(range(len(nums))):
        res[i] *= suffix
        suffix *= nums[i]

    return res

# Example usage
print(product_except_self([1,2,3,4]))  # Output: [24,12,8,6]
```

> **Asked by:** Amazon (SDE-2, 2023) — Source: LeetCode

---

## 8. Binary Tree Level Order Traversal

```python
from collections import deque

def level_order(root):
    if not root:
        return []
    res = []
    queue = deque([root])
    while queue:
        level = []
        for _ in range(len(queue)):
            node = queue.popleft()
            level.append(node.val)
            if node.left: queue.append(node.left)
            if node.right: queue.append(node.right)
        res.append(level)
    return res
```

> **Asked by:** Facebook (2022) — Source: Glassdoor

---

## 9. Rotate Image (Matrix)

```python
def rotate(matrix):
    matrix.reverse()
    for i in range(len(matrix)):
        for j in range(i):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
```

> **Asked by:** Google (2021) — Source: LeetCode

---

## 10. Search in Rotated Sorted Array

```python
def search(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        if nums[left] <= nums[mid]:
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
    return -1
```

> **Asked by:** Microsoft (2022) — Source: LeetCode


---

# Python Projects That Can Land You Your Dream Job 

> If you use Visual Studio Code, don't forget to read about these mind-blowing [free extensions](https://medium.com/gitconnected/5-must-use-visual-studio-code-extensions-in-2025-00e121400690). 


1. [Comparing Excel to PDF Conversion Methods with Python Hacks](https://medium.com/gitconnected/comparing-excel-to-pdf-conversion-methods-with-python-hacks-1aa7300f4bd5)
2. [Unleashing Dog Breeds with Python for Fun and Laughs](https://medium.com/gitconnected/unleashing-dog-breeds-with-python-for-fun-and-laughs-1f9f81034969)
3. [Ditch the Paper, Embrace Python: Build a Note-Taking App in 2025](https://medium.com/gitconnected/ditch-the-paper-embrace-python-build-a-note-taking-app-in-2025-1b1696ebed54)
4. [Cracking Transit Data — Calgary 2025](https://medium.com/gitconnected/cracking-transit-data-calgary-2025-49baea30833e)
5. [Webscraping vs API](https://medium.com/gitconnected/web-scraping-vs-api-which-data-extraction-method-is-best-for-your-needs-c578464d6083)
6. [Python’s If and Else Statements](https://towardsdev.com/pythons-if-and-else-statements-3b0b0bf3ea00)
7. [Pick-Up Line Generator using Python Dictionaries](https://towardsdev.com/pick-up-line-generator-using-python-dictionaries-f800e5477b02)
8. [Crazy Things You Can Do With the Python Pillow Function](https://levelup.gitconnected.com/crazy-things-you-can-do-with-the-python-pillow-function-3544ea01c567)
9. [The two Google Search Python Libraries you should never miss!](https://medium.com/analytics-vidhya/the-two-google-search-python-libraries-you-should-never-miss-dfb2ec324a33)
10. [Presenting Python code using RISE](https://towardsdatascience.com/presenting-python-code-using-rise-d0dddd48e749)
11. [How to handle JSON in Python?](https://towardsdatascience.com/how-to-handle-json-in-python-d877125df39b)
12. [Using the Pandas DataFrame in Day-To-Day Life](https://towardsdatascience.com/using-the-pandas-dataframe-in-day-to-day-life-91859ee12cca)
13. [Global, Local, and Nonlocal variables in Python](https://towardsdatascience.com/global-local-and-nonlocal-variables-in-python-6b11c20d73b0)
14. [Rendering Images inside a Pandas DataFrame](https://towardsdatascience.com/rendering-images-inside-a-pandas-dataframe-3631a4883f60)
15. [Reading An Image In Python (Without Using Special Libraries)](https://towardsdatascience.com/reading-an-image-in-python-without-using-special-libraries-534b57de7dd4)
16. [Mastering the Bar Plot in Python](https://towardsdatascience.com/mastering-the-bar-plot-in-python-4c987b459053)
17. [Python Operators from Scratch!!! — A Beginner’s Guide](https://towardsdatascience.com/python-operators-from-scratch-a-beginners-guide-8471306f4278)
18. [Splitting the dataset into three sets](https://medium.com/analytics-vidhya/splitting-the-dataset-into-three-sets-78f419f0d608)
19. [Normalization vs Standardization, which one is better](https://towardsdatascience.com/normalization-vs-standardization-which-one-is-better-f29e043a57eb)
20. [Learning One-Hot Encoding in Python the Easy Way](https://towardsdatascience.com/learning-one-hot-encoding-in-python-the-easy-way-665010457ad9)
21. [Wikipedia API for Python](https://towardsdatascience.com/wikipedia-api-for-python-241cfae09f1c)
22. [Google Trends API for Python](https://towardsdatascience.com/google-trends-api-for-python-a84bc25db88f)
23. [Google Translate API for Python](https://towardsdatascience.com/google-translate-api-for-python-723093c2144b)
24. [Speech Recognition using Python](https://medium.com/analytics-vidhya/speech-recognition-using-python-bafe550ee6e9)
25. [Learn the Python Math Module](https://levelup.gitconnected.com/learn-the-python-math-module-9c2c516ea37c)
26. [Learn the Python len() Function](https://levelup.gitconnected.com/learn-the-python-len-function-49b20bb8edd9)
27. [How to create NumPy arrays from scratch?](https://towardsdatascience.com/how-to-create-numpy-arrays-from-scratch-3e0341f9ffea)
28. [Python enumerate() built-in-function](https://towardsdatascience.com/python-enumerate-built-in-function-acccf988d096)
29. [Python Lambda Function](https://towardsdatascience.com/python-lambda-function-b6e1fa3420c1)
30. [Python Input, Output and Import](https://towardsdatascience.com/python-input-output-and-import-73e875516694)
31. [Is Python object-oriented?](https://towardsdatascience.com/is-python-object-oriented-834d6c70cf54)
32. [Using the Pandas Data Frame as a Database.](https://towardsdatascience.com/using-the-pandas-data-frame-as-a-database-282edec5a3ab)
33. [Python range() built-in-function](https://towardsdatascience.com/python-range-built-in-function-b2489ea99660)
34. [Python eval() built-in-function](https://towardsdatascience.com/python-eval-built-in-function-601f87db191)
35. [Top Python Libraries Used In Data Science](https://towardsdatascience.com/top-python-libraries-used-in-data-science-a58e90f1b4ba)
36. [Predicting PewDiePie’s daily subscribers using Linear Regression](https://towardsdatascience.com/predicting-pewdiepies-daily-subscribers-using-linear-regression-15da7bd28f85)
37. [Python Dictionary from Scratch!!!](https://towardsdatascience.com/python-dictionary-from-scratch-c41316794bcc)
38. [How to build a basic machine learning model from scratch](https://medium.com/analytics-vidhya/building-a-machine-learning-model-to-predict-the-price-of-the-car-bc51783ba2f3)
39. [Exploring the data using Python](https://towardsdatascience.com/exploring-the-data-using-python-47c4bc7b8fa2)
40. [Python Tuples from Scratch !!!](https://towardsdatascience.com/python-tuples-from-scratch-43affe1751ba)
41. [Python Strings from scratch !!!](https://towardsdatascience.com/python-strings-from-scratch-afd5ad034de8)
42. [Exploratory data analysis in Python.](https://towardsdatascience.com/exploratory-data-analysis-in-python-c9a77dfa39ce)
43. [Scraping two YouTube accounts using Python libraries.](https://medium.com/@tanunprabhu95/scraping-two-youtube-accounts-using-python-libraries-6af17f2071dd)
44. [Web Scraping Using Python Libraries](https://towardsdatascience.com/web-scraping-using-python-libraries-fe3037152ed1)
45. [Python Pandas Data Frame Basics](https://towardsdatascience.com/python-pandas-data-frame-basics-b5cfbcd8c039)
46. [Python Lists from Scratch](https://towardsdatascience.com/python-lists-from-scratch-4b958eb956fc)
47. [Manipulating the data with Pandas using Python](https://towardsdatascience.com/manipulating-the-data-with-pandas-using-python-be6c5dfabd47)
48. [Data Cleaning using Python with Pandas Library](https://towardsdatascience.com/data-cleaning-with-python-using-pandas-library-c6f4a68ea8eb)
    

# Credits
This repository is created and maintained by [Tanu N Prabhu](https://medium.com/@tanunprabhu95). With a passion for programming and education, I aim to provide valuable resources to help others succeed in their Python journey.

Feel free to explore, contribute, and share your feedback. Happy coding!

> Tip for interview prep: Always understand the logic behind these problems and practice writing clean, efficient code. Challenge yourself with more problems to boost your skills! 



<br>
<br>

[![Open Source](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://opensource.org/)
[![Maintened by - Tanu Nanda Prabhu](https://img.shields.io/badge/Maintained%20by-Tanu%20Nanda%20Prabhu-red)](https://tanu-n-prabhu.github.io/myWebsite.io/)
[![made-with-Markdown](https://img.shields.io/badge/Made%20with-Markdown-1f425f.svg)](http://commonmark.org)

























