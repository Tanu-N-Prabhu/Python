
# Python Engineering Design Principles

Python design principles help engineers write clean, maintainable, and efficient code that scales in production environments. Below are the core principles and practices.

---

## 1. Readability Counts (PEP 8 & Zen of Python)

- Follow PEP 8 style guide.
- Zen of Python: `import this`

**Example:**
```python
def add_numbers(a, b):
    '''Return the sum of two numbers.'''
    return a + b
```

---

## 2. DRY (Don’t Repeat Yourself)

**Example:**
```python
def calculate_total(price, tax):
    return price + tax
```

---

## 3. KISS (Keep It Simple, Stupid)

**Example:**
```python
def is_even(n):
    return n % 2 == 0
```

---

## 4. Modularity

**Example Directory Structure:**
```
my_project/
├─ data_processing/
├─ models/
└─ main.py
```

---

## 5. Encapsulation and Abstraction

**Example:**
```python
class BankAccount:
    def __init__(self, balance):
        self._balance = balance

    def deposit(self, amount):
        self._balance += amount

    def get_balance(self):
        return self._balance
```

---

## 6. Composition over Inheritance

**Example:**
```python
class Engine:
    def start(self):
        print("Engine started")

class Car:
    def __init__(self):
        self.engine = Engine()

    def start(self):
        self.engine.start()
```

---

## 7. Use of Pythonic Idioms

**Example:**
```python
squares = (x*x for x in range(10))

with open("data.txt") as f:
    content = f.read()
```

---

## 8. Immutability and Constants

**Example:**
```python
MAX_RETRIES = 5
DAYS_IN_WEEK = 7
```

---

## 9. Error Handling (EAFP vs LBYL)

**Example (EAFP):**
```python
try:
    value = my_dict["key"]
except KeyError:
    value = None
```

---

## 10. Testing and Testability

**Example (pytest):**
```python
def add(a, b):
    return a + b

def test_add():
    assert add(2, 3) == 5
```

---

## 11. Performance and Efficiency

**Example:**
```python
total = sum(x*x for x in range(1000000))
```

---

## 12. Concurrency and Parallelism

**Example (asyncio):**
```python
import asyncio

async def fetch_data():
    await asyncio.sleep(1)
    return "data"

async def main():
    results = await asyncio.gather(fetch_data(), fetch_data())
    print(results)

asyncio.run(main())
```

---

## 13. Logging and Observability

**Example:**
```python
import logging

logging.basicConfig(level=logging.INFO)
logging.info("Process started")
```

---

## 14. Dependency Management

**Example requirements.txt:**
```
numpy==1.26.0
pandas==2.2.0
```

---

## 15. Documentation and Maintainability

**Example:**
```python
def greet(name: str) -> str:
    '''Return a greeting message for the given name.'''
    return f"Hello, {name}!"
```

---

## 16. Version Control and Code Review

- Use Git branching strategies.  
- Conduct code reviews regularly.

---

## Summary of Principles

| Principle                | Key Idea                                           |
|--------------------------|--------------------------------------------------|
| Readability              | Code should be clean and easy to understand     |
| DRY                      | Don’t repeat yourself                            |
| KISS                     | Keep it simple                                   |
| Modularity               | Split code into modules                          |
| Encapsulation            | Hide internal state                              |
| Composition over Inheritance | Prefer flexible relationships                  |
| Pythonic Idioms          | Use Python’s built-in features                  |
| Immutability             | Use constants and immutable types               |
| EAFP                     | Prefer exception handling                        |
| Testability              | Small, testable units                            |
| Performance              | Optimize using Python constructs                 |
| Concurrency              | Async for I/O, multiprocessing for CPU          |
| Logging                  | Use structured logging                           |
| Dependency Management    | Virtual environments and pinned dependencies   |
| Documentation            | Docstrings, type hints, maintainable code       |
