"""
Implement a function that adds two numbers together and returns their sum in binary.
The conversion can be done before, or after the addition.

The binary number returned should be a string.

Examples:(Input1, Input2 --> Output (explanation)))

1, 1 --> "10" (1 + 1 = 2 in decimal or 10 in binary)
5, 9 --> "1110" (5 + 9 = 14 in decimal or 1110 in binary)
"""


def add_binary(a,b):
    # calculate the sum
    decimal_sum = a + b

    # convert the sum to binary
    binary_sum = bin(decimal_sum)[2:]

    return binary_sum


# Test cases
result1 = add_binary(1, 1)
print(result1)  # Should print 7 (110 + 101 = 7 in decimal)

result2 = add_binary(0, 1)
print(result2)  # Should print 15 (1111 + 10 = 15 in decimal)

result3 = add_binary(1, 0)
print(result3)

# also possible witout using bin() function
dec = 10
binary = ""

while dec > 0:
    binary = str(dec % 2) + binary
    dec = dec // 2

print(binary)

