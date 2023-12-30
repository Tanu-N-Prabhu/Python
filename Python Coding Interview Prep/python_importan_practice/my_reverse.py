name = "dhiraj"
n = list(name)
l = len(n)
s = []
r = []

# easiest with slicing
print(n[::-1])

# by calling from end
for i in range((l - 1), -1, -1):
    r.append(n[i])
print(r)

# by stack operations
for i in n:
    s.append(i)

r = []
while len(s) > 0:
    r.append(s.pop())
print(r)

count_seconds = 5
for i in reversed(range(count_seconds + 1)):
    print(i)


def reverse_join_reversed_iter(string):
    s1 = ''.join(reversed(string))
    return s1


reverse_join_reversed_iter(name)


# This program will reverse the string that is passed by iterable object
# to it from the main function
class Reverse:
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        # initialize the iterable
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index -= 1
        return self.data[self.index]

    def main():
        rev = Reverse('Drapsicle')
        for char in rev:
            print(char)

    if __name__ == '__main__':
        main()


# A Python program to demonstrate working of Generators
def reverse_gen(data):
    # this is like counting from 100 to 1 by taking one(-1)
    # step backward.
    for index in range(len(data)-1, -1, -1):
        yield data[index]

    def main():
        rev = reverse_gen('Harssh')
        for char in rev:
            print(char)
        data ='dhiraj'
        print(list(data[i] for i in range(len(data)-1, -1, -1)))

    if __name__ == "__main__":
        main()
