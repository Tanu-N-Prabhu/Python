# Python Interview Questions and Answers - Strings


## 1. Python program to remove character from string

**Input String**: Python

**Input Character** : o

**Output**: Pythn

```python
str = "Python"
ch = "o"
print(str.replace(ch," ")) 

>> Pyth n

```

## 2. Python Program to count occurrence of characters in string


**Input String**: Python

**Input Character** : o

**Output**: 1

```python
string = "Python"
char = "y"
count = 0
for i in range(len(string)):
    if(string[i] == char):
        count = count + 1
print(count)

>> 1

```
