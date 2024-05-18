"""
Problem: Perfect Substring

Problem Description:

A perfect substring is a substring of a string in which all characters have the same frequency. 
For example, in the string "1102021222", the substring "1222" is a perfect substring 
because all its characters (1, 2, and 0) have the same frequency.

Given a string `s` and a positive integer `k`, your task is to find and 
count all perfect substrings of length `k` in the given string `s`.

Write a function `perfect_substring(s, k)` that takes a string `s` and an integer `k` as input 
and returns the count of perfect substrings of length `k`.

Input Format:

- The input consists of two lines:
  - The first line contains a string `s` (1 ≤ |s| ≤ 10^5), where |s| denotes the length of the string.
  - The second line contains a single integer `k` (1 ≤ k ≤ |s|), representing the length of 
  the perfect substrings to be searched.

Output Format:

- Print a single integer representing the count of perfect substrings of length `k` in the given string `s`.

Sample Input:

```
1102021222
2
```

Sample Output:

```
2
```

**Explanation:**

In the string "1102021222", the perfect substrings of length 2 are "11" and "22", as they each consist of two identical characters. 
Therefore, the output is 2.
"""

# perfect substings
def perfect_substrings(s, k):
    # Initialize count variable to store the count of perfect substrings
    count = 0
    
    # Iterate over each index i in the string s
    for i in range(len(s)):
        # Iterate over each index j from i+1 to the end of the string s
        for j in range(i + 1, len(s) + 1):
            # Extract the substring from index i to j
            substring = s[i:j]
            # Initialize a dictionary to store the frequency of characters in the substring
            freq = {}
            # Iterate over each character in the substring
            for char in substring:
                # Increment the frequency count of the character in the dictionary
                freq[char] = freq.get(char, 0) + 1
            # Check if all character frequencies in the substring are equal to k
            if all(value == k for value in freq.values()):
                # If all frequencies are equal to k, increment the count of perfect substrings
                count += 1
    
    # Return the count of perfect substrings
    return count


s = "string"
k = 2
result = perfect_substrings(s, k)
print(result)
