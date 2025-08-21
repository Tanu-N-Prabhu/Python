# Advanced Python Interview Questions

This document contains advanced-level Python interview questions with detailed answers and explanations. These are commonly asked in senior and specialized roles.

---

## 1. What are Python decorators, and how do they work?
A **decorator** is a function that modifies the behavior of another function or method. They are commonly used for logging, access control, caching, etc.

```python
def decorator(func):
    def wrapper(*args, **kwargs):
        print("Before function call")
        result = func(*args, **kwargs)
        print("After function call")
        return result
    return wrapper

@decorator
def say_hello():
    print("Hello")

say_hello()
```
**Explanation:** The `@decorator` syntax is shorthand for `say_hello = decorator(say_hello)`.

---

## 2. What is the Global Interpreter Lock (GIL), and why does it matter?
The **GIL** is a mutex in CPython that allows only one thread to execute Python bytecode at a time.  
- It simplifies memory management but limits true parallelism in CPU-bound tasks.  
- For I/O-bound tasks, multithreading still works well.  
- For CPU-bound tasks, use **multiprocessing** or C extensions.

---

## 3. What is the difference between `deepcopy` and `copy`?
- `copy.copy()` → creates a **shallow copy**, meaning nested objects are shared.  
- `copy.deepcopy()` → creates a **full independent copy**.

```python
import copy

a = [[1,2], [3,4]]
shallow = copy.copy(a)
deep = copy.deepcopy(a)

a[0][0] = 99
print(shallow)  # [[99, 2], [3, 4]] (changed)
print(deep)     # [[1, 2], [3, 4]] (independent)
```

---

## 4. How does Python manage memory?
- Uses **reference counting** as the primary mechanism.  
- Has a **cyclic garbage collector** to handle reference cycles.  
- Developers can use `gc` module for fine-grained control.  
- `__slots__` can be used in classes to reduce memory usage.

---

## 5. Explain Python's Method Resolution Order (MRO).
MRO defines the order in which base classes are searched when executing a method. Python uses **C3 linearization**.

```python
class A: pass
class B(A): pass
class C(A): pass
class D(B, C): pass

print(D.mro())
```
Output: `[D, B, C, A, object]`

---

## 6. What are metaclasses in Python?
A **metaclass** is a class of a class. It defines how classes behave.

```python
class Meta(type):
    def __new__(cls, name, bases, dct):
        print(f"Creating class {name}")
        return super().__new__(cls, name, bases, dct)

class MyClass(metaclass=Meta):
    pass
```
**Explanation:** When `MyClass` is created, `Meta.__new__` is called.

---

## 7. What are Python descriptors?
A **descriptor** is an object attribute with `__get__`, `__set__`, or `__delete__` methods.

```python
class Descriptor:
    def __get__(self, instance, owner):
        return "Got value"
    def __set__(self, instance, value):
        print(f"Set value {value}")

class MyClass:
    attr = Descriptor()

obj = MyClass()
print(obj.attr)
obj.attr = 42
```

---

## 8. How does `asyncio` differ from threading?
- `asyncio` → single-threaded, cooperative multitasking (coroutines).  
- `threading` → true OS threads, but limited by GIL.  
- `multiprocessing` → separate processes, bypass GIL.  

Use `asyncio` for **I/O-bound** high-concurrency tasks.

---

## 9. What are context managers? How do they work?
A context manager defines **setup and teardown logic** using `__enter__` and `__exit__` methods.

```python
class MyContext:
    def __enter__(self):
        print("Entering context")
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Exiting context")

with MyContext():
    print("Inside block")
```

---

## 10. What are `__slots__` in Python classes?
`__slots__` is used to limit the attributes that an object can have, saving memory.

```python
class MyClass:
    __slots__ = ['x', 'y']
    def __init__(self, x, y):
        self.x = x
        self.y = y

obj = MyClass(1,2)
# obj.z = 3  # AttributeError
```

---

## 11. Explain Python’s garbage collection mechanism.
- Uses **reference counting**.  
- Cyclic garbage collector detects and removes reference cycles.  
- `gc.collect()` can be called manually.  

---

## 12. How do you optimize performance in Python?
- Use built-in functions (C optimized).  
- Use list comprehensions instead of loops.  
- Use `multiprocessing` for CPU-bound tasks.  
- Use generators for large datasets.  
- Profile with `cProfile`.  

---

## 13. Explain duck typing in Python.
Python emphasizes **behavior over type**.  
If an object implements required methods, it can be used regardless of its class.

```python
def quack(obj):
    obj.quack()

class Duck:
    def quack(self): print("Quack!")

class Person:
    def quack(self): print("I'm quacking like a duck")

quack(Duck())
quack(Person())
```

---

## 14. What is monkey patching?
Dynamic modification of classes or modules at runtime.

```python
class MyClass:
    def hello(self):
        return "Hello"

def new_hello(self):
    return "Hi"

MyClass.hello = new_hello
print(MyClass().hello())  # Hi
```

---

## 15. What are Python type hints?
Introduced in PEP 484. Used to specify expected types.

```python
def greet(name: str) -> str:
    return "Hello " + name
```

Static analyzers (like `mypy`) can check type consistency.

---

## 16. Explain difference between `@classmethod`, `@staticmethod`, and instance methods.
- **Instance method** → needs `self`, operates on instance.  
- **Class method** → needs `cls`, operates on class.  
- **Static method** → no `self/cls`, utility function inside class.

```python
class MyClass:
    def instance_method(self): pass
    @classmethod
    def class_method(cls): pass
    @staticmethod
    def static_method(): pass
```

---

## 17. What are Python data classes?
Introduced in Python 3.7 (`dataclasses` module). Automatically generates `__init__`, `__repr__`, etc.

```python
from dataclasses import dataclass

@dataclass
class Point:
    x: int
    y: int
```

---

## 18. What are Python weak references?
Weak references allow referencing an object without increasing its reference count, useful for caches.

```python
import weakref

class MyClass: pass
obj = MyClass()
ref = weakref.ref(obj)
print(ref())
```

---

## 19. What is pickling and unpickling in Python?
Pickling = serializing Python objects.  
Unpickling = deserializing back to objects.

```python
import pickle

data = {'x': 1}
s = pickle.dumps(data)
print(pickle.loads(s))
```

---

## 20. How does `__new__` differ from `__init__`?
- `__new__` → creates a new instance (called before `__init__`).  
- `__init__` → initializes the created instance.

```python
class MyClass:
    def __new__(cls):
        print("Creating instance")
        return super().__new__(cls)
    def __init__(self):
        print("Initializing instance")
```

---

