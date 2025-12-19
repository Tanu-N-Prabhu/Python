# Python Interview Questions and Answers - Strings 2025
## Master Advanced String Manipulation Techniques for Python Interviews

| ![space-1.jpg](https://github.com/Tanu-N-Prabhu/Python/blob/56b9c2ffea9d34a5b1d1d2243257a2eeeb9494eb/Img/gaelle-marcel-vrkSVpOwchk-unsplash.jpg)| 
|:--:| 
| Photo by <a href="https://unsplash.com/@gaellemarcel?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash">Gaelle Marcel</a> on <a href="https://unsplash.com/photos/person-holding-balloons-vrkSVpOwchk?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash">Unsplash</a> |



[![Hits](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2FTanu-N-Prabhu%2FPython%2Fblob%2F17433a8641945535243f296c5409d86bdbd037c9%2FPython%2520Coding%2520Interview%2520Prep%2FPython_Interview_Questions_and_Answers_Strings.md&count_bg=%2379C83D&title_bg=%23555555&icon=&icon_color=%23E7E7E7&title=hits&edge_flat=false)](https://hits.seeyoufarm.com)

# Introduction

Strings are a fundamental aspect of Python programming, playing a crucial role in many applications, from web development to data analysis. In technical interviews, string manipulation questions are commonly asked to evaluate a candidate’s problem-solving abilities and understanding of key programming concepts.

This repository focuses on advanced Python string interview questions and their solutions. It covers a wide range of topics, including permutations, palindromes, anagram grouping, regular expression matching, and more. Whether you're preparing for a coding interview or looking to enhance your Python skills, these examples will provide valuable insights and practical techniques to handle complex string problems efficiently.

Dive into these advanced string challenges and sharpen your skills to ace your next technical interview!

---

## 1. Python program to remove characters from a string


<details><summary><b>Hint</b></summary>
<p>

> **Input** - Python
>
> **Input Character** - o
>
> **Output** - Pythn

</p>
</details>

```python
str = "Python"
ch = "o"
print(str.replace(ch," ")) 

>> Pyth n

```

---

## 2. Python Program to count occurrence of characters in string

<details><summary><b>Hint</b></summary>
<p>

> **Input** - Python
>
> **Input Character** - o
>
> **Output** - 1

</p>
</details>

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
---

## 3. Python program in to check string is anagrams or not

<details><summary><b>Hint</b></summary>
<p>

> Input - Python
>
> Input Character - onypth
>
> Output - Anagrams
    
</p>
</details>

```python
str1 = "python"
str2 = "yonthp"
if (sorted(str1) == sorted(str2)):
    print("Anagram")
else:
    print("Not an anagram")
    
> Anagram

```

---

## 4. Python program to check string is palindrome or not

<details><summary><b>Hint</b></summary>
<p>

> Input - madam
>
> Output - Palindrome
    
</p>
</details>

```python
string = "madam"
if(string == string[:: - 1]):
   print("Palindrome")
else:
   print("Not a Palindrome") 

> Palindrome

```
---

## 5. Python code to check given character is digit or not

<details><summary><b>Hint</b></summary>
<p>

> Input - a
>
> Output - Not a Digit
    
</p>
</details>

```python
ch = 'a'
if ch >= '0' and ch <= '9': 
    	print("Digit")
else: 
    print("Not a Digit")
    
> Not a Digit


```
---

## 6. Program to replace the string space with any given character

<details><summary><b>Hint</b></summary>
<p>

> Input - m m
>    
> Input charcter - a
>
> Output - mam
    
</p>
</details>

```python
string = "m d m"
result = '' 
ch = "a"
for i in string:  
        if i == ' ':  
            i = ch   
        result += i  
print(result)
    
> madam

```

---

## 7. Check if Two Strings are Permutations of Each Other

```python
def are_permutations(s1: str, s2: str) -> bool:
    if len(s1) != len(s2):
        return False
    return sorted(s1) == sorted(s2)

# Example usage:
print(are_permutations("abc", "cab")) 

> True

```

---

## 8. Find All Permutations of a Given String

```python
from itertools import permutations

def string_permutations(s: str) -> list:
    return [''.join(p) for p in permutations(s)]

# Example usage:
print(string_permutations("ABC"))

> ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

```
---

## 9. Find the Longest Palindromic Substring

```python
def longest_palindromic_substring(s: str) -> str:
    def expand_around_center(left: int, right: int) -> str:
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left+1:right]
    
    longest = ""
    for i in range(len(s)):
        # Odd length palindrome
        substr1 = expand_around_center(i, i)
        # Even length palindrome
        substr2 = expand_around_center(i, i + 1)
        longest = max(longest, substr1, substr2, key=len)
    return longest

# Example usage:
print(longest_palindromic_substring("babad"))

> "bab" or "aba"

```
---

## 10. Count and Group Anagrams from a List of Strings

```python

from collections import defaultdict

def group_anagrams(words: list) -> dict:
    anagrams = defaultdict(list)
    for word in words:
        sorted_word = ''.join(sorted(word))
        anagrams[sorted_word].append(word)
    return dict(anagrams)

# Example usage:
print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))

> {'aet': ['eat', 'tea', 'ate'], 'ant': ['tan', 'nat'], 'abt': ['bat']}

```
---






<br>
<br>

[![Open Source](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://opensource.org/)
[![Maintened by - Tanu Nanda Prabhu](https://img.shields.io/badge/Maintained%20by-Tanu%20Nanda%20Prabhu-red)](https://tanu-n-prabhu.github.io/myWebsite.io/)
[![made-with-Markdown](https://img.shields.io/badge/Made%20with-Markdown-1f425f.svg)](http://commonmark.org)


