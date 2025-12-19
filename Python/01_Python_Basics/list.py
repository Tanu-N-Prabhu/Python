def list():
    List = ["Tanu", "Nanda", "Prabhu"]
    print(List)

def byIndex():
    List = ["Tanu", "Nanda", "Prabhu"]
    Index = List[2]
    print(Index)

def appending():
    adder = [1, 2, 3, 4]
    adder.append(5)
    print(adder)

def slicing():
    slice = [1, 2, 3, 4, 5]
    slice1 = slice[:2]
    print(slice1)

def index():
    index = [1, 2, 3, 4, 5]
    index1 = index.index(3)
    print(index1)

def insert():
    insert = ["Tanu", "Nanda"]
    insert.insert(2, "Prabhu")
    print(insert)

def remove():
    remove = ["Daimler", "Mercedes", "Benz"]
    remove.remove("Daimler")
    print(remove)

def pop():
    popped = ["BMW", "Mercedes", "Mini"]
    pop1 = popped.pop(2)
    print(pop1)

option = int(input("Enter the option such as 1, 2, 3, 4, 5, 6, 7, 8"))

if option == 1:
    list()
elif option == 2:
    byIndex()
elif option == 3:
    appending()
elif option == 4:
    slicing()
elif option == 5:
    index()
elif option == 6:
    insert()
elif option == 7:
    remove()
elif option == 8:
    pop()
else:
    print("You have entered invalid option !!!!")



