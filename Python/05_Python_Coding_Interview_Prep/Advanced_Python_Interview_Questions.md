
# Advanced Python Interview Questions and Answers

This document contains 25 advanced Python interview questions with detailed answers, example code, and best practices. It is designed for software engineers preparing for technical interviews.

---

## 1. What are Python decorators and how do they work?

**Answer:**  
Decorators are functions that modify the behavior of other functions or classes. They are commonly used for logging, access control, caching, etc.

**Example:**
```python
def decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Before calling {func.__name__}")
        result = func(*args, **kwargs)
        print(f"After calling {func.__name__}")
        return result
    return wrapper

@decorator
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")
```

**Notes:**  
- Decorators are syntactic sugar for `greet = decorator(greet)`.  
- Can be stacked and used with arguments by adding another layer of functions.

---

## 2. Explain Python generators and the `yield` keyword.

**Answer:**  
Generators are iterators that lazily produce values one at a time, using `yield` instead of `return`. They are memory-efficient for large datasets.

**Example:**
```python
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

for num in fibonacci(5):
    print(num)
```

**Notes:**  
- `yield` pauses function state, allowing resumption.  
- Useful for streaming large data instead of loading everything into memory.

---

## 3. How does Python manage memory?

**Answer:**  
Python uses **reference counting** and a **garbage collector** to manage memory. Cyclic references are cleaned up by the garbage collector.

**Example:**
```python
import gc

a = [1, 2, 3]
b = a  # reference count increases
del a  # reference count decreases
gc.collect()  # manually triggers garbage collection
```

**Notes:**  
- `sys.getrefcount(obj)` can check reference count.  
- Avoid circular references for performance reasons.

---

## 4. What are Python’s `*args` and `**kwargs`?

**Answer:**  
- `*args` collects positional arguments as a tuple.  
- `**kwargs` collects keyword arguments as a dict.

**Example:**
```python
def func(*args, **kwargs):
    print("Positional:", args)
    print("Keyword:", kwargs)

func(1, 2, x=10, y=20)
```

**Notes:**  
- Useful for writing flexible functions.  
- Can be combined with normal arguments: `def f(a, *args, **kwargs): ...`

---

## 5. Explain Python’s `with` statement and context managers.

**Answer:**  
The `with` statement simplifies resource management (like files or network connections) using context managers (`__enter__` and `__exit__` methods).

**Example:**
```python
with open("file.txt", "w") as f:
    f.write("Hello, World!")
```

**Custom context manager:**
```python
class Managed:
    def __enter__(self):
        print("Entering")
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Exiting")

with Managed() as m:
    print("Inside block")
```

---

## 6. Difference between Python lists and tuples.

**Answer:**  
| Feature         | List       | Tuple       |
|-----------------|-----------|------------|
| Mutability      | Mutable   | Immutable  |
| Syntax          | `[1,2,3]`| `(1,2,3)` |
| Performance     | Slower    | Faster    |

**Notes:**  
- Tuples can be used as dictionary keys.  
- Lists are preferred for dynamic collections.

---

## 7. Explain Python’s GIL (Global Interpreter Lock).

**Answer:**  
The GIL ensures that only one thread executes Python bytecode at a time, preventing race conditions.  

**Impact:**  
- CPU-bound tasks may not benefit from multithreading.  
- I/O-bound tasks benefit via `threading`.  
- For CPU-bound tasks, use `multiprocessing` instead.

---

## 8. How does Python handle multithreading and multiprocessing?

**Answer:**  
- **Threading:** Shares memory, limited by GIL. Good for I/O.  
- **Multiprocessing:** Uses separate processes, bypasses GIL. Good for CPU-intensive tasks.

**Example:**
```python
from threading import Thread
def task(n):
    print(n)

threads = [Thread(target=task, args=(i,)) for i in range(5)]
for t in threads: t.start()
for t in threads: t.join()
```

---

## 9. What are Python’s iterators?

**Answer:**  
Iterators are objects implementing `__iter__()` and `__next__()`. They allow lazy iteration over data.

**Example:**
```python
my_list = [1,2,3]
it = iter(my_list)
print(next(it))  # 1
print(next(it))  # 2
```

---

## 10. Explain Python’s `__slots__`.

**Answer:**  
`__slots__` restricts dynamic attribute creation, reducing memory usage.

**Example:**
```python
class Point:
    __slots__ = ['x', 'y']
    def __init__(self, x, y):
        self.x = x
        self.y = y
```

**Notes:**  
- Cannot add attributes not in `__slots__`.  
- Useful for large-scale objects.

---

## 11. What are Python metaclasses?

**Answer:**  
Metaclasses are “classes of classes” that control class creation.

