<h1 align = "center">Python Coding Interview Questions</h1>

<!-- Feature Image -->
| ![space-1.jpg](https://dyclassroom.com/image/topic/python/logo.png) | 
|:--:| 
| Image Credits [DY Classroom](https://dyclassroom.com/python/python-introduction) |

<!-- Content-->

# 1. Python Decimals - Converting an Integer into Decimals

```python
import decimal
integer = 10
print(decimal.Decimal(integer))
print(type(decimal.Decimal(integer)))

> 10
> <class 'decimal.Decimal'>

```

> Click [here](https://github.com/Tanu-N-Prabhu/Python/blob/master/Code%20Snapshots%20%F0%9F%93%B7/Python_Integer_to_Decimal.png) to view the Code Snapshot

---

# 2. Python Decimals - Converting an String of Integers into Decimals

```python
import decimal
string = '12345'
print(decimal.Decimal(string))
print(type(decimal.Decimal(string)))

> 12345
> <class 'decimal.Decimal'>

```

> Click [here](https://github.com/Tanu-N-Prabhu/Python/blob/master/Code%20Snapshots%20%F0%9F%93%B7/Python_String_to_Decimal.png) to view the Code Snapshot

---

# 3. Python Strings - Reversing a String using an Extended Slicing Technique

```python
string = "Python Programming"
print(string[::-1])

> gnimmargorP nohtyP

```

> Click [here](https://github.com/Tanu-N-Prabhu/Python/blob/master/Code%20Snapshots%20%F0%9F%93%B7/Python_String_Reversal.png) to view the Code Snapshot

---


# 4. Python Strings - Counting Vowels in a Given Word

```python
vowel = ['a', 'e', 'i', 'o', 'u']
word = "programming"
count = 0
for character in word:
    if character in vowel:
        count += 1
print(count)

> 3
```

> Click [here](https://github.com/Tanu-N-Prabhu/Python/blob/master/Code%20Snapshots%20%F0%9F%93%B7/Python_Vowel_Count.png) to view the Code Snapshot

---

# 5. Python Strings - Counting Consonants in a Given Word

```python
vowel = ['a', 'e', 'i', 'o', 'u']
word = "programming"
count = 0
for character in word:
    if character not in vowel:
        count += 1
print(count)

> 8
```

> Click [here](https://github.com/Tanu-N-Prabhu/Python/blob/master/Code%20Snapshots%20%F0%9F%93%B7/Python_Consonant_Count.png) to view the Code Snapshot

---


# 6. Python Strings - Counting the Number of Occurances of a Character in a String

```python
word = "python"
character = "p"
count = 0
for letter in word:
    if letter == character:
        count += 1
print(count)

> 1
```

> Click [here](https://github.com/Tanu-N-Prabhu/Python/blob/master/Code%20Snapshots%20%F0%9F%93%B7/Python_Character_Occurance_Count.png) to view the Code Snapshot

---

# 7. Python Lists - Writing Fibonacci Series

```python
fib = [0,1]
# Range starts from 0 by default
for i in range(5):  
    fib.append(fib[-1] + fib[-2]) 

# Converting the list of integers to string
print(', '.join(str(e) for e in fib))

> 0, 1, 1, 2, 3, 5, 8

```

> Click [here](https://github.com/Tanu-N-Prabhu/Python/blob/master/Code%20Snapshots%20%F0%9F%93%B7/Python_Fibonacci_Series.png) to view the Code Snapshot

---

# 8. Python Lists - Finding the Maximum Number in a List

```python
numberList = [15, 85, 35, 89, 125]

maxNum = numberList[0]
for num in numberList:
    if maxNum < num:
        maxNum = num
print(maxNum)

> 125

```

> Click [here](https://github.com/Tanu-N-Prabhu/Python/blob/master/Code%20Snapshots%20%F0%9F%93%B7/Python_Max_Number_List.png) to view the Code Snapshot

---

# 9. Python Lists - Finding the Minimum Number in a List

```python
numberList = [15, 85, 35, 89, 125, 2]

minNum = numberList[0]
for num in numberList:
    if minNum > num:
        minNum = num
print(minNum)

> 2

```

> Click [here](https://github.com/Tanu-N-Prabhu/Python/blob/master/Code%20Snapshots%20%F0%9F%93%B7/Python_Max_Number_List.png) to view the Code Snapshot

---










<br>
<br>

[![Open Source](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://opensource.org/)
[![Maintened by - Tanu Nanda Prabhu](https://img.shields.io/badge/Maintained%20by-Tanu%20Nanda%20Prabhu-red)](https://tanu-n-prabhu.github.io/myWebsite.io/)
[![made-with-Markdown](https://img.shields.io/badge/Made%20with-Markdown-1f425f.svg)](http://commonmark.org)

























