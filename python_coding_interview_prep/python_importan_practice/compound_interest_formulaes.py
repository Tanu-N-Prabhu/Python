def A(P, r, n, t):
    r = r / 100
    return round(P * ((1 + r / n)**(n * t)), 2)


def CI(P, r, n, t):
    r = r / 100
    return round((P * ((1 + r / n)**(n * t)) - P), 2)


def R(A, P, n, t):
    return round((n * (((A / P)**(1 / (n * t))) - 1) * 100), 2)


P = 10000
r = 5
n = 1
t = 3

A = A(P, r, n, t)
print(A)
print(CI(P, r, n, t))
print(R(A, P, n, t))
