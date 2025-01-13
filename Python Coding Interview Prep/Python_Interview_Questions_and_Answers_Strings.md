# Python Interview Questions and Answers - Strings

| ![space-1.jpg](https://github.com/Tanu-N-Prabhu/Python/blob/56b9c2ffea9d34a5b1d1d2243257a2eeeb9494eb/Img/gaelle-marcel-vrkSVpOwchk-unsplash.jpg)| 
|:--:| 
| Photo by <a href="https://unsplash.com/@gaellemarcel?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash">Gaelle Marcel</a> on <a href="https://unsplash.com/photos/person-holding-balloons-vrkSVpOwchk?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash">Unsplash</a> |



[![Hits](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2FTanu-N-Prabhu%2FPython%2Fblob%2F17433a8641945535243f296c5409d86bdbd037c9%2FPython%2520Coding%2520Interview%2520Prep%2FPython_Interview_Questions_and_Answers_Strings.md&count_bg=%2379C83D&title_bg=%23555555&icon=&icon_color=%23E7E7E7&title=hits&edge_flat=false)](https://hits.seeyoufarm.com)

## 1. Python program to remove characters from string


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
