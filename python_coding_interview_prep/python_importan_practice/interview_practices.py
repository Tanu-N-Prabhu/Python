
import os
import time

l1 = []
l2 = []
l3 = []
s1 = []
s2 = []


def get_missing_number(lst):
    # return [x for x in range(1, lst[-1]) if x not in lst]
    return set(range(lst[-1])[1:]) - set(lst)


l = list(range(1, 100))
l.remove(50)

print(set(range(l[-1])[1:]))
print('=' * 100)
print(set(l))
print(get_missing_number(l))


def find_duplicates(elements):
    # return [x for x in elements if elements.count(x) > 1]
    duplicates, seen = set(), set()
    for element in elements:
        if element in seen:
            duplicates.add(element)
        seen.add(element)
#         print('seen: {}'.format(seen))
#         print('duplicates: {}'.format(duplicates))
#         print('-' * 50)
    return list(duplicates)


l = [20, 30, 40, 20, 50, 30]
print(find_duplicates(l))


def intersect(lst1, lst2):
    # return [x for x in lst1 if x in lst2]
    res, lst2_copy = [], lst2[:]
    for el in lst1:
        if el in lst2_copy:
            res.append(el)
            lst2_copy.remove(el)
    return res


l1 = [20, 30, 40, 20, 50, 30]
l2 = [70, 80, 40, 90, 50, 100]
print(intersect(l1, l2))


def is_anagram(s1: str, s2: str) -> bool:
    # return sorted(s1) == sorted(s2)
    if len(s1) != len(s2):
        return False
    return set(s1) == set(s2)


print(is_anagram("elvies", "lives"))


print(max(l1))
print(min(l1))


# remove all duplicates
lst = list(range(10)) + list(range(10))
print(lst)
lst = list(set(lst))
print(lst)


def reverse(str):
    # return str[::-1]
    if len(str) <= 1:
        return str
    return reverse(str[1:]) + str[0]


print(reverse("hello"))


houses = ["Eric's house", "Kenny's house",
          "Kyle's house", "Stan's house", "Dhiraj's house"]

# Each function call represents an elf doing his work


def deliver_presents_recursively(houses):
    # Worker elf doing his work
    if len(houses) == 1:
        house = houses[0]
        print("Delivering presents to", house)

    # Manager elf doing his work
    else:
        mid = len(houses) // 2
        first_half = houses[:mid]
        second_half = houses[mid:]

        # Divides his work among two elves
        deliver_presents_recursively(first_half)
        deliver_presents_recursively(second_half)


print(deliver_presents_recursively(houses))


# Find pairs of integers in list so that their sum is equal to integer x
def find_pairs(l, x):
    pairs = []
    for (i, el1) in enumerate(l):
        for (j, el2) in enumerate(l[(i+1):]):
            if el1 + el2 == x:
                pairs.append((el1, el2))
    return pairs


print(l1)
tic = time.perf_counter()
print(find_pairs(l1, 50))
toc = time.perf_counter()
print(toc - tic)


# Compute the first n Fibonacci numbers
def cal_fibinacci(n):
    a, b = 0, 1
    fib = []
    for i in range(n):
        fib.append(b)
        a, b = b, (a + b)
    return fib


print(cal_fibinacci(10))

# one line fibonacci
lambda x: x if x <= 1 else fib(x-1) + fib(x+1)


def is_palindrome(phrase):
    return phrase == phrase[::-1]


print(is_palindrome("madam"))


def qsort(l):
    if l == []:
        return []
    return qsort([x for x in l[1:] if x < l[0]]) + l[0:1] + qsort([x for x in l[1:] if x >= l[0]])


print(l1)
print(qsort(l1))


# as a list ...
l = [3, 4]
l += [5, 6]
print(l)

# ... as a stack ...
l.append(10)
l.extend([9, 7])
l.pop()
print(l)

# ... and as a queue
l.insert(0, 5)
l.pop()
print(l)


def get_permutations(w):
    if len(w) <= 1:
        return set(w)
    smaller = get_permutations(w[1:])
    perms = set()
    for x in smaller:
        for pos in range(0, len(x) + 1):
            perm = x[:pos] + w[0] + x[pos:]
            perms.add(perm)
    return perms


print(get_permutations("nan"))


