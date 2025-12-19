# Python Interview Questions
### Designed for Tier 1 Companies

_**Written By**: Tanu Nanda Prabhu_

This file contains 20 Python interview questions with answers and
explanations.
Each section includes:
1. **Question**
2. **Python Solution (runnable in Colab)**
3. **Step-by-Step Explanation**

------------------------------------------------------------------------

## 1. Reverse a String in Python

``` python
s = "hello"
reversed_s = s[::-1]
print(reversed_s)  # Output: "olleh"
```

**Explanation:**
- `[::-1]` reverses the string.

------------------------------------------------------------------------

## 2. Check if a String is a Palindrome

``` python
def is_palindrome(word):
    return word == word[::-1]

print(is_palindrome("madam"))  # True
print(is_palindrome("hello"))  # False
```

**Explanation:** Compare the word with its reverse.

------------------------------------------------------------------------

## 3. Factorial of a Number

``` python
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n-1)

print(factorial(5))  # 120
```

**Explanation:** Uses recursion.

------------------------------------------------------------------------

## 4. Fibonacci Sequence

``` python
def fibonacci(n):
    seq = [0, 1]
    for i in range(2, n):
        seq.append(seq[-1] + seq[-2])
    return seq

print(fibonacci(10))
```

**Explanation:** Each number is sum of previous two.

------------------------------------------------------------------------

## 5. Find Maximum in a List

``` python
nums = [3, 9, 2, 5, 7]
print(max(nums))  # 9
```

**Explanation:** `max()` finds largest number.

------------------------------------------------------------------------

## 6. Remove Duplicates from List

``` python
nums = [1, 2, 2, 3, 4, 4, 5]
unique_nums = list(set(nums))
print(unique_nums)  # [1, 2, 3, 4, 5]
```

**Explanation:** `set` keeps unique values.

------------------------------------------------------------------------

## 7. Check Anagram

``` python
def is_anagram(s1, s2):
    return sorted(s1) == sorted(s2)

print(is_anagram("listen", "silent"))  # True
```

**Explanation:** Sorted letters must match.

------------------------------------------------------------------------

## 8. Count Vowels

``` python
s = "hello world"
vowels = "aeiou"
count = sum(1 for char in s if char in vowels)
print(count)  # 3
```

**Explanation:** Loop and count vowels.

------------------------------------------------------------------------

## 9. Second Largest Number

``` python
nums = [10, 5, 8, 20, 15]
nums = list(set(nums))
nums.sort()
print(nums[-2])  # 15
```

**Explanation:** Sort and pick second last.

------------------------------------------------------------------------

## 10. Sum of Digits

``` python
n = 1234
digit_sum = sum(int(digit) for digit in str(n))
print(digit_sum)  # 10
```

**Explanation:** Convert number to string, sum digits.

------------------------------------------------------------------------

## 11. Prime Numbers up to N

``` python
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

primes = [x for x in range(50) if is_prime(x)]
print(primes)
```

**Explanation:** Check divisibility up to √n.

------------------------------------------------------------------------

## 12. Missing Number in List

``` python
nums = [1, 2, 3, 5]
n = len(nums) + 1
expected_sum = n * (n+1) // 2
actual_sum = sum(nums)
print(expected_sum - actual_sum)  # 4
```

**Explanation:** Compare expected vs actual sum.

------------------------------------------------------------------------

## 13. Check if List is Sorted

``` python
nums = [1, 2, 3, 4, 5]
print(nums == sorted(nums))  # True
```

**Explanation:** Compare with sorted list.

------------------------------------------------------------------------

## 14. Find GCD

``` python
import math
print(math.gcd(48, 18))  # 6
```

**Explanation:** Uses built-in gcd.

------------------------------------------------------------------------

## 15. Find LCM

``` python
import math
def lcm(a, b):
    return abs(a*b) // math.gcd(a, b)

print(lcm(12, 15))  # 60
```

**Explanation:** Formula: (a\*b)/GCD.

------------------------------------------------------------------------

## 16. Flatten 2D List

``` python
matrix = [[1, 2], [3, 4], [5, 6]]
flat = [num for row in matrix for num in row]
print(flat)  # [1, 2, 3, 4, 5, 6]
```

**Explanation:** Nested list comprehension.

------------------------------------------------------------------------

## 17. Frequency of Elements

``` python
from collections import Counter
nums = [1, 2, 2, 3, 3, 3]
print(Counter(nums))  # {1:1, 2:2, 3:3}
```

**Explanation:** Counter counts frequencies.

------------------------------------------------------------------------

## 18. Merge Two Sorted Lists

``` python
list1 = [1, 3, 5]
list2 = [2, 4, 6]
merged = sorted(list1 + list2)
print(merged)
```

**Explanation:** Concatenate and sort.

------------------------------------------------------------------------

## 19. Intersection of Lists

``` python
list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]
intersection = list(set(list1) & set(list2))
print(intersection)  # [3, 4]
```

**Explanation:** `&` finds common elements.

------------------------------------------------------------------------

## 20. Find Duplicates in List

``` python
nums = [1, 2, 2, 3, 4, 4, 5]
duplicates = [num for num in set(nums) if nums.count(num) > 1]
print(duplicates)  # [2, 4]
```

**Explanation:** Check elements with count \> 1.

------------------------------------------------------------------------

> These 20 questions cover strings, lists, recursion, math, primes, anagrams, frequency, and arrays useful for Tier 1 Python interviews.
