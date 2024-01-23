# Context:
# The provided code takes an integer 'n' as input, followed by 'n' pairs of integers (a, b). It attempts to perform
# integer division (a // b) for each pair and prints the result. If any exception occurs during the division,
# it catches the exception and prints an error message with the specific error code.

# Input:
# - n: An integer representing the number of pairs to process.
# - For each pair:
#   - a, b: Two integers for which integer division (a // b) is performed.

# Output:
# - For each pair, either the result of the integer division or an error message with the specific error code.

n = int(input())

for _ in range(n):
    a, b = input().split()
    try:
        result = int(a) // int(b)
        print(result)
    except Exception as e:
        print(f"Error Code: {e}")
