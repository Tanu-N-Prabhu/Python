class ArrayList:
    def __init__(self, number_list):
        self.numbers = number_list

    def __iter__(self):
        # initialize 
        self.pos = 0
        return self

    def __next__(self):
        # next iteration value
        if(self.pos < len(self.numbers)):
            self.pos += 1
            return self.numbers[self.pos - 1]
        else:
            raise StopIteration

array_obj = ArrayList([1, 2, 3])

it = iter(array_obj)

print(next(it)) #output: 2
print(next(it)) #output: 3

print(next(it))
#Throws Exception
#Traceback (most recent call last):
#...
#StopIteration