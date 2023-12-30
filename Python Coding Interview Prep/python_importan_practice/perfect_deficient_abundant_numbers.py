"""
Perfect, deficient and abundant numbers

A perfect number is a number for which the sum of its proper divisor is exactly equal to the number.
eg. 1+2+4+7+14 = 28 which means 28 is a perfect number.

A number n is called deficient if the sum of its proper divisor is less than n and it is called 
abundant if the sum exceeds n.

input 
28
output
Perfect
"""

def get_divs(n):
    return [i for i in range(1, n) if n % i == 0]


def classify(num):
    divs_sum = sum(get_divs(num))
    if divs_sum > num:
        print('{} is abundant number'.format(num))
    elif divs_sum < num:
        print('{} is deficient number'.format(num))
    elif divs_sum == num:
        print('{} is perfect number'.format(num))