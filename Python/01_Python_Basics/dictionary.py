name = {1: "Tanu", 2: "Nanda", 3: "Prabhu"}

print(name[1])
print(name[2])
print(name[3])
print(name)

# Creating the new Dictinoary from an empty dictionary

name1 = {}
name1[1] = "Mercedes"
name1[2] = "Benz"

print(name1)

# Calculating the length of the dictionary name1 can be done by
length = len(name1)
print(length)


# Reassigning the key of the dictionary

name[2] = "N"
print(name)

# Removing the key valur pair using a del:

name2 = {1: "Newton", 2: "Einstein", 3: "Tanu"}
del name2[3]

print(name2)
