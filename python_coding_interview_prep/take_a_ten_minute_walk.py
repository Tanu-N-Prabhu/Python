"""
You live in the city of Cartesia where all roads are laid out in a perfect grid.
You arrived ten minutes too early to an appointment, so you decided to take the opportunity to
go for a short walk. The city provides its citizens with a Walk Generating App on their phones --
everytime you press the button it sends you an array of one-letter strings representing directions
to walk (eg. ['n', 's', 'w', 'e']). You always walk only a single block for each letter (direction)
and you know it takes you one minute to traverse one city block, so create a function that will
return true if the walk the app gives you will take you exactly ten minutes (you don't want to be
early or late!) and will, of course, return you to your starting point. Return false otherwise.

Note: you will always receive a valid array containing a random assortment of direction letters
('n', 's', 'e', or 'w' only). It will never give you an empty array (that's not a walk, that's
standing still!).
"""


def is_valid_walk(walk):
    # Check if the walk has exactly 10 elements
    if len(walk) == 10:
        # Use the count function to count occurrences of each direction
        count_n = walk.count('n')
        count_s = walk.count('s')
        count_e = walk.count('e')
        count_w = walk.count('w')

        # Check if the total north-south and east-west distances are zero
        return count_n == count_s and count_e == count_w

    return False


# Example usage:
walk1 = ['n', 's', 'n', 's', 'n', 's', 'n', 's', 'n', 's']
walk2 = ['n', 's', 'e', 'w', 'n', 's', 'e', 'w', 'n', 's']
walk3 = ['n', 's', 'e', 'w', 'n', 's', 'e', 'w', 'n', 'w']

print(is_valid_walk(walk1))  # Output: True
print(is_valid_walk(walk2))  # Output: True
print(is_valid_walk(walk3))  # Output: False
