# passing a list as a parameter to a function
list = ["Tanu", "Nanda", "Prabhu"]

def call_list(li):
    return  li

print(call_list(list))
print(call_list(list[2]))

# Accessing an element in a list using a function

list2 = [1, 2, 3, 4, 5]

def listing(li1):
    return li1

print(listing(list2[1]))

# Modifing a list value in a function

list3 = [4, 3, 2, 1, 0]

def modify(l1):
    return l1[1]+1

print(modify(list3))

# Manipulating the list using the functions

list4 = [1, 1, 3, 8]

def list_manip(li):
    li.remove(3)
    li.insert(2,4)
    return li

print(list_manip(list4))