# Python Interview Questions (September 2025)

This document contains 25 frequently asked Python interview questions from major tech companies in **September 2025**.  
Each question includes an **answer, explanation, and code example (where applicable)**.

---

## 1. What are Python’s key features?
**Answer:** Python is interpreted, dynamically typed, object-oriented, and has extensive libraries.  
**Explanation:** These features make Python versatile for scripting, web development, ML, and system tasks.  
**Code Example:**
```python
print("Hello, Python!")  # Interpreted, no compilation needed
```

---

## 2. What is PEP 8 and why is it important?
**Answer:** PEP 8 is the style guide for writing clean, readable Python code.  
**Explanation:** Following PEP 8 improves consistency and readability across projects.  
**Code Example:**
```python
# Good PEP 8 practice
def add_numbers(a, b):
    return a + b
```

---

## 3. Explain Python’s memory management.
**Answer:** Python uses reference counting and garbage collection for memory management.  
**Explanation:** Objects are destroyed when reference count reaches zero. Cyclic references are handled by GC.  
**Code Example:**
```python
import gc
print(gc.isenabled())  # True by default
```

---

## 4. What is the Global Interpreter Lock (GIL)?
**Answer:** The GIL ensures only one thread executes Python bytecode at a time.  
**Explanation:** Good for memory safety, but limits multi-core CPU-bound performance.  
**Code Example:**
```python
import threading

x = 0
def task():
    global x
    for _ in range(1000000):
        x += 1

t1 = threading.Thread(target=task)
t2 = threading.Thread(target=task)
t1.start(); t2.start()
t1.join(); t2.join()
print(x)  # Not 2M due to GIL
```

---

## 5. Difference between deep copy and shallow copy?
**Answer:** Shallow copy copies references; deep copy creates independent copies.  
**Explanation:** Shallow copies share nested objects, deep copies don’t.  
**Code Example:**
```python
import copy
a = [[1,2],[3,4]]
shallow = copy.copy(a)
deep = copy.deepcopy(a)
a[0][0] = 99
print(shallow)  # [[99, 2], [3, 4]]
print(deep)     # [[1, 2], [3, 4]]
```

---

## 6. Explain Python’s `with` statement.
**Answer:** It simplifies resource management using context managers.  
**Explanation:** Ensures resources are released properly.  
**Code Example:**
```python
with open("file.txt", "w") as f:
    f.write("Hello!")
# File auto-closed
```

---

## 7. What are Python decorators?
**Answer:** Functions that modify behavior of other functions.  
**Explanation:** Useful for logging, authentication, caching.  
**Code Example:**
```python
def log(func):
    def wrapper(*args):
        print("Calling", func.__name__)
        return func(*args)
    return wrapper

@log
def greet(name):
    print(f"Hello {name}")

greet("Python")
```

---

## 8. What are Python generators?
**Answer:** Functions using `yield` to return values lazily.  
**Explanation:** Memory efficient, used in large datasets.  
**Code Example:**
```python
def gen():
    for i in range(3):
        yield i

for x in gen():
    print(x)
```

---

## 9. Difference between `is` and `==`?
**Answer:** `is` checks identity, `==` checks equality.  
**Explanation:** Two objects can be equal but not identical.  
**Code Example:**
```python
a = [1,2]
b = [1,2]
print(a == b)  # True
print(a is b)  # False
```

---

## 10. What are Python’s data structures?
**Answer:** Lists, tuples, sets, dicts.  
**Explanation:** Built-ins cover most needs, implemented efficiently.  
**Code Example:**
```python
my_list = [1,2,3]
my_tuple = (1,2,3)
my_set = {1,2,3}
my_dict = {"a":1,"b":2}
```

---

## 11. Explain list comprehension.
**Answer:** A concise way to create lists.  
**Explanation:** More readable and efficient than loops.  
**Code Example:**
```python
squares = [x**2 for x in range(5)]
print(squares)
```

---

## 12. Explain Python’s `@staticmethod` vs `@classmethod`.
**Answer:**  
- `staticmethod`: No access to class or instance.  
- `classmethod`: Accesses class but not instance.  
**Code Example:**
```python
class MyClass:
    @staticmethod
    def sm():
        print("Static")
    @classmethod
    def cm(cls):
        print("Class", cls)

MyClass.sm()
MyClass.cm()
```

