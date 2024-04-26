"""
Sets are lists with no duplicate entries
"""
print(set("my name is Eric and Eric is my name".split()))
# {'name', 'and', 'Eric', 'is', 'my'}
a = set(["Jake", "John", "Eric"])
b = set(["John", "Jill"])
print(a)
print("a intersection b: " + str(a.intersection(b)))
print("a symmeteric diff b: " + str(a.symmetric_difference(b)))
print("a diff b: " + str(a.difference(b)))
print("a union b: " + str(a.union(b)))
print("b diff a: " + str(b.difference(a)))

# count the each element
days = ['S','M','M','M','F','S']
y = set(days)
# {'F', 'S', 'M'}
print([[x,days.count(x)] for x in y])
#[['M', 3], ['S', 2], ['F', 1]]
