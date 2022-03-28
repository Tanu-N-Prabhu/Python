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


## 3. Python program in to check string is anagrams or not

Input String: Python

Input Character: onypth

Output: Anagrams


```python
str1 = "python"
str2 = "yonthp"
if (sorted(str1) == sorted(str2)):
    print("Anagram")
else:
    print("Not an anagram")
    
> Anagram

```

## 4. Python program to check string is palindrome or not

Input String: madam

Output: Palindrome

```python
string = "madam"
if(string == string[:: - 1]):
   print("Palindrome")
else:
   print("Not a Palindrome") 

> Palindrome

```
