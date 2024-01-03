"""
A square of squares
You like building blocks. You especially like building blocks that are squares.
And what you even like more, is to arrange them into a square of square building blocks!

However, sometimes, you can't arrange them into a square. Instead, you end up with an ordinary
rectangle! Those blasted things! If you just had a way to know, whether you're currently working
in vain… Wait! That's it! You just have to check if your number of building blocks is a perfect square.

Task
Given an integral number, determine if it's a square number:

In mathematics, a square number or perfect square is an integer that is the square of an integer;
in other words, it is the product of some integer with itself.

The tests will always use some integral number, so don't worry about that in dynamic typed languages.

Examples
-1  =>  false
 0  =>  true
 3  =>  false
 4  =>  true
25  =>  true
26  =>  false
"""


def is_square(n):
    # Check if the number is negative
    if n < 0:
        return False

    # Calculate the square root of the number
    square_root = int(n ** 0.5)

    # Check if the square of the square root is equal to the original number
    return square_root ** 2 == n


# Test cases
print(is_square(-1))  # Should print False
print(is_square(0))   # Should print True
print(is_square(3))   # Should print False
print(is_square(4))   # Should print True
print(is_square(25))  # Should print True
print(is_square(26))  # Should print False
