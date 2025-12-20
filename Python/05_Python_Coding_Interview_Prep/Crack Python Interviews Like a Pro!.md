# Crack Python Interviews Like a Pro!
## Struggling with Python interview questions/concepts? 

| [![Discord](https://img.shields.io/discord/718138360538857794.svg?label=&logo=discord&logoColor=ffffff&color=7389D8&labelColor=6A7EC2)](https://discord.gg/qFryjbX)  | ![GitHub forks](https://img.shields.io/github/forks/Tanu-N-Prabhu/Python?label=Fork&style=social)  | ![GitHub stars](https://img.shields.io/github/stars/Tanu-N-Prabhu/Python?style=social) | ![GitHub repo size](https://img.shields.io/github/repo-size/Tanu-N-Prabhu/Python) |  ![GitHub contributors](https://img.shields.io/github/contributors/Tanu-N-Prabhu/Python)| [![Gitpod ready-to-code](https://img.shields.io/badge/Gitpod-ready--to--code-blue?logo=gitpod)](https://gitpod.io/#https://github.com/Tanu-N-Prabhu/Python)| [![commits](https://badgen.net/github/commits/Tanu-N-Prabhu/Python)](https://github.com/Tanu-N-Prabhu/Python/commits/main?icon=github&color=green)|![GitHub last commit (branch)](https://img.shields.io/github/last-commit/Tanu-N-Prabhu/Python/master?display_timestamp=committer)|![Views Counter](https://views-counter.vercel.app/badge?pageId=Tanu-N-Prabhu%2FViews-Counter)|
|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|

| ![space-1.jpg](https://github.com/Tanu-N-Prabhu/Python/blob/master/Img/rubaitul-azad-ZIPFteu-R8k-unsplash.jpg) | 
|:--:| 
| Photo by <a href="https://unsplash.com/@rubaitulazad?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash">Rubaitul Azad</a> on <a href="https://unsplash.com/photos/a-white-cube-with-a-yellow-and-blue-logo-on-it-ZIPFteu-R8k?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash">Unsplash</a> |

This repo has got you covered with optimized solutions, step-by-step explanations, and real interview problems from top tech companies.

* Master prevalent coding challenges with clear solutions
* Learn concepts with detailed explanations & visualizations
* Improve your skills with real-world examples & best practices
* Start learning now, level up your coding game, and land your dream job!
* **Follow** & **Star** this repo to stay updated with new questions!   

**Stay Connected**

* Follow me on [LinkedIn](https://ca.linkedin.com/in/tanu-nanda-prabhu-a15a091b5) for daily Python interview questions & insights!
* Read my articles on [Medium](https://medium.com/@tanunprabhu95) for in-depth explanations & tutorials!
* Got a different solution? Drop your thoughts in the discussions! Let’s learn together! 

<p align = "right"> Written by <a href = "https://medium.com/@tanunprabhu95">Tanu Nanda Prabhu</a></p>

---

### 1) Two Sum Problem – Efficient Python Solution
#### Problem Statement
You are given an array of numbers and a target sum. Your task is to find the indices of the two numbers that add up to the target.

##### Example
```python
nums = [2, 7, 11, 15]
target = 9
# Output: [0, 1] (Because 2 + 7 = 9)
```

#### Optimized Approach – Hash Map
Instead of using a brute-force approach with two loops, we can solve this problem efficiently using a hash map (dictionary).
##### Solution Code
```python
def two_sum(nums, target):
    num_map = {}  # Stores number and its index
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_map:
            return [num_map[complement], i]
        num_map[num] = i
    return []  # No solution found
```
#### Why is this efficient?
* Time Complexity: O(n) – We iterate through the list once.
* Space Complexity: O(n) – Stores numbers and their indices in a dictionary.
* Got another approach? Share it below!
* Follow this repository for more interview questions & solutions!


---

### 2) Mastering Python Data Structures in One Go! 
Understanding data structures is key to writing efficient Python code. Here’s a quick breakdown of four essential types

* List – Ordered, mutable, allows duplicates
* Tuple – Ordered, immutable, allows duplicates
* Set – Unordered, mutable, no duplicates
* Dictionary – Key-value pairs, unordered, mutable
  
**Quick comparison with an example**

```python
# List vs Tuple vs Set vs Dictionary
my_list = [1, 2, 3, 3]  # Allows duplicates
my_tuple = (1, 2, 3, 3)  # Immutable but allows duplicates
my_set = {1, 2, 3, 3}  # No duplicates
my_dict = {"a": 1, "b": 2, "c": 3}  # Key-value storage

print(my_list, my_tuple, my_set, my_dict)
```

**When to use what?**

* Use lists when order matters and you need modifications.
* Use tuples when you want an unchangeable sequence.
* Use sets when you need unique elements.
* Use dictionaries when you need fast key-based lookups.  

---

### 3) Python’s Memory Efficiency: Mutable vs Immutable

Mutable Objects (list, dict, set)

* Can be modified after creation.
* Stored in memory at the same location even after modification.
* Not hashable (can’t be used as dictionary keys).
* Changes affect all references pointing to the object.
* Efficient when frequent modifications are needed.

Immutable Objects (int, str, tuple)

* Cannot be modified after creation
* Every modification creates a new object in memory
* Hashable (can be used as dictionary keys)
* Changes do not affect other references
* Can be inefficient if modified frequently   

> Fun Fact: Python reuses small immutable objects (like numbers -5 to 256 and short strings) to save memory!

---

### 4) Lazy Evaluation in Python (Generators vs Lists)

* Lists store all elements in memory, consuming more space.
* Generators produce values on demand, saving memory.
* That’s why range(10**6) is more efficient than `[x for x in range(10**6)]`.

---

### 5) Python’s Interning Mechanism (Why `a is b` Might Be True)

* Python optimizes memory by reusing small integers (-5 to 256) and short strings.
* Example: `a = 256` and `b = 256` → `a is b` ✅
* But `a = 257` and `b = 257` → `a is b` ❌ (because 257 is outside the cached range)

---

### 6)  Decorator Magic: Functions That Modify Functions

* Decorators wrap a function, adding behavior without changing its original code.
* Used in logging, caching, authentication, and more.
* Example: `@lru_cache` speeds up recursive functions by storing previous results.

---

### 7) Packing & Unpacking: Python’s Tuple Trick

* `a, b = b, a` works because Python automatically packs values into tuples and unpacks them efficiently.
* This concept is used in function arguments `(*args, **kwargs)` to handle dynamic inputs.

---

### 8) Python Unpacking: The Hidden Power of Simplicity
Ever swapped values in Python without using a temp variable? That’s tuple unpacking in action! 

##### What’s happening?

Python automatically packs values into a tuple and then unpacks them into variables.
This isn’t just for swapping—it's also used in loops, function returns, and argument unpacking!

##### Why it matters

* Cleaner syntax
* Fewer lines of code
* More readable logic   

> **Fun Fact**: Python doesn’t need a `swap()` function like other languages — thanks to unpacking, it’s built right into the language! One of the few languages where swapping values is truly one line, no tricks needed.

---

### 9) Python Scopes: How Your Variables Live and Die

Ever wondered why some variables disappear or seem "undefined"? That’s because of Python’s scope rules — the LEGB rule!

##### LEGB stands for

* Local – Inside a function
* Enclosing – In nested functions
* Global – At the top level of the script
* Built-in – Provided by Python itself

##### Why it matters
Understanding the scope prevents bugs, avoids variable conflicts, and helps you write clean, modular code.

> **Fun Fact**: Python reads variables from the innermost to the outermost scope — it won't even look at global variables if something local exists!

---
### 10) Python’s Identity vs Equality, `is` vs `==`

These two look similar, but they’re different! 

* `==` checks if values are equal
* `is` checks if they’re the same object in memory

##### Why it matters

* Two objects can be equal in value but not identical in memory
* Misusing them can cause confusing bugs
* Especially important when working with mutable data types and None checks

> **Fun Fact**: Python _interns small integers_ and strings, so `a is b` might return `True` even if you didn’t expect it. But don’t rely on it—it’s an optimization, not a rule!

---

### 11) Python Metaclasses: The Class of a Class

Ever heard the phrase: “Everything in Python is an object”?
Well, even classes are objects! And the blueprint for those? That’s where metaclasses come in.

##### What is a Metaclass?
A metaclass is what creates classes, just like classes create objects. It’s the “behind-the-scenes architect” of Python’s object model.

##### Why it matters:
* Used to control class creation
* Great for customizing class behavior across a codebase
* Powerful in frameworks like Django and ORMs for auto-generating code

> **Fun Fact**: The default metaclass in Python is type — yes, _type()_ not only tells you what something is... It’s also how classes are built!

---

### 12) Vectorization in NumPy

Why loops are out and speed is in?

##### Why is it so important

Vectorization in NumPy allows you to apply operations on whole arrays without writing manual loops. It’s cleaner, faster, and ideal for handling large datasets. Using optimized C code under the hood supercharges performance and is a must-know for every data scientist.

> **Fun Fact**: NumPy vectorized ops can be 100x faster than regular Python loops!

```python
import numpy as np
import time

# Setup
size = 1_000_000
a = np.random.rand(size)
b = np.random.rand(size)

# Traditional loop
start = time.time()
result_loop = []
for i in range(size):
    result_loop.append(a[i] + b[i])
print("Loop Time:", round(time.time() - start, 4), "seconds")

# Vectorized with NumPy
start = time.time()
result_vectorized = a + b
print("Vectorized Time:", round(time.time() - start, 4), "seconds")

```

##### What It Shows
* The loop takes significantly longer to perform the addition.
* The vectorized approach is lightning fast and cleaner.

---


### 13) Understanding Lazy Evaluation in Python

How Python delays execution to optimize performance?

##### Why is it so important

Lazy evaluation is a powerful concept that helps Python save memory and compute only when needed. It’s often used in iterators, generators, and libraries like Pandas or NumPy, especially when dealing with huge datasets.

> **Fun Fact**: Python’s `range()` is lazy, it doesn’t generate all numbers at once, just the one you ask for!


```python
# Generator function (lazy)
def lazy_numbers():
    for i in range(1, 6):
        print(f"Generating {i}")
        yield i

# Using the generator
gen = lazy_numbers()

for num in gen:
    print(f"Using {num}")

```

##### What It Shows
* Values are generated one at a time, only when needed.
* No upfront memory usage — great for large or infinite data.
* `yield` makes functions behave lazily like iterators.

---


### 14) Feature Scaling with Scikit-Learn

Prepare your data the right way for better ML results

##### Why is it so important

Feature scaling is the backbone of good model performance. Without it, algorithms like KNN, SVM, or Gradient Descent-based models can give poor or biased results. It ensures all features contribute equally, especially when they’re on different scales.

> **Fun Fact**: Not scaling your features can make even the best model perform worse than a basic one. Tiny preprocessing = huge difference in accuracy! 


```python
from sklearn.preprocessing import StandardScaler
import numpy as np

# Sample data: [height (cm), weight (kg)]
X = np.array([[170, 65], [180, 85], [160, 55]])

scaler = StandardScaler()
scaled_X = scaler.fit_transform(X)

print(scaled_X)

```

##### What It Shows
* Your features (height, weight) are standardized (mean = 0, std = 1)
* This makes all features equally important during model training
* Easy plug-and-play with any ML pipeline

---

### 15) One-Hot Encoding Explained

Make categories readable for machine learning

##### Why is it so important

Machine learning models can’t process text directly, they need numbers. One-hot encoding turns categorical variables into binary vectors without implying any order, making them model-friendly without misleading the algorithm.

###### Summary

* Converts categorical data into numerical format
* Prevents false assumptions of order in categories
* Essential for most ML models like logistic regression, trees, and neural nets
* Built into pandas and scikit-learn


> **Fun Fact**: One-hot encoded vectors are often sparse, most values are 0. That’s why ML frameworks optimize their storage behind the scenes!




```python

import pandas as pd

# Sample data
df = pd.DataFrame({
    'Color': ['Red', 'Blue', 'Green', 'Blue']
})

# One-hot encoding
encoded = pd.get_dummies(df, columns=['Color'])

print(encoded)

```

##### What It Shows

* Converts each category in the `Color` column into its binary column
* Each row has a 1 in the column that matches its category
* Zero assumption of order, pure categorical handling

---
