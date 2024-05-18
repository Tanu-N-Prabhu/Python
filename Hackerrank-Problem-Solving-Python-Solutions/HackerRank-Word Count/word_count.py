
"""
Problem: Word Count

Problem Description:

You are given a string consisting of words separated by spaces. Write a function `word_count(s)` 
to count the number of words in the string excluding any integer word.

Input Format:

- The input consists of a single line containing a string `s`, where `s` consists of 
lowercase English letters and spaces.
- The length of the string `s` is at most 10^5.

Output Format:

- Print a single integer representing the number of words in the string.

Sample Input:

```
hello world this is a sample string
```

Sample Output:

```
6
```

Explanation:

The string contains 6 words: "hello", "world", "this", "is", "a", and "sample". Therefore, the output is 6.
"""

# Counting occurrences of words in a string, ignoring numeric values using list comprehension
def count_non_numeric_words(sentence):
    words = sentence.split()
    # return count 1 if only one word otherwise check if not int then count
    word_count = sum(1 for word in words if not isinstance(word, int)) - 1
    return word_count

# Example usage
input_sentence = "This is a sample string 123 to count words from. This string contains repeated words."
non_numeric_word_count = count_non_numeric_words(input_sentence)
print(non_numeric_word_count)