**Example:**
```python
class Meta(type):
    def __new__(cls, name, bases, dct):
        print(f"Creating class {name}")
        return super().__new__(cls, name, bases, dct)

class MyClass(metaclass=Meta):
    pass
```

**Notes:**  
- Rarely needed; mainly for frameworks and advanced class behavior.

---

## 12. Difference between `deepcopy` and `shallow copy`.

**Answer:**  
- **Shallow copy:** Copies outer object, inner objects are references.  
- **Deep copy:** Recursively copies all objects.

**Example:**
```python
import copy
a = [[1,2],[3,4]]
b = copy.copy(a)    # shallow
c = copy.deepcopy(a) # deep
```

---

## 13. How does Python handle exceptions?

**Answer:**  
Python uses `try/except/finally` blocks to handle exceptions.

**Example:**
```python
try:
    1/0
except ZeroDivisionError as e:
    print("Error:", e)
finally:
    print("Cleanup code")
```

**Notes:**  
- Multiple exceptions can be caught.  
- Avoid bare `except` blocks in production code.

---

## 14. What are Python’s `staticmethod` and `classmethod`?

**Answer:**  
- **staticmethod:** Does not take `self` or `cls`.  
- **classmethod:** Takes `cls` and affects the class, not instance.

**Example:**
```python
class MyClass:
    @staticmethod
    def static_method(): print("Static")
    @classmethod
    def class_method(cls): print(f"Class: {cls}")

MyClass.static_method()
MyClass.class_method()
```

---

## 15. How to optimize Python performance?

**Answer:**  
- Use built-in functions and libraries (`map`, `filter`, `itertools`).  
- Use list comprehensions instead of loops.  
- Avoid global variables.  
- Profile code using `cProfile` or `timeit`.

---

## 16. Explain Python’s `__new__` vs `__init__`.

**Answer:**  
- `__new__` creates the instance.  
- `__init__` initializes the instance after creation.

**Example:**
```python
class MyClass:
    def __new__(cls):
        print("Creating instance")
        return super().__new__(cls)
    def __init__(self):
        print("Initializing instance")

obj = MyClass()
```

---

## 17. Difference between Python `is` and `==`.

**Answer:**  
- `==` checks value equality.  
- `is` checks object identity.

**Example:**
```python
a = [1,2]; b = [1,2]
print(a == b)  # True
print(a is b)  # False
```

---

## 18. Explain Python’s `__repr__` vs `__str__`.

**Answer:**  
- `__str__` → user-friendly output.  
- `__repr__` → developer-friendly, unambiguous, ideally can recreate object.

**Example:**
```python
class Point:
    def __repr__(self): return f"Point({self.x},{self.y})"
    def __str__(self): return f"({self.x},{self.y})"
```

---

## 19. How does Python handle method resolution order (MRO)?

**Answer:**  
Python uses **C3 linearization** for multiple inheritance to determine method lookup order.  

**Example:**
```python
class A: pass
class B(A): pass
class C(A): pass
class D(B,C): pass

print(D.__mro__)
```

---

## 20. Difference between Python `@property` and getter/setter methods.

**Answer:**  
`@property` allows controlled attribute access without explicit getter/setter methods.

**Example:**
```python
class Circle:
    def __init__(self, radius): self._radius = radius
    @property
    def radius(self): return self._radius
    @radius.setter
    def radius(self, value): self._radius = value
```

---

## 21. What is Python’s `abc` module?

**Answer:**  
`abc` defines **Abstract Base Classes** for creating interfaces.

**Example:**
```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self): pass
```

---

## 22. Explain Python’s `functools.lru_cache`.

**Answer:**  
Caches function results to improve performance for repeated calls.

**Example:**
```python
from functools import lru_cache

@lru_cache(maxsize=32)
def fib(n):
    if n < 2: return n
    return fib(n-1) + fib(n-2)
```

---

## 23. Difference between `deepcopy` and `copy.copy`.

**Answer:**  
Covered in Q12 — `deepcopy` copies nested objects recursively, `copy` copies only the top-level object.

---

## 24. How does Python implement duck typing?

**Answer:**  
Python relies on object behavior rather than explicit type checks.

**Example:**
```python
def process(obj):
    try:
        obj.write("Hello")
    except AttributeError:
        print("Object cannot write")

class FileLike:
    def write(self, msg): print(msg)
```

---

## 25. How to profile Python code?

**Answer:**  
Use modules like `cProfile`, `timeit`, `line_profiler`.

**Example:**
```python
import cProfile

def compute():
    sum(range(1000000))

cProfile.run("compute()")
```

---

**Bonus Tips:**  
- Practice writing Pythonic code.  
- Understand time/space complexity for built-in data structures.  
- Know standard libraries and modules.  
- Be ready to explain trade-offs and design choices.
