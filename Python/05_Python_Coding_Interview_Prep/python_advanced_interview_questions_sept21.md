# Advanced Python Interview Questions and Answers
_September 21, 2025_

This document contains **25 advanced-level Python interview questions with detailed answers**.  
You can use it to prepare for technical interviews or as reference material.

<p align = "right"><i>Written By Tanu Nanda Prabhu</i></p>

---

## 1. What are Python descriptors, and how do they work?

**Answer:**  
Descriptors are objects that define how attribute access is interpreted by overriding methods like `__get__`, `__set__`, and `__delete__`.  
They are commonly used in property, staticmethod, and classmethod implementations.

```python
class Descriptor:
    def __get__(self, instance, owner):
        return "Value retrieved"

    def __set__(self, instance, value):
        print(f"Setting {value}")

class MyClass:
    attr = Descriptor()

obj = MyClass()
print(obj.attr)   # Value retrieved
obj.attr = 10     # Setting 10
```

---

## 2. Explain the Python Global Interpreter Lock (GIL). Why is it needed?

**Answer:**  
The GIL ensures that only one thread executes Python bytecode at a time.  
It is needed because CPython’s memory management is not thread-safe.  
This means CPU-bound tasks don't gain much from threading, but I/O-bound tasks do.

---

## 3. How can you achieve true parallelism in Python?

**Answer:**  
Use **multiprocessing** instead of threading.  
The `multiprocessing` module creates separate processes, each with its own Python interpreter and memory space.

```python
from multiprocessing import Process

def task():
    print("Running in parallel")

p1 = Process(target=task)
p2 = Process(target=task)
p1.start()
p2.start()
```

---

## 4. What is the difference between deep copy and shallow copy?

**Answer:**  
- **Shallow copy:** Copies references to objects (not the objects themselves).  
- **Deep copy:** Recursively copies all objects.  

```python
import copy

a = [[1, 2], [3, 4]]
shallow = copy.copy(a)
deep = copy.deepcopy(a)

a[0][0] = 99
print(shallow)  # [[99, 2], [3, 4]]
print(deep)     # [[1, 2], [3, 4]]
```

---

## 5. What are Python metaclasses?

**Answer:**  
Metaclasses are classes of classes.  
They define how classes behave.  
By default, `type` is the metaclass.  

```python
class Meta(type):
    def __new__(cls, name, bases, dct):
        dct['id'] = 100
        return super().__new__(cls, name, bases, dct)

class MyClass(metaclass=Meta):
    pass

print(MyClass.id)  # 100
```

---

## 6. Explain `__slots__` in Python.

**Answer:**  
`__slots__` is used to restrict dynamic attribute creation and save memory by replacing the default `__dict__`.

```python
class Point:
    __slots__ = ['x', 'y']
    def __init__(self, x, y):
        self.x = x
        self.y = y

p = Point(1, 2)
# p.z = 3  # AttributeError
```

---

## 7. What is monkey patching in Python?

**Answer:**  
Monkey patching is dynamically modifying a class or module at runtime.

```python
class A:
    def greet(self):
        return "Hello"

def new_greet(self):
    return "Hi, patched!"

A.greet = new_greet
print(A().greet())  # Hi, patched!
```

---

## 8. How does Python’s garbage collection work?

**Answer:**  
Python uses **reference counting** and a **cyclic garbage collector** to free unused objects.  
Objects are destroyed when their reference count drops to zero.

---

## 9. What are Python coroutines?

**Answer:**  
Coroutines are generalizations of generators used for asynchronous programming.  
They allow suspending and resuming execution.

```python
async def fetch_data():
    return "data"

import asyncio
print(asyncio.run(fetch_data()))
```

---

## 10. What is the difference between `is` and `==`?

**Answer:**  
- `is`: checks **identity** (same object in memory).  
- `==`: checks **equality** (same value).  

```python
a = [1, 2]
b = [1, 2]
print(a == b)  # True
print(a is b)  # False
```

---

## 11. Explain method resolution order (MRO) in Python.

