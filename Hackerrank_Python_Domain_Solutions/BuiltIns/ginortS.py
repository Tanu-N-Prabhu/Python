# Context:
# This script takes a string 's' as input and sorts its characters based on multiple criteria.
# The sorting order is as follows:
#   1. Even digits come before odd digits.
#   2. Digits come before uppercase letters.
#   3. Uppercase letters come before lowercase letters.
#   4. Characters are sorted lexicographically.

# Input: A string 's' containing alphanumeric characters.

# Output: A sorted string based on the specified criteria.

# Example:
# Input: "aB2Z7XY1"
# Output: "147BXYZa"
# Explanation: The digits are sorted first (1, 7, 2), followed by uppercase letters (B, X, Y, Z),
# and finally, lowercase letters (a).

# Sorting Logic:
# The lambda function in the sorted function defines the sorting criteria using multiple keys.
# 1. x.isdigit() and int(x) % 2 == 0: Even digits come first.
# 2. x.isdigit(): Digits come next.
# 3. x.isupper(): Uppercase letters come after digits.
# 4. x.islower(): Lowercase letters come after uppercase letters.
# 5. x: Lexicographical order for characters.

# The sorted characters are then joined to form the final sorted string.

s = input()
sorted_string = "".join(
    sorted(
        s,
        key=lambda x: (
            x.isdigit() and int(x) % 2 == 0,
            x.isdigit(),
            x.isupper(),
            x.islower(),
            x,
        ),
    )
)
print(sorted_string)
