# Python Cheatsheet 
## Phase 2: Data Structures

This phase focuses on Python’s core built-in data structures, their syntax, common operations, and practical usage patterns. This file is designed to work as a single-file cheatsheet for quick reference, interviews, and teaching.

## Covered Data Structures
- List
- Tuple
- Set
- Dictionary
- When to use which data structure

# Lists

## What is a List?

A list is an ordered, mutable collection that allows duplicate values.

```python
numbers = [1, 2, 3, 4]
names = ["Alice", "Bob", "Charlie"]
```
## Common Operations

```python
len(numbers)          # Length
numbers.append(5)     # Add element
numbers.insert(1, 10) # Insert at index
numbers.remove(3)     # Remove value
numbers.pop()         # Remove last element
numbers.sort()        # Sort list
numbers.reverse()     # Reverse list
```

## Accessing Elements

```python
numbers[0]      # First element
numbers[-1]     # Last element
numbers[1:3]    # Slicing
```

## List Comprehension

```python
squares = [x**2 for x in range(5)]
```

# Tuples
## What is a Tuple?

A tuple is an ordered, immutable collection.

```python
point = (10, 20)
colors = ("red", "green", "blue")
```

## Characteristics

- Faster than lists
- Cannot be modified after creation
- Can be used as dictionary keys

## Tuple Unpacking

```python
x, y = point
```
## Single-Element Tuple

```python
single = (5,)
```

# Sets
## What is a Set?

A set is an **unordered**, **mutable** collection of **unique elements**.

```python
numbers = {1, 2, 3, 4}
```

## Creating a Set

```python
empty_set = set()
```

## Common Operations

```python
numbers.add(5)
numbers.remove(2)
numbers.discard(10)  # No error if missing
```

## Set Operations

```python
a = {1, 2, 3}
b = {3, 4, 5}

# Union
a | b

# Intersection
a & b

# Difference
a - b
```

## Dictionaries
## What is a Dictionary?

A dictionary stores data as **key-value pairs**. Keys must be unique.

```python
student = {
    "name": "Alice",
    "age": 20,
    "grade": "A"
}
```

## Accessing Values

```python
student["name"]
student.get("age")
```

## Modifying Dictionary

```python
student["age"] = 21
student["city"] = "Toronto"
```

## Removing Items

```python
student.pop("grade")
del student["city"]
```

## Looping Through Dictionary

```python
for key, value in student.items():
    print(key, value)
```

## Dictionary Comprehension

```python
squares = {x: x**2 for x in range(5)}
```

# Nested Data Structures

```python
users = [
    {"id": 1, "name": "Alice"},
    {"id": 2, "name": "Bob"}
]
```

Accessing nested values:

```python
users[0]["name"]
```

# When to Use What?

| **Data Structure** | **Use Case** |
| :-----------: | :---------- |
| List | Ordered collection with frequent updates. |
| Tuple | Fixed data that should not change. |
| Set | Unique items and fast membership testing. |
| Dictionary | Fast lookups using keys. |

# Time Complexity (Quick Reference)

| Operation | List | Set | Dictionary |
| :----------:  | :----------: | :----------: | :----------: |
| Access | O(1) | N/A | O(1) |
| Insert | O(n) | O(1) | O(1) |
| Delete | O(n) | O(1) | O(1) |
|Search | O(n) | O(1) | O(1) |

# End of Phase 2

Next Phase: Phase 3: Object-Oriented Programming (Classes & Objects)

This phase builds the foundation for writing clean, structured, and scalable Python programs.