s1 = ['red', 'green', 'blue']
list(map(lambda x: x[0], s1))


list(map(lambda x, y: str(x) + y, [4, 1, 3], s1))


' is '.join(['this', 'good'])


list(filter(lambda x: True if x > 10 else False, [1, 15, 9, 20]))


print('   good '.strip())


sorted(l1)


sorted(l1, key=lambda x: 0 if x == 50 else x)


# zip or groups by one of each list
print(l1)
print(l2)
l3 = list(zip(l1, l2))
print(l3)


# ungrouping
list(zip(*l3))


list(enumerate(s1))


a, b = 'jane', 'alice'
print(a)
print(b)
a, b = b, a
print(a)
print(b)


def f(x, y, z):
    return x + y * z


print(f(*[1, 3, 4]))
f(**{'z': 4, 'x': 1, 'y': 3})


a, *b = l1
print(a)
print(b)


x = {'alice': 18}
y = {'bob': 27, 'ann': 22}
z = {**x, **y}
print(z)


l1 = [20, 40, 30]
l1.append(30)
print(l1)
l1.insert(2, 60)
print(l1)
l1 + [30]
print(l1)
l1.remove(60)
print(l1)
l1.reverse()
print(l1)
l1.sort()
print(l1)
l1.index(30)
l1.index(30, 1)


stack = [3]
stack.append(5)
print(stack)
stack.pop()


basket = {'apple', 'banana', 'mango'}
print(basket)
same = set(['apple', 'banana', 'mango'])
print(same)
print('mashroom' in basket)
print('apple' in basket)


calories = {'apple': 50, 'banana': 80, 'chocolate': 540}
print(calories)
print(calories['apple'] < calories['banana'])
print('apple' in calories.keys())
print(50 in calories.values())
for k, v in calories.items():
    print(k) if v > 500 else None


# list comprehention
l = [('hi ' + x) for x in ['alice', 'bob', 'zen']]
print(l)
l = [x * y for x in range(3) for y in range(3) if x > y]
print(l)
squares = {x**2 for x in [0, 2, 4] if x < 4}
print(squares)


if None or 0 or 0.0 or '' or [] or {} or set():
    print('dead')
else:
    print('good')


s = "the quick brown fox jumps over the lazy dog"
print(s[1:])
print(s[:-1])
print(s[::-1])
print(s[-3:])
print(s.startswith('the'))
print(s.find('dog'))
print(s.replace('dog', 'wolf'))
print(len(s))
print('fox' in s)


[(lambda x: x * 2)(x) for x in l1]

# ## Iterators, Generators and Decorators


class Counter(object):
    def __init__(self, low, high):
        self.current = low
        self.high = high

    # return itself as as iterator object
    def __iter__(self):
        return self

    # return the next value still the value is less than high
    def __next__(self):
        if self.current > self.high:
            raise StopIteration
        else:
            self.current += 1
        return self.current - 1

    # generator
    def generator(self):
        print("inside my generator")
        yield 'a'
        yield 'b'
        yield 'c'

    # yield
    def counter_generator(self):
        while self.current <= self.high:
            yield self.current
            self.current += 1


# calling
c = Counter(5, 10)
for i in c:
    print(i, end=' ')

c.generator()
for char in c.generator():
    print(char)

c = Counter(1, 5)
for i in c.counter_generator():
    print(i, end=' ')


# clouser adder is a clouser
def add_num(num):
    def adder(number):
        return num + number
    return adder


result = add_num(10)
result = result(20)
print(result)


# decorator
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("before call")
        print(args)
        print(kwargs)
        # changing args
        args = [5, 9]
        result = func(*args, **kwargs)
        print("after call")
        return result
    return wrapper


@my_decorator
def add(a, b):
    print("our add function")
    return a + b


add(1, 3)


# Find the first non-repeating integer in a list
def find_first_unique(lst):
    counts = {}  # Creating a dictionary
    # Initializing dictionary with pairs like (lst[i],(count,order))
    counts = counts.fromkeys(lst, (0, len(lst)))
    order = 0
    for ele in lst:
        # counts[ele][0] += 1  # Incrementing for every repitition
        # counts[ele][1] = order
        counts[ele] = (counts[ele][0]+1, order)
        # increment order
        order += 1
    answer = None
    answer_key = None
    # filter non-repeating with least order
    for ele in lst:
        if (counts[ele][0] == 1) and (answer is None):
            answer = counts[ele]
            answer_key = ele
        elif answer is None:
            continue
        elif (counts[ele][0] == 1) and (counts[ele][1] < answer[1]):
            answer = counts[ele]
            answer_key = ele
    return answer_key


