# Python Cheatsheet
## Phase 1: Foundations

> **Written by**: *Tanu Nanda Prabhu*

This repository is designed as a progressive Python cheatsheet, released in phases. Each phase builds on the previous one and can be used independently for quick revision or teaching.

# Phase 1: Python Foundations

This phase covers the **core building blocks** of Python programming.

### Topics Covered
- Python syntax basics
- Variables and data types
- Operators
- Input and output
- Conditional statements
- Loops
- Functions
- Common built-in functions

# Python Basics

## What is Python?
Python is a high-level, interpreted, dynamically typed programming language.

## Python File
```python
print("Hello, World!")
```

# Indentation

Python uses indentation instead of braces.

```python
if True:
    print("Indented block")
```

# Variables and Data Types

## Variables
```python
x = 10
name = "Python"
pi = 3.14
```

# Multiple Assignment

```
a, b, c = 1, 2, 3
```

# Data Types

```python
int      # 10
float    # 3.14
str      # "Hello"
bool     # True / False
NoneType # None
```

# Type Checking

```python
type(x)
```


# Operators

## Arithmetic
```python
+  -  *  /  //  %  **
```

## Comparison

```python
==  !=  >  <  >=  <=
```

## Logical

```python
and  or  not
```

## Assignment

```python
=  +=  -=  *=  /=
```

# Input and Output

## Input
```python
name = input("Enter your name: ")
```
## Output

```python
print("Hello", name)
```

## Formatted Output

```python
age = 25
print(f"Age: {age}")
```

# Control Flow (Conditionals)

## if Statement
```python
if x > 0:
    print("Positive")
```
## if-else

```python
if x % 2 == 0:
    print("Even")
else:
    print("Odd")
```

## if-elif-else

```python
if x > 0:
    print("Positive")
elif x < 0:
    print("Negative")
else:
    print("Zero")
```


## for Loop
```python
for i in range(5):
    print(i)
```

## while Loop

```python
count = 0
while count < 3:
    print(count)
    count += 1
```

## break and continue

```python
for i in range(5):
    if i == 3:
        break
```

# Functions

## Defining a Function
```python
def greet(name):
    return f"Hello {name}"
```

## Function Call

```python
greet("Python")
```

## Default Parameters

```python
def power(base, exp=2):
    return base ** exp
```

# Common Built-in Functions

```python
len()
type()
range()
max()
min()
sum()
abs()
round()
```

## Example

```python
numbers = [1, 2, 3]
print(sum(numbers))
```

## End of Phase 1

Next Phase: **Phase 2: Data Structures (list, tuple, set, dict)**

This cheatsheet is designed to be **clean, minimal, and copy-paste friendly**.
