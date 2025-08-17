
# Python Interview Questions and Answers

This repository contains **20 of the most frequently asked Python interview questions**, along with clear answers and explanations to help you prepare for technical interviews.

---

## Table of Contents

1. [What is Python?](#1-what-is-python)
2. [What are Python's key features?](#2-what-are-pythons-key-features)
3. [What is PEP 8?](#3-what-is-pep-8)
4. [What is the difference between Python 2 and Python 3?](#4-what-is-the-difference-between-python-2-and-python-3)
5. [What are Python data types?](#5-what-are-python-data-types)
6. [What is the difference between list, tuple, and set?](#6-what-is-the-difference-between-list-tuple-and-set)
7. [What is a Python dictionary?](#7-what-is-a-python-dictionary)
8. [What are Python functions?](#8-what-are-python-functions)
9. [What are Python decorators?](#9-what-are-python-decorators)
10. [What is Python's `*args` and `**kwargs`?](#10-what-is-pythons-args-and-kwargs)
11. [What is the difference between shallow copy and deep copy?](#11-what-is-the-difference-between-shallow-copy-and-deep-copy)
12. [What are Python modules and packages?](#12-what-are-python-modules-and-packages)
13. [What is Python's Global Interpreter Lock (GIL)?](#13-what-is-pythons-global-interpreter-lock-gil)
14. [What is the difference between Python multithreading and multiprocessing?](#14-what-is-the-difference-between-python-multithreading-and-multiprocessing)
15. [What is Python's `with` statement?](#15-what-is-pythons-with-statement)
16. [What are Python iterators and generators?](#16-what-are-python-iterators-and-generators)
17. [What is the difference between `is` and `==`?](#17-what-is-the-difference-between-is-and-)
18. [What is Python's `lambda` function?](#18-what-is-pythons-lambda-function)
19. [What is exception handling in Python?](#19-what-is-exception-handling-in-python)
20. [What are Python's built-in data structures?](#20-what-are-pythons-built-in-data-structures)

---

## 1. What is Python?

**Answer:** Python is a high-level, interpreted programming language known for its readability, simplicity, and versatility. It supports multiple programming paradigms including procedural, object-oriented, and functional programming.

**Explanation:** Python is widely used in web development, data science, AI, automation, and scripting due to its easy syntax and strong community support.

---

## 2. What are Python's key features?

- Easy to learn and use
- Interpreted language
- Dynamically typed
- Open source
- Extensive standard library
- Supports multiple paradigms (OOP, functional, procedural)
- Large community support

**Explanation:** These features make Python suitable for both beginners and professional developers.

---

## 3. What is PEP 8?

**Answer:** PEP 8 is Python's official style guide that provides coding conventions for writing readable and consistent Python code.

**Explanation:** Following PEP 8 ensures your code is clean, maintainable, and adheres to community standards.

---

## 4. What is the difference between Python 2 and Python 3?

| Feature            | Python 2           | Python 3            |
|-------------------|-----------------|------------------|
| Print statement     | `print "Hello"` | `print("Hello")` |
| Integer division    | `5/2 = 2`       | `5/2 = 2.5`      |
| Unicode support     | Limited         | Default          |
| End of life         | 2020            | Supported        |

**Explanation:** Python 3 is the current standard. Python 2 is outdated and not recommended for new projects.

---

## 5. What are Python data types?

- Numeric: `int`, `float`, `complex`
- Sequence: `list`, `tuple`, `range`
- Text: `str`
- Set types: `set`, `frozenset`
- Mapping: `dict`
- Boolean: `bool`
- None type: `NoneType`

**Explanation:** Data types define the kind of value a variable can hold.

---

## 6. What is the difference between list, tuple, and set?

| Feature      | List           | Tuple          | Set                |
|-------------|----------------|---------------|------------------|
| Mutable     | Yes            | No            | Yes               |
| Ordered     | Yes            | Yes           | No                |
| Duplicate   | Allowed        | Allowed       | Not allowed       |

**Explanation:** Use tuples for immutable sequences, sets for unique items, and lists for flexible collections.

---

## 7. What is a Python dictionary?

**Answer:** A dictionary is a collection of key-value pairs enclosed in `{}`. Each key is unique.

**Example:**
```python
person = {"name": "Alice", "age": 25}
print(person["name"])  # Output: Alice
```

**Explanation:** Dictionaries are ideal for fast lookups using unique keys.

---

## 8. What are Python functions?

**Answer:** Functions are reusable blocks of code that perform a specific task.

**Example:**
```python
def greet(name):
    return f"Hello, {name}"
```

**Explanation:** Functions help organize code and avoid repetition.

---

## 9. What are Python decorators?

**Answer:** Decorators are functions that modify the behavior of another function without changing its code.

**Example:**
```python
def decorator(func):
    def wrapper():
        print("Before function")
        func()
    return wrapper

@decorator
def say_hello():
    print("Hello")

say_hello()
```

**Explanation:** Decorators are used for logging, access control, and instrumentation.

---

## 10. What is Python's `*args` and `**kwargs`?

- `*args` allows passing a variable number of positional arguments.
- `**kwargs` allows passing a variable number of keyword arguments.

**Example:**
```python
def func(*args, **kwargs):
    print(args, kwargs)
```

**Explanation:** Useful for flexible function signatures.

---

## 11. What is the difference between shallow copy and deep copy?

- Shallow copy: Copies only the reference to the objects, changes affect the original.
- Deep copy: Creates a new object and recursively copies all objects.

**Example:**
```python
import copy
list1 = [[1, 2], [3, 4]]
shallow = copy.copy(list1)
deep = copy.deepcopy(list1)
```

---

## 12. What are Python modules and packages?

- **Module:** A file containing Python code (`.py`).
- **Package:** A folder containing modules and `__init__.py`.

**Explanation:** They help organize code into reusable and maintainable units.

---

## 13. What is Python's Global Interpreter Lock (GIL)?

**Answer:** GIL is a mutex that allows only one thread to execute Python bytecode at a time.

**Explanation:** It affects multithreaded CPU-bound tasks, but not I/O-bound tasks.

---

## 14. What is the difference between Python multithreading and multiprocessing?

| Feature       | Multithreading       | Multiprocessing       |
|--------------|-------------------|--------------------|
| Parallelism   | Limited (GIL)      | True parallelism    |
| Memory        | Shared memory       | Separate memory     |
| Use case      | I/O-bound tasks     | CPU-bound tasks     |

---

## 15. What is Python's `with` statement?

**Answer:** `with` is used to simplify resource management (e.g., file handling) and ensures proper cleanup.

**Example:**
```python
with open("file.txt") as f:
    data = f.read()
```

---

## 16. What are Python iterators and generators?

- **Iterator:** Object that can be iterated using `__iter__()` and `__next__()`.
- **Generator:** Function that yields values lazily using `yield`.

**Example:**
```python
def gen():
    for i in range(3):
        yield i
```

---

## 17. What is the difference between `is` and `==`?

- `is`: Checks identity (if two objects are the same in memory)
- `==`: Checks value equality

**Example:**
```python
a = [1,2]; b = [1,2]
print(a == b)  # True
print(a is b)  # False
```

---

## 18. What is Python's `lambda` function?

**Answer:** Anonymous inline function using `lambda` keyword.

**Example:**
```python
square = lambda x: x*x
print(square(5))  # 25
```

**Explanation:** Useful for short, throwaway functions.

---

## 19. What is exception handling in Python?

**Answer:** Mechanism to handle runtime errors using `try`, `except`, `finally`.

**Example:**
```python
try:
    x = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")
```

---

## 20. What are Python's built-in data structures?

- Lists
- Tuples
- Sets
- Dictionaries
- Strings

**Explanation:** Built-in data structures are optimized for different use cases, such as sequences, mappings, and sets.

---

**Author:** Tanu Nanda Prabhu  
**Last Updated:** August 17, 2025
