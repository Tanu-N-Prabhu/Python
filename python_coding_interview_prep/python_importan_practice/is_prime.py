def is_prime(number):
    """
    Check if a given number is prime.
    """
    if number <= 1:
        return False
    elif number == 2:
        return True
    elif number % 2 == 0:
        return False
    else:
        # Check divisibility from 3 to the square root of the number steps 2
        for i in range(3, int(number**0.5) + 1, 2):
            if number % i == 0:
                return False
        return True

# Example Usage:
num_to_check = 13
if is_prime(num_to_check):
    print(f"{num_to_check} is a prime number.")
else:
    print(f"{num_to_check} is not a prime number.")
