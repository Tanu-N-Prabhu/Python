"""Yield are used in Python generators. A generator function is defined like a normal function, but whenever it needs
to generate a value, it does so with the yield keyword rather than return. If the body of a def contains yield,
the function automatically becomes a generator function. """
import types


# fill in this function
def fib():
    current, next = 0, 1
    while True:
        current, next = next, current + next
        yield current        


# testing code
if isinstance(fib(), types.GeneratorType):
    print("Good, The fib function is a generator.")

    counter = 0
    for n in fib():
        print(n)
        counter += 1
        if counter == 5:
            break
