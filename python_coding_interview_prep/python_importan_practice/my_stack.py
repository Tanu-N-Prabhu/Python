class mystack:
    
    def __init__(self):
        self.data =[]
        
    def length(self): #length of the list
        return len(self.data)
    
    def is_full(self): #check if the list is full or not
        if len(self.data) == 5:
            return True
        else:
            return False
        
    def push(self, element):# insert a new element
        if len(self.data) < 5:
            self.data.append(element)
        else:
            return "overflow"
        
    def pop(self): # # remove the last element from a list
        if len(self.data) == 0:
            return "underflow"
        else:
            return self.data.pop()

a = mystack() # I create my object
a.push(10) # insert the  element
a.push(23)
a.push(25)
a.push(27)
a.push(11)
print(a.length())
print(a.is_full())
print(a.data)
print(a.push(31)) # we try to insert one more element in the list - the output will be overflow
print(a.pop())
print(a.pop())
print(a.pop())
print(a.pop())
print(a.pop())
print(a.pop()) # try to delete an element in a list without elements - the output will be underflow
 