print(find_first_unique([1, 1, 1, 2]))


def f(*args, **kwargs):
    print(args)
    print(kwargs)


f(1, 2, 3)
#(1, 2, 3)
# {}


# list
doubles = [2 * n for n in range(50)]
# generator / iterator
doubles = (2 * n for n in range(50))


def print_name_with_prefix(prefix):
    print(f"Searching prefix:{prefix}")
    while True:
        name = (yield)
        if prefix in name:
            print(name)


# generator
x = print_name_with_prefix("hello")


# ciser encryption of a text and shift key
def encrypt(text, key):

    encrypted_text = ''

    # Fill in the blanks to create an encrypted text
    for char in text.lower():
        idx = (alphabet.index(char) + key) % len(alphabet)
        encrypted_text = encrypted_text + alphabet[idx]

    return encrypted_text


# Check the encryption function with the shift equals to 10
alphabet = 'abcdefghijklmnopqrstuvwxyz'
print(encrypt("datacamp", 10))


# Create a word list from the string stored in text
text = 'StRing ObJeCts haVe mANy inTEResting pROPerTies'
text_split = text.split()
word_list = list()
for word in text_split:
    if text_split.index(word) % 2 != 0:
        word = word.upper()
    else:
        word = word.lower()
    word_list.append(word)

word_list = ' '.join(word_list)

# change all files name in a directory
# Python program to rename all file
# names in your directory

os.chdir('./')
print(os.getcwd())

for count, f in enumerate(os.listdir()):
    f_name, f_ext = os.path.splitext(f)
    f_name = "geek" + str(count)
    print(f_name)
    # new_name = f'{f_name}{f_ext}'
    # os.rename(f, new_name)


def reversing(n):
    reverse = 0
    while n != 0:
        reverse = reverse * 10 + n % 10
        n = n // 10
    return reverse


n = 465
print(reversing(n))


# A function to print all prime factors of
# a given number n
def primeFactors(n):
    import math

    # Print the number of two's that divide n
    while n % 2 == 0:
        print(n)
        n = n / 2

    # n must be odd at this point
    # so a skip of 2 ( i = i + 2) can be used
    for i in range(3, int(math.sqrt(n))+1, 2):

        # while i divides n , print i and divide n
        while n % i == 0:
            print(i)
            n = n / i

    # Condition if n is a prime
    # number greater than 2
    if n > 2:
        print(n)


# Driver Program to test above function
n = 315
primeFactors(n)


"""
Write a function to swap a number in place (that is, without temporary variables) .
"""


def swap_numbers(pair_ab):
    if not len(pair_ab) == 2:
        return
    # assume a = 9; b = 5
    pair_ab[0] = pair_ab[1] - pair_ab[0]  # a = -4; b = 5
    pair_ab[1] = pair_ab[1] - pair_ab[0]  # a = -4; b = 9
    pair_ab[0] = pair_ab[1] + pair_ab[0]  # a = 5; b = 9


a = 9
b = 5
pair = [a, b]
swap_numbers(pair)

"""

"""


def plusOne(A):
    num_string = ''.join(str(i) for i in A)
    num = int(num_string)
    num = num + 1
    num = str(num)
    final_arr = list(num)
    return (final_arr)


l = [25, 30, 40, 50]
plusOne(l)
# ['2', '5', '3', '0', '4', '0', '5', '1']

# Traversing from one point to another point
# storing the minimum number of steps


def traversal_steps(A, B):
    points = list(zip(A, B))
    minSteps = 0
    for p in range(len(points)-1):
        # taking the manhattan distance between x and y-coordinates
        d1 = abs(points[p][0] - points[p+1][0])
        d2 = abs(points[p][1] - points[p+1][1])
        # adding the maximum among the two to the running steps parameter
        minSteps += max(d1, d2)
    return (minSteps)


A = [2, 5, 7, 9]
B = [6, 5, 4, 3]
print(traversal_steps(A, B))

