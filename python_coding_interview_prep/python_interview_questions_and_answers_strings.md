# Python Interview Questions and Answers - Strings


## 1. Python program to remove character from string


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
