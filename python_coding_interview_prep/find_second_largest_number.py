# This will find the second largest number in a list
def second_largest(numbers):
    first, second = float('-inf'), float('-inf')
    for num in numbers:
        if num > first:
            first, second = num, first
        elif first > num > second:
            second = num
    return second if second != float('-inf') else None

if __name__ == '__main__':
    numbers = [10, 5, 20, 8, 15]
    print(second_largest(numbers))  # Output: 15
    