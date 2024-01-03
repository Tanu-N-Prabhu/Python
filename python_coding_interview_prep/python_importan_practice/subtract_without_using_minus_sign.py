def subtract_nums(num1, num2):
    # Loop until there is no borrow left (num2 becomes 0)
    while num2 != 0:
        # Perform bitwise NOT to find the bits that need to borrow
        borrow = (~num1) & num2

        # Perform bitwise XOR to subtract bits without considering borrow
        num1 = num1 ^ num2

        # Left shift the borrow to the next bit
        num2 = borrow << 1

    # Return the final result after subtraction
    return num1


# Example usage
print(subtract_nums(195, 7))
