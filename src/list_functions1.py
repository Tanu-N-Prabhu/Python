# Passing the entire list as a parameter to the function
list1 = [1, 2, 3, 4, 5, 6]

def func1(l1):
    for item1 in list1:
        print(item1)

func1(list1)

# Generating the list using a range function

# range (stop)
list2 = range(5)
print(list2)

# range (start, stop)
list3 = range(1, 10)
print(list3)

#range (start, step, stop)
list4 = range(2, 10, 20)
print(list4)

# range function are innutable, they cannot be modified

# Using range function in a for loop

list5 = [1, 3, 5, 7]

def fun2(l2):
    for item3 in range(0, 4):
        print(l2[item3])

fun2(list5)

# Modifying the list using the range function

list6 = [1, 2, 3, 4, 5]

def modify(list):
    for item4 in range(0, 5):
        list[item4] = list[item4] + 5
        print(list[item4])

modify(list6)

# Passing multiple lists into the function

list7 = [1, 2, 3]
list8 = [4, 5, 6]

def multiple(a, b):
    print(a, b)

multiple(list7, list8 )

# Iterating through a list of list using a function

listoflist = [[1, 2, 3], [4, 5, 6]]

def makeOneList (a):
    bothLists = []
    for item in a:
        for element in item:
            bothLists.append(element)
    print(bothLists)

makeOneList(listoflist)