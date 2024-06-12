from functools import reduce


# map
my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [1, 2, 3, 4, 5]

results = list(map(lambda x, y: (x, y), my_strings, my_numbers))
# same result can achieve with  [(x,y) for x,y in zip(my_strings,my_numbers)]

print(results)

pos_check_numbers = ['534', '7766', '8533']
pos_check_numbers = ','.join(map(str, pos_check_numbers)) 
print(pos_check_numbers)

circle_areas = [3.56773, 5.57668, 4.00914, 56.24241, 9.01344, 32.00013]

result = list(map(round, circle_areas, range(1,7)))

print(result)

# filter
scores = [66, 90, 68, 59, 76, 60, 88, 74, 81, 65]


def is_a_student(score):
    return score > 75


over_75 = list(filter(is_a_student, scores))

print(over_75)

dromes = ("demigod", "rewire", "madam", "freer", "anutforajaroftuna", "kiosk")

palindromes = list(filter(lambda word: word == word[::-1], dromes))

print(palindromes)

# reduce works as cumulatively
numbers = [3, 4, 6, 9, 34, 12]


def custom_sum(first, second):
    return first + second


result = reduce(custom_sum, numbers)
print(result)

# factorial by reduce
n = 6
result = reduce(lambda x, y: x*y, range(1, n+1))
print(result)
