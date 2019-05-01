a = input("Enter the value of a: ")
b = input("Enter the value of b: ")
c = input("Enter the value of c: ")

if a > b > c:
    print("a is greater than b and c")
elif b > c > a:
    print("b is greater than c and a")
elif a == b == c:
    print("a, b, c are all equal")
elif a == b:
    print("a and b are equal")
elif b == c:
    print("b and c are equal")
elif a == c:
    print("a and c are equal")
else:
    print("c is greater than a and b")