---

## 13. What is Python’s MRO?
**Answer:** Method Resolution Order defines order of class inheritance search.  
**Explanation:** Uses C3 linearization.  
**Code Example:**
```python
class A: pass
class B(A): pass
class C(B): pass
print(C.mro())
```

---

## 14. What are Python descriptors?
**Answer:** Objects defining `__get__`, `__set__`, `__delete__`.  
**Explanation:** Used for properties, ORM fields.  
**Code Example:**
```python
class Descriptor:
    def __get__(self, obj, objtype):
        return "value"
class My:
    x = Descriptor()

print(My().x)
```

---

## 15. How does Python handle multithreading vs multiprocessing?
**Answer:**  
- **Multithreading:** Limited by GIL for CPU tasks. Good for I/O.  
- **Multiprocessing:** Spawns processes, bypassing GIL.  
**Code Example:**
```python
from multiprocessing import Process

def work():
    print("Working")

p = Process(target=work)
p.start(); p.join()
```

---

## 16. Explain Python’s garbage collection.
**Answer:** Uses reference counting + cyclic GC.  
**Explanation:** Cyclic GC detects and removes circular references.  
**Code Example:**
```python
import gc
gc.collect()
```

---

## 17. What is monkey patching?
**Answer:** Dynamically modifying a class/module at runtime.  
**Explanation:** Can be useful but risky.  
**Code Example:**
```python
class A:
    def hello(self): print("Hi")

def new_hello(self): print("Hello patched")

A.hello = new_hello
A().hello()
```

---

## 18. Difference between `@property` and normal methods?
**Answer:** `@property` allows method access like attributes.  
**Explanation:** Used for encapsulation.  
**Code Example:**
```python
class Circle:
    def __init__(self, r): self.r = r
    @property
    def area(self): return 3.14 * self.r**2

c = Circle(5)
print(c.area)
```

---

## 19. Explain Python’s `__slots__`.
**Answer:** Restricts attribute creation, saves memory.  
**Explanation:** Used in memory-sensitive apps.  
**Code Example:**
```python
class Point:
    __slots__ = ['x','y']
    def __init__(self,x,y): self.x,self.y=x,y
```

---

## 20. Explain Python’s AsyncIO.
**Answer:** Library for async programming with `async/await`.  
**Explanation:** Efficient for I/O-bound tasks.  
**Code Example:**
```python
import asyncio

async def hello():
    await asyncio.sleep(1)
    print("Hello async")

asyncio.run(hello())
```

---

## 21. How does Python implement immutability?
**Answer:** Immutable types: str, tuple, frozenset.  
**Explanation:** Values cannot be modified in-place.  
**Code Example:**
```python
s = "abc"
# s[0] = "x"  # Error
```

---

## 22. Explain Python’s metaclasses.
**Answer:** Classes of classes, control class creation.  
**Explanation:** Used in frameworks/ORMs.  
**Code Example:**
```python
class Meta(type):
    def __new__(cls, name, bases, dct):
        print("Creating", name)
        return super().__new__(cls, name, bases, dct)

class My(metaclass=Meta): pass
```

---

## 23. Difference between `copy` and `deepcopy`?
**Answer:** `copy` keeps refs, `deepcopy` copies recursively.  
(Already explained in Q5 for clarity, but here reinforced as it’s frequently asked.)

---

## 24. Explain duck typing.
**Answer:** Behavior determined by methods, not inheritance.  
**Explanation:** “If it quacks like a duck, it’s a duck.”  
**Code Example:**
```python
class Duck:
    def quack(self): print("Quack")
class Person:
    def quack(self): print("I’m quacking like a duck")

def make_quack(obj): obj.quack()

make_quack(Duck())
make_quack(Person())
```

---

## 25. Explain Python’s typing module.
**Answer:** Provides type hints for static analysis.  
**Explanation:** Helps with readability and catching errors.  
**Code Example:**
```python
from typing import List

def square(nums: List[int]) -> List[int]:
    return [x*x for x in nums]
```

---

