"""
Problem: Double Base Palindromes

Problem Description:

A double base palindrome is a number that is a palindrome in both its decimal (base 10) 
and binary (base 2) representations. For example, the number 585 is 
a double base palindrome because it reads the same forwards and backwards in both decimal and binary: 
585 (decimal) = 1001001001 (binary).

Write a function `double_base_palindromes(n)` that takes a positive integer `n` as input and 
returns the count of double base palindromes less than or equal to `n`.

Input Format:

- The input consists of a single integer `n` (1 ≤ n ≤ 10^6), representing the upper limit 
for the search of double base palindromes.

Output Format:

- Print a single integer representing the count of double base palindromes less than or equal to `n`.

Sample Input:

```
100
```

Sample Output:

```
10
```

Explanation:

The double base palindromes less than or equal to 100 are: 1, 3, 5, 7, 9, 33, 99. Therefore, the output is 7.
"""

# check the string is palindrome or not
def is_palindrome(s):
    # checking string with its reverse are same or not
    return s == s[::-1]


# convert a int to binary
def to_binary(n):
    # taking from 3rd character as first two would be 0b for bin number
    return bin(n)[2:]

# calculate the sum of all palindromes
def sum_double_base_palindromes(n):
    # loop till the input and check if both palindrom of the number and palindrome of it's binary number are same or not
    double_base_palindromes = [i for i in range(1, n+1) if is_palindrome(str(i)) \
    and is_palindrome(to_binary(i))]
    return sum(double_base_palindromes)


input_num = 5
output = sum_double_base_palindromes(input_num)
print(output)
