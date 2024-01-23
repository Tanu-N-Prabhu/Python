# Input: an integer n
n = int(input())

# Function to generate the first n Fibonacci numbers
def generate_fibonacci(n):
    fibonacci = [0, 1]
    while len(fibonacci) < n:
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
    
    # Remove the first two Fibonacci numbers (0 and 1) if n is greater than 2
    return fibonacci[:n]

# Generate the first n Fibonacci numbers
fibonacci_numbers = generate_fibonacci(n)

# Use map and lambda to cube each number in the Fibonacci sequence
cubed_fibonacci = list(map(lambda x: x**3, fibonacci_numbers))

# Print the result
print(cubed_fibonacci)
