"""
Greatest common divisor by subtraction.
"""
def gcd(a, b):
    if a == b:
        return a
    if a > b:
        gcd(a - b, b)
    else:
        gcd(a, b - a)


"""
Greatest common divisor by division.
"""
def gcd(a, b):
    if a == b:
        return a
    if a > b:
        gcd(a // b, b)
    else:
        gcd(a, b // a)

        
"""
Greatest common divisor by multiplication.
"""
def gcd(a, b):
    if a == b:
        return a
    if a > b:
        gcd(a * (b // a), b)
    else:
        gcd(a, b * (a // b))

        
"""
Greatest common divisor by recursion.
"""
def gcd(a, b):
    if a == b:
        return a
    if a > b:
        return gcd(a - b, b)
    else:
        return gcd(a, b - a)