"""
find the consecutive number starting and ending position
of a sorted array with binary search
input: 
arr = [2,4,5,5,5,5,5,7.9,9]
target = 5
output: [2,6]
T(n) = O(log n)
S(n) = O(1)
"""


def find_start(arr, target):
    if arr[0] == target:
        return 0
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        # if mid == start of the sequences
        # means left side of mid < target
        if arr[mid] == target and arr[mid - 1] < target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


def find_end(arr: list, target: int) -> int:
    if arr[-1] == target:
        return len(arr) - 1
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        # means mid is target
        # then right side is greated that target value
        if arr[mid] == target and arr[mid + 1] > target:
            return mid
        elif arr[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return -1


def first_and_last(arr: list, target: int) -> list:
    if len(arr) == 0
    or arr[0] > target
    or arr[-1] < target:
        return [-1, -1]
    start = find_start(arr, target)
    end = find_end(arr, target)
    return [start, end]


arr = [2, 4, 5, 5, 5, 5, 5, 7.9, 9]
target = 5
print(first_and_last(arr, target))


def longestConsecutive(nums: List[int]) -> int:
    numSet = set(nums)
    longest = 0

    for n in nums:
        # check if its the start of a sequence
        if (n - 1) not in numSet:
            length = 1
            while (n + length) in numSet:
                length += 1
            longest = max(length, longest)
    return longest


"""
Top k frequent elements in a list of string
O(n)
"""


def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    count = {}
    freq = [[] for i in range(len(nums) + 1)]

    for n in nums:
        count[n] = 1 + count.get(n, 0)
    for n, c in count.items():
        freq[c].append(n)

    res = []
    for i in range(len(freq) - 1, 0, -1):
        for n in freq[i]:
            res.append(n)
            if len(res) == k:
                return res


"""
Trapping rain water
"""


def trap(self, height: List[int]) -> int:
    if not height:
        return 0

    l, r = 0, len(height) - 1
    leftMax, rightMax = height[l], height[r]
    res = 0
    while l < r:
        if leftMax < rightMax:
            l += 1
            leftMax = max(leftMax, height[l])
            res += leftMax - height[l]
        else:
            r -= 1
            rightMax = max(rightMax, height[r])
            res += rightMax - height[r]
    return res


def multi_word_search(doc_list, keywords):
    """
    Takes list of documents (each document is a string) and a list of keywords.  
    Returns a dictionary where each key is a keyword, and the value is a list of indices
    (from doc_list) of the documents containing that keyword

    >>> doc_list = ["The Learn Python Challenge Casino.", "They bought a car and a casino", "Casinoville"]
    >>> keywords = ['casino', 'they']
    >>> multi_word_search(doc_list, keywords)
    {'casino': [0, 1], 'they': [1]}
    """
    import re
    if len(keywords) == 0:
        return {}
    words = []
    result_list = {}
    keywords = [key.lower() for key in keywords]
    print(keywords)
    for key in keywords:
        if key not in result_list.keys():
            result_list[key] = []
    i = 0

    for d in doc_list:
        words = d.split(' ')
        words = [re.sub("[ ;:,.]", "", word) for word in words]
        for word in words:
            if word.lower() in keywords:
                result_list[word.lower()].append(i)
        i += 1
    return result_list


def is_valid_zip(zip_code):
    """Returns whether the input string is a valid (5 digit) zip code
    """
    try:
        if zip_code == '00000':
            zip_code = 11111
        else:
            zip_code = int(zip_code)
        c = 0
        while zip_code != 0:
            zip_code //= 10
            c += 1
        if c == 5:
            return True

    except ValueError:
        print(f'invalid literal for int() with base 10: {zip_code}')
    except TypeError:
        print(f'invalid literal for int() with base 10: {zip_code}')
    return False


# sort binary array in place
def sort_binary_digits(arr):
    left, right = 0, len(arr) - 1

    while left < right:
        if arr[left] == 1 and arr[right] == 0:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
        if arr[left] == 0:
            left += 1
        if arr[right] == 1:
            right -= 1

# Example usage:
binary_digits = [0, 1, 1, 0, 1, 0, 0, 1]
sort_binary_digits(binary_digits)
print(binary_digits)  # Output: [0, 0, 0, 0, 1, 1, 1, 1]
