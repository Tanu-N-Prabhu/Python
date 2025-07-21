# Python Programming: Data Types, Loops, and Functions

_A Beginner's Guide to Core Python Concepts_

This document covers essential Python programming foundations every data analyst or beginner developer should know. With clear explanations and practical examples, it’s ideal for self-learners, bootcamp students, and anyone brushing up on Python basics.

---

## 1. Data Types in Python

Python has several built-in data types that are commonly used in data analysis.

### Numeric Types

- **int** – Integer numbers (e.g., `5`, `-42`)
- **float** – Decimal numbers (e.g., `3.14`, `-0.001`)
- **complex** – Complex numbers (rarely used in data analysis)

```python
a = 10         # int
b = 3.14       # float
```

### Boolean

- **bool** – Represents `True` or `False`

```python
is_valid = True
```

### Text Type

- **str** – Strings or sequences of characters

```python
name = "Data Analysis"
```

### Sequence Types

- **list** – Ordered, mutable collection
- **tuple** – Ordered, immutable collection
- **range** – Represents a sequence of numbers

```python
numbers = [1, 2, 3]       # list
coordinates = (10, 20)    # tuple
```

### Set Types

- **set** – Unordered collection of unique elements

```python
fruits = {"apple", "banana", "apple"}  # Output: {'apple', 'banana'}
```

### Dictionary

- **dict** – Key-value pairs

```python
person = {"name": "Alice", "age": 25}
```

---

## 2. Loops in Python

Loops allow you to run blocks of code multiple times.

### For Loop

Used to iterate over a sequence (like a list or a string).

```python
for i in range(5):
    print("Iteration:", i)
```

### While Loop

Repeats as long as a condition is `True`.

```python
x = 0
while x < 3:
    print("x is", x)
    x += 1
```

### Loop Control Statements

- `break` – Exit the loop early
- `continue` – Skip the rest of the loop and go to the next iteration

```python
for i in range(5):
    if i == 3:
        break
    print(i)
```

---

## 3. Functions in Python

Functions allow you to reuse blocks of code.

### Defining a Function

```python
def greet(name):
    print("Hello,", name)
```

### Calling a Function

```python
greet("Alice")  # Output: Hello, Alice
```

### Return Statement

```python
def add(a, b):
    return a + b

result = add(5, 3)
print(result)  # Output: 8
```

### Default Arguments

```python
def greet(name="friend"):
    print("Hi,", name)

greet()        # Output: Hi, friend
greet("Bob")   # Output: Hi, Bob
```

### Variable Scope

- Variables inside functions are **local**.
- Variables outside are **global** (unless shadowed).

```python
x = 5  # global

def change():
    x = 10  # local
    print("Inside function:", x)

change()
print("Outside function:", x)
```

---

## Summary

| Concept       | Description                              | Example                     |
|---------------|------------------------------------------|-----------------------------|
| Data Types    | Types of data like int, str, list        | `x = [1, 2, 3]`             |
| For Loop      | Iterates over sequences                  | `for i in range(5)`         |
| While Loop    | Loops while a condition is true          | `while x < 10:`             |
| Function      | Reusable code blocks                     | `def greet(name):`          |
| Return        | Outputs a value from a function          | `return a + b`              |
| Default Args  | Function parameters with default values  | `def greet(name="friend")`  |

---

## What's Next?

Move on to:
- [Basic Statistics README](../basic_statistics_readme.md)
- [Jupyter Notebook Tutorial](../jupyter_notebooks.md)
- [25 Interview Questions on Data Analysis](../25_questions_readme.md)

---

© This content is part of the Data Analysis Learning Series
