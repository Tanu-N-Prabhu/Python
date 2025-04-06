# 🚀 Crack Python Interviews Like a Pro!
## 💻 Struggling with Python interview questions/concepts? 

This repo has got you covered with optimized solutions, step-by-step explanations, and real interview problems from top tech companies.

✅ Master prevalent coding challenges with clear solutions   
✅ Learn concepts with detailed explanations & visualizations   
✅ Improve your skills with real-world examples & best practices   
⚡ Start learning now, level up your coding game, and land your dream job!   
🔔 Follow & ⭐ Star this repo to stay updated with new questions!   

📢 **Stay Connected**

🔗 Follow me on [LinkedIn](https://ca.linkedin.com/in/tanu-nanda-prabhu-a15a091b5) for daily Python interview questions & insights!   
📝 Read my articles on [Medium](https://medium.com/@tanunprabhu95) for in-depth explanations & tutorials!   
💬 Got a different solution? Drop your thoughts in the discussions! Let’s learn together! 🧠🔥

<p align = "right"> Written by <a href = "https://medium.com/@tanunprabhu95">Tanu Nanda Prabhu</a></p>

---

### 1) Two Sum Problem – Efficient Python Solution 💻⚡
#### Problem Statement
You are given an array of numbers and a target sum. Your task is to find the indices of the two numbers that add up to the target.

##### 📝 Example
```python
nums = [2, 7, 11, 15]
target = 9
# Output: [0, 1] (Because 2 + 7 = 9)
```

#### 🚀 Optimized Approach – Hash Map 🗂️
💡 Instead of using a brute-force approach with two loops, we can solve this problem efficiently using a hash map (dictionary).
##### 📝 Solution Code
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
#### 🔎 Why is this efficient? 🤔
✅ Time Complexity: O(n) – We iterate through the list once.  
✅ Space Complexity: O(n) – Stores numbers and their indices in a dictionary.  
💬 Got another approach? Share it below! 🗣️👇  
📌 Follow this repository for more interview questions & solutions! ⭐  


---

### 2) Mastering Python Data Structures in One Go! 🚀🐍
Understanding data structures is key to writing efficient Python code. Here’s a quick breakdown of four essential types

🔹 List – Ordered, mutable, allows duplicates  
🔹 Tuple – Ordered, immutable, allows duplicates  
🔹 Set – Unordered, mutable, no duplicates  
🔹 Dictionary – Key-value pairs, unordered, mutable  

💡 Quick comparison with an example

```python
# List vs Tuple vs Set vs Dictionary
my_list = [1, 2, 3, 3]  # Allows duplicates
my_tuple = (1, 2, 3, 3)  # Immutable but allows duplicates
my_set = {1, 2, 3, 3}  # No duplicates
my_dict = {"a": 1, "b": 2, "c": 3}  # Key-value storage

print(my_list, my_tuple, my_set, my_dict)
```

🔥 When to use what?

✔ Use lists when order matters and you need modifications.  
✔ Use tuples when you want an unchangeable sequence.  
✔ Use sets when you need unique elements.  
✔ Use dictionaries when you need fast key-based lookups.  

Which data structure do you use the most in Python? Drop your thoughts in the comments! 👇

---

### 3) Python’s Memory Efficiency: Mutable vs Immutable

Mutable Objects (list, dict, set)

✅ Can be modified after creation   
✅ Stored in memory at the same location even after modification   
❌ Not hashable (can’t be used as dictionary keys)   
✅ Changes affect all references pointing to the object   
✅ Efficient when frequent modifications are needed   

Immutable Objects (int, str, tuple)

❌ Cannot be modified after creation   
❌ Every modification creates a new object in memory   
✅ Hashable (can be used as dictionary keys)   
✅ Changes do not affect other references   
❌ Can be inefficient if modified frequently   

> 💡 Fun Fact: Python reuses small immutable objects (like numbers -5 to 256 and short strings) to save memory!

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

✅ Cleaner syntax   
✅ Fewer lines of code   
✅ More readable logic   

> **Fun Fact**: Python doesn’t need a `swap()` function like other languages — thanks to unpacking, it’s built right into the language! One of the few languages where swapping values is truly one line, no tricks needed.

---

### 9) Python Scopes: How Your Variables Live and Die

Ever wondered why some variables disappear or seem "undefined"? That’s because of Python’s scope rules — the LEGB rule! 🕵️‍♂️

##### LEGB stands for

* Local – Inside a function
* Enclosing – In nested functions
* Global – At the top level of the script
* Built-in – Provided by Python itself

##### Why it matters
Understanding the scope prevents bugs, avoids variable conflicts, and helps you write clean, modular code.

> **Fun Fact**: Python reads variables from the innermost to the outermost scope — it won't even look at global variables if something local exists!

---