**Answer:**  
MRO determines the order in which classes are searched when calling a method.  
It uses the **C3 linearization algorithm**.

```python
class A: pass
class B(A): pass
class C(B): pass

print(C.mro())  # [C, B, A, object]
```

---

## 12. How does Python handle memory management?

**Answer:**  
- Objects are allocated on the heap.  
- Reference counting + garbage collection manages memory.  
- Developers can use `gc` module for fine control.

---

## 13. What are Python weak references?

**Answer:**  
Weak references allow referencing objects without increasing their reference count.  
Useful for caching.

```python
import weakref

class MyClass:
    pass

obj = MyClass()
r = weakref.ref(obj)
print(r())  # <__main__.MyClass object>
del obj
print(r())  # None
```

---

## 14. What is the difference between `@classmethod`, `@staticmethod`, and instance methods?

**Answer:**  
- **Instance method:** Takes `self` (default).  
- **Class method:** Takes `cls`, operates on the class.  
- **Static method:** Takes no default args.

```python
class MyClass:
    def instance_method(self):
        return "instance"

    @classmethod
    def class_method(cls):
        return "class"

    @staticmethod
    def static_method():
        return "static"
```

---

## 15. How do you implement caching in Python?

**Answer:**  
Use `functools.lru_cache`.

```python
from functools import lru_cache

@lru_cache(maxsize=100)
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)
```

---

## 16. What is a Python context manager?

**Answer:**  
Context managers handle setup and cleanup automatically with `with`.

```python
with open("file.txt", "w") as f:
    f.write("Hello")
```

Custom context manager:

```python
class MyManager:
    def __enter__(self):
        print("Start")
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("End")

with MyManager():
    pass
```

---

## 17. Explain duck typing in Python.

**Answer:**  
Duck typing means an object’s suitability is determined by presence of methods/attributes, not its type.

```python
class Duck:
    def quack(self): return "Quack"

class Person:
    def quack(self): return "I'm quacking!"

def make_it_quack(obj):
    print(obj.quack())

make_it_quack(Duck())
make_it_quack(Person())
```

---

## 18. What is the difference between `deepcopy` and `pickle`?

**Answer:**  
- `deepcopy`: Creates in-memory independent copies.  
- `pickle`: Serializes objects to a byte stream for persistence/transfer.

---

## 19. How are Python strings immutable but still allow operations like concatenation?

**Answer:**  
Strings are immutable. Concatenation creates new string objects instead of modifying the original.

---

## 20. What is the difference between `__new__` and `__init__`?

**Answer:**  
- `__new__`: Creates a new instance (called before `__init__`).  
- `__init__`: Initializes an existing instance.

---

## 21. What are Python memoryviews?

**Answer:**  
`memoryview` allows working with slices of binary data without copying.

```python
data = bytearray(b"hello")
mv = memoryview(data)
mv[0] = ord('H')
print(data)  # bytearray(b'Hello')
```

---

## 22. Explain async vs threading.

**Answer:**  
- **Async:** Single-threaded, non-blocking, cooperative multitasking.  
- **Threading:** Multi-threaded, preemptive multitasking.  

---

## 23. How do Python decorators work internally?

**Answer:**  
Decorators wrap functions by taking a function as input and returning a new function.

```python
def decorator(func):
    def wrapper(*args, **kwargs):
        print("Before")
        return func(*args, **kwargs)
    return wrapper

@decorator
def greet():
    print("Hello")

greet()
```

---

## 24. What is the difference between `__call__` and `__init__`?

**Answer:**  
- `__init__`: Initializes an object.  
- `__call__`: Makes an object callable like a function.

```python
class MyClass:
    def __call__(self, x):
        return x * 2

obj = MyClass()
print(obj(5))  # 10
```

---

## 25. How do you handle memory leaks in Python?

**Answer:**  
- Use `gc` module to debug.  
- Avoid circular references.  
- Use weak references.  
- Profile with `objgraph` or `tracemalloc`.

---
