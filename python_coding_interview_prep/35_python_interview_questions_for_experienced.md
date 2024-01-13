# Python Coding Interview Questions And Answers

Here Coding compiler sharing a list of 35 Python interview questions for experienced. These Python questions are prepared by expert Python developers. This list of interview questions on Python will help you to crack your next Python job interview. All the best for your future and happy [python learning](https://codingcompiler.com/python-coding-interview-questions-answers/)


## 1. Debugging a Python Program

```python
# By using this command we can debug a python program
python -m pdb python-script.py
```

---

## 2. Yield Keyword in Python
### The keyword in Python can turn any function into a generator. Yields work like a standard return keyword.

```python
def days(index):
    day = ['S','M','T','W','Tr','F','St']            
    yield day[index]    
    yield day[index+1]  
  
res = days(0)
print(next(res), next(res))

> S M
```
----

## 3. Converting a List into a String
### When we want to convert a list into a string, we can use the `<.join()>` method which joins all the elements into one and returns as a string.

```python
days = ['S','M','T','W','Tr','F','St'] 
ltos = ' '.join(days)
print(ltos)

> S M T W Tr F St
```
---

## 4. Converting a List into a Tuple
### By using Python `<tuple()>` function we can convert a list into a tuple. But we can’t change the list after turning it into tuple, because it becomes immutable.

```python
days = ['S','M','T','W','Tr','F','St'] 
ltos = tuple(days)
print(ltos)

> ('S', 'M', 'T', 'W', 'Tr', 'F', 'St')
```
---


## 5. Converting a List into a Set
### User can convert list into set by using `<set()>` function.

```python
days = ['S','M','T','W','Tr','F','St'] 
ltos = set(days)
print(ltos)

> {'T', 'W', 'M', 'F', 'S', 'Tr', 'St'}
```
---

## 6. Counting the occurrences of a particular element in the list
### We can count the occurrences of an individual element by using a `<count()>` function.

```python
days = ['S','M','W', 'M','M','F','S']

print(days.count('M'))

> 3
```
---

### 6.1. Counting the occurrences of elements in the list

```python
days = ['S','M','M','M','F','S']
y = set(days)

# this is just like value_counts() in pandas and Counter in dict
print([[x,days.count(x)] for x in y])

> [['M', 3], ['S', 2], ['F', 1]]
```

---

## 7. Creating a NumPy Array in Python
### NumPy arrays are more flexible then lists in Python.

```python
import numpy as np

arr = np.array([1, 2, 3, 4, 5])

print(arr)
print(type(arr))

> [1 2 3 4 5]
  <class 'numpy.ndarray'>
  
  ```
  ---



---


