"""
Create a function taking a positive integer between 1 and 3999 (both included) as its parameter and
returning a string containing the Roman Numeral representation of that integer.

Modern Roman numerals are written by expressing each digit separately starting with the left most
digit and skipping any digit with a value of zero.
In Roman numerals 1990 is rendered: 1000=M, 900=CM, 90=XC; resulting in MCMXC.
2008 is written as 2000=MM, 8=VIII; or MMVIII. 1666 uses each Roman symbol in
descending order: MDCLXVI.
"""


def int_to_roman(num):
    # Define the values and symbols for Roman numerals
    val = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    syb = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]

    # Initialize an empty string to store the Roman numeral
    roman_num = ''

    # Initialize an index to iterate through the values and symbols
    i = 0

    # Continue the loop until the original number becomes zero
    while num > 0:
        # Append the corresponding symbol to the result string
        # and subtract the corresponding value from the number
        for _ in range(num // val[i]):
            roman_num += syb[i]
            num -= val[i]

        # Move to the next value and symbol
        i += 1

    # Return the final Roman numeral representation
    return roman_num


# Example usage:
result1 = int_to_roman(1990)
result2 = int_to_roman(2008)
result3 = int_to_roman(1666)

print(result1)  # Output: "MCMXC"
print(result2)  # Output: "MMVIII"
print(result3)  # Output: "MDCLXVI"
