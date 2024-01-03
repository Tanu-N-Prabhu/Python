def pf(n, p):
    pfc = 0
    result = 1
    for i in p:
        while n % i == 0:
            n //= i
            pfc += 1
            if n == 1 or n == 0:
                result *= i ** ((pfc + 1) // 2)
                return result
    return None


n = 78
p = [2, 3, 5]

print(pf(n, p))
