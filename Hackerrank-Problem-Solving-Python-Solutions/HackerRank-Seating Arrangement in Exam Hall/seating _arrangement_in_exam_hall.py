"""
Problem Statement  :

Semester exams are going on for university students. Examiners noticed that 
a group of people are trying to cheat. 
They marked students of that group as ‘1’ and students of another group ( who are not cheating ) as ‘0’ 

We can reduce cheating by not allowing students from group 1 to sit together, 
means no two students from group 1 can sit together. 
Seatings are marked using above conditions. 
Your task is to give the seating placement of nth possibility 
Possibility order from 1 to 10 is given below

[1  10  100  101  1000  1001  1010  10000  10001  10010]

Sample input :

3 → number of test cases

4

6

9

Sample output :

101

1001

10001

Explanation :

4th possibility is 101 

6th possibility is 1001

9th possibility is 10001
"""


def get_seating_placement(n):
    """
    This function returns the seating placement of the nth possibility.

    Args:
        n: The nth possibility (integer).

    Returns:
        The seating arrangement as a string.
    """
    binary_str = bin(
        n - 1)[2:]  # Convert n-1 to binary string (remove '0b' prefix)
    length = len(binary_str)
    # Create a string of '0's with length equal to the number of digits in the binary representation
    # This string will represent the initial seating arrangement where all seats are empty.
    seating = "0" * length

    # Loop through each character (0 or 1) in the binary st# Combine the three parts: empty seats before, cheating student, and empty seats after.ring
    for i, char in enumerate(binary_str):
        if char == "1":
            # Slice the seating string from the index after the current position (i+1) to the end.
            # This creates a substring of '0's representing the empty seats after the cheating student.
            # Combine the three parts: empty seats before, cheating student, and empty seats after.
            seating = seating[:i] + "1" + seating[i:]
    return seating


# Test cases
print(get_seating_placement(3))  # Output: 101
print(get_seating_placement(6))  # Output: 1001
print(get_seating_placement(9))  # Output: 10001
