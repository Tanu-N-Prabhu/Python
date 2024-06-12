import operator
# defaultdict
from collections import defaultdict, Counter


# Function to return a default values for keys that is not present
def def_value():
    return "Not Present"
    
# Defining the defaultdict which never fail and return with default value
d = defaultdict(def_value)
d["a"] = 1
d["b"] = 2

print(d["a"])
print(d["b"])
print(d["c"])
# Not Present


phonebook = {"John": 938477566, "Jack": 938377264, "Jill": 947662781}
print(phonebook)
phonebook["Dhiraj"] = 7893493052
print(phonebook)

for name, number in phonebook.items():
    print("Phone number of %s is %d" % (name, number))

# delete item and no return value
del phonebook["John"]
print(phonebook)
# return the value and then delete
nam = phonebook.pop("Dhiraj")
print(nam)
print(phonebook)

# sorting a dictionary by value
xs = {'b': 3, 'a': 4, 'c': 2, 'd': 1}
print(sorted(xs.items(), key=lambda x: x[1]))
print(sorted(xs.items(), key=lambda x: x[1], reverse=True))
# by key
print(sorted(xs.items(), key=lambda x: x[0]))

xs = [{'b': 3, 'a': 4, 'c': 2, 'd': 1},
      {'d': 2, 'a': 4, 'c': 1, 'b': 5}]
print(list(
    map(lambda x: list(sorted(x.items(), key=lambda x: x[1])), (x for x in xs))))

name_for_userid = {
    382: "Alice",
    590: "Bob",
    951: "Dilbert",
}

dict = {}
dict['1'] = 'apple'
dict['3'] = 'orange'
dict['2'] = 'pango'

lst = dict.keys()

# Sorted by key
print("Sorted by key: ", sorted(lst))

lst = dict.values()

# sorted by values
print("Sorted by values: ", sorted(lst))

# Function argument unpacking
def myfunc(x, y, z):
    print(x, y, z)

tuple_vec = (1, 0, 1)
dict_vec = {'x': 1, 'y': 0, 'z': 1}

# args and kargs
myfunc(*tuple_vec)
myfunc(**dict_vec)

# used get function of dict
def greeting(userid):
    return "Hi %s!" % name_for_userid.get(userid, "there")

greeting(382)
greeting(333333)

rollNumbers =[122,233,353,456]
names = ['alex','bob','can', 'don'] 
NewDictionary={ i:j for (i,j) in zip (rollNumbers,names)}
print(NewDictionary)

# difference between set and dictionary
myset = {0, 'apple', 3.5}
mydictionary = {'0': 'first', 'apple': 'second', '3.5': 'third'}

# using naive method to get count of each element in string
test_str = "GeeksforGeeks"
all_freq = {}

for i in test_str:
    if i in all_freq:
        all_freq[i] += 1
    else:
        all_freq[i] = 1

# printing result
print ("Count of all characters in GeeksforGeeks is :\n "
                                        + str(all_freq))
#Count of all characters in GeeksforGeeks is :
# {'r': 1, 'e': 4, 'k': 2, 'G': 2, 's': 2, 'f': 1, 'o': 1}


d1 = {'key1': 50, 'key2': 100, 'key3':200}
d2 = {'key1': 200, 'key2': 100, 'key4':300}
new_dict = Counter(d1) + Counter(d2)
print(new_dict)
# Counter({'key4': 300, 'key1': 250, 'key2': 200, 'key3': 200})

# merging two dict
d1.update(d2)
