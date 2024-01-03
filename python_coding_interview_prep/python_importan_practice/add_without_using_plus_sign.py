"""
Bitwise AND is a binary operation that operates on each pair of corresponding bits of its operands. The result of the AND operation is 1 only if both bits are 1; otherwise, the result is 0.

Here's a quick overview of how bitwise AND works at the binary level:

- 0 & 0 = 0: If both bits are 0, the result is 0.
- 0 & 1 = 0: If one of the bits is 0, the result is 0.
- 1 & 0 = 0: If one of the bits is 0, the result is 0.
- 1 & 1 = 1: If both bits are 1, the result is 1.

Let's take an example:

```python
num1 = 9    # binary: 1001
num2 = 14   # binary: 1110

result = num1 & num2
```

In this case:

```
   1001  (num1)
 & 1110  (num2)
 --------
   1000  (result)
```

The bitwise AND operation compares each pair of corresponding bits (from right to left), and the result is 1 only where both bits are 1. In this example, only the rightmost bit has a 1 in both `num1` and `num2`, so the result is `1000`, which is 8 in decimal.

So, in the context of the provided code:

```python
data = num1 & num2
```

Certainly! Let's discuss the bitwise XOR (`^`) and left shift (`<<`) operations:

### Bitwise XOR (`^`):
Bitwise XOR is a binary operation that results in a 1 when the corresponding bits of the operands are different, and 0 when they are the same. The truth table for XOR is as follows:

- 0 ^ 0 = 0
- 0 ^ 1 = 1
- 1 ^ 0 = 1
- 1 ^ 1 = 0

In the context of binary addition, XOR is used to add the bits of the operands without considering the carry. It's a bit-wise addition operation where the result is 1 only if the bits are different.

Example:
```python
num1 = 9    # binary: 1001
num2 = 14   # binary: 1110

result = num1 ^ num2
```

```
   1001  (num1)
 ^ 1110  (num2)
 --------
   0111  (result)
```

The result (`0111`) represents the bits that need to be added without considering the carry.

### Bitwise Left Shift (`<<`):
The left shift operator (`<<`) shifts the bits of a binary number to the left by a specified number of positions. In the context of binary addition, left shift is used to carry the result of addition to the next higher bit.

Example:
```python
data = 1
data = data << 1
```

In this case, `data` initially holds the value `1` (binary: `0001`). After the left shift by one position (`<< 1`), the value becomes `2` (binary: `0010`). The left shift essentially multiplies the number by 2.

In the provided code:
```python
num2 = data << 1
```
This line left-shifts the value of `data` (which may represent a carry) by one position, preparing it to be added to the next bit during the next iteration of the loop.

These bitwise operations play a crucial role in binary addition and manipulation of individual bits.
"""


# Main Comment: Binary Addition Using Bitwise Operations
def add_nums(num1, num2):
    # Loop until there is no carry left (num2 becomes 0)
    while num2 != 0:
        # Perform bitwise AND to find the common set bits
        data = num1 & num2

        # Perform bitwise XOR to add bits without considering carry
        num1 = num1 ^ num2

        # Left shift the carry to the next bit
        num2 = data << 1

    # Return the final result after addition
    return num1


print(add_nums(195, 7))
