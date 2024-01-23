# Context:
# This script takes a list of words as input, counts the occurrences of each word, and 
# prints the total number of unique words
# along with the count of each word. The order of input is preserved in the output.

# Importing necessary modules for word counting and ordering.
from collections import Counter, OrderedDict

# Creating a class that inherits from both Counter and OrderedDict to maintain order and count of words.
class OrderedCounter(Counter, OrderedDict):
    pass

# Initializing an empty list to store input words.
word_ar = []

# Taking the number of words as input.
n = int(input())

# Taking the words as input and adding them to the list.
for i in range(n):
    word_ar.append(input().strip())

# Creating an OrderedCounter object to count and maintain the order of words.
word_counter = OrderedCounter(word_ar)

# Printing the total number of unique words.
print(len(word_counter))

# Printing the count of each word along with their occurrences.
for word in word_counter:
    print(word_counter[word], end=" ")
