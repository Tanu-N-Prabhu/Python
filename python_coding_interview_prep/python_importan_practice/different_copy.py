from copy import copy, deepcopy

# Using '=' operator
x = [1, 2, 3]
y = x
x[0] = 5    # value of 'y' also changes as it is the SAME object
x[1] = 15
print "Shallow copy: ", y

# Using copy.deepcopy()
a = [10, 20, 30]
b = deepcopy(a)
a[1] = 70   # value of 'b' does NOT change because it is ANOTHER object
print "Deep copy: ", b


list_1 = [1, 2, [3, 5], 4]

## shallow copy
list_2 = copy(list_1) 
list_2[3] = 7
list_2[2].append(6)

list_2    # output => [1, 2, [3, 5, 6], 7]
list_1    # output => [1, 2, [3, 5, 6], 4]

## deep copy
list_3 = deepcopy(list_1)
list_3[3] = 8
list_3[2].append(7)

list_3    # output => [1, 2, [3, 5, 6, 7], 8]
list_1    # output => [1, 2, [3, 5, 6], 4]