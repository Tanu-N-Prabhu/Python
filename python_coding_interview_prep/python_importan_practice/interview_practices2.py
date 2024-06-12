from functools import wraps
import re

movies = [
    "The Godfather, 1972, Francis Ford Coppola",
    "Pather Panchali, 1975, Satyajit Ray",
]
# Compile a regular expression to print only movie name and director name
pattern = re.compile(r", \d+, ")

movies_without_year = []
for movie in movies:
    # Retrieve a movie name and its director
    split_result = re.split(pattern, movie)
    # Create a new string with a movie name and its director
    movie_and_director = ", ".join(split_result)
    # Append the resulting string to movies_without_year
    movies_without_year.append(movie_and_director)

for movie in movies_without_year:
    print(movie)


college_years = ["Freshman", "Sophomore", "Junior", "Senior"]
print(list(enumerate(college_years, 2019)))
# [(2019, 'Freshman'), (2020, 'Sophomore'), (2021, 'Junior'), (2022, 'Senior')]

fruits = ["Apples", "Oranges", "Bananas"]
quantities = [5, 3, 4]
prices = [1.50, 2.25, 0.89]
# Desired output
# [('Apples', 5, 1.50), ('Oranges', 3, 2.25), ('Bananas', 4, 0.89)]
list(zip(fruits, quantities, prices))


# how to write the doc test
def sum(a, b):
    """
    >>> sum(4, 3)
    7

    >>> sum(-4, 5)
    1
    """
    return a + b


def makebold(fn):
    @wraps(fn)
    def wrapped(*args, **kwargs):
        return "<b>" + fn(*args, **kwargs) + "</b>"

    return wrapped


def makeitalic(fn):
    @wraps(fn)
    def wrapped(*args, **kwargs):
        return "<i>" + fn(*args, **kwargs) + "</i>"

    return wrapped


@makebold
@makeitalic
def hello():
    return "hello world"


@makebold
@makeitalic
def log(s):
    return s


print(hello())  # returns "<b><i>hello world</i></b>"
print(hello.__name__)  # with functools.wraps() this returns "hello"
print(log("hello"))  # returns "<b><i>hello</i></b>"

# get every third element of a list
thelist = [1, 2, 3, 4, 5]
[x for i, x in enumerate(thelist) if i % 3 == 0]


# calculate sum for even position elements using enumerate()
def sum_even_position(lst):
    total = 0
    for i, element in enumerate(lst):
        if i % 2 == 0:
            total += element
    return total


# calculate sum for even position elements using range()
def sum_even_position(lst):
    total = 0
    for i in range(0, len(lst), 2):
        total += lst[i]
    return total


my_list = [1, 2, 3, 4, 5]
result = sum_even_position(my_list)
print(result)  # 6


my_list = [1, 2, 3, 4, 5]
result = sum_even_position(my_list)
print(result)  # 6


def find_duplicate(arr):
    xor_result = 0

    # XOR of all elements in the array
    for num in arr:
        xor_result ^= num

    # XOR of numbers from 0 to (N-2)
    for i in range(len(arr) - 1):
        xor_result ^= i

    return xor_result


# Example usage
arr = [0, 1, 2, 3, 1]  # N = 5
duplicate_number = find_duplicate(arr)
print("Duplicate number:", duplicate_number)


# given a string s find the length of the longest substring without repeating characters
# sliding window problem
def length_of_longest_substring(s):
    """
    Finds the length of the longest substring in a string without repeating characters.

    Args:
        s: The string to search.

    Returns:
        The length of the longest substring without repeating characters.
    """
    used = {}
    max_length = 0
    start = 0

    for i, char in enumerate(s):
        # If the character is already in used and within the current window
        if char in used and used[char] >= start:
            # Shift the starting index to avoid duplicates
            start = used[char] + 1
        else:
            # Update the max_length if the current window is longer
            max_length = max(max_length, i - start + 1)
        # Update the used dictionary
        used[char] = i

    return max_length


# Example usage
string = "abcabcbb"
length = length_of_longest_substring(string)
print(f"The length of the longest substring without repeating characters in '{string}' is: {length}")
