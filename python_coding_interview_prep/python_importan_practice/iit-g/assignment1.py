"""
Q1. A token is the smallest individual unit in a python program. Tokens are following
keywords: True, False and, not, or, if, while, break eg. if i == 5 and j == 10
identifiers: Identifiers are the names given to any variable, function, class, list, methods, etc. for their identification. eg. students = []
operators: eg. i == j
literals: Literals are the fixed values or data items used in a source code. eg. {"name": "dhiraj"}
"""


"""
Q2. 
"""
a=[11,89,41,32,77,90]
b=[95,24,39,15,74,22]

# by list comprehension
[print("a element value is greater than b \
element value") if x > y else print("a element value is less \
than b element value") for x, y in zip(a, b)]
print('-' * 100)
# or by loop
for x, y in zip(a,b):
   if x > y:
       print("a element value is greater than element value")
   elif x < y:
       print("a element value is less than b element value")
print('-' * 100)

"""
Q3.
"""
class Calculator:
    """
    This is calculator class
    """
    num1 = None
    num2 = None

    def __init__(self):
        print("Calculator object created")

    def addition(self)->float:
        return self.num1 + self.num2

    def subtraction(self)-> float:
        return self.num1 - self.num2

    def multiplication(self)->float:
        return self.num1 * self.num2

    def division(self)->float:
        return self.num1 / self.num2

    def execute_command(self, num1: float, num2: float, op: str)-> float:
        try:
            self.num1 = num1
            self.num2 = num2

            if op.lower() == 'add':
                return self.addition()

            elif op.lower() == 'sub':
                return self.subtraction()

            elif op.lower() == 'mul':
                return self.multiplication()

            elif op.lower() == 'div':
                return self.division()

            else:
                print("Please enter valid numbers and command to execute")
        except:
            print("please enter valid data")


c = Calculator()
num1 = 2
num2 = 4
print(num1, num2)
print("Add %s" % c.execute_command(num1, num2, 'aDd'))
print("Sub %s" % c.execute_command(num1, num2, 'sub'))
print("Mul %s" % c.execute_command(num1, num2, 'MUL'))
print("Div %s" % c.execute_command(num1, num2, 'dIv'))
print('-' * 100)

"""
Q4.
"""
numbers = []
n = 0
while n >= 0:
    n = int(input("Enter the number or enter 0 to exit: "))
    if n == 0:
        break
    numbers.append(n)


a = [(x, x**2) for x in numbers]
print("(Number, square)")
print(a)
print('-' * 100)

"""
Q5.
"""
def check_leap_year(year: int) -> bool:
    if year > 0 and (year % 4 == 0 and year // 100 != 0) or (year % 400 == 0):
        return True
    return False

print(check_leap_year(int(input("Enter the year to check leap year or not: "))))
print('-' * 100)

"""
Q6.
"""
arr = [x for x in range(1, 11)]
print(arr)
even_numbers = []
odd_numbers = []
result = {}

[even_numbers.append(x) if x % 2 == 0 else odd_numbers.append(x) for x in arr]
result['even'] = even_numbers
result['odd'] = odd_numbers
print(result)
print('-' * 100)


"""
Q7.
"""
for i in range(1,6):
    for j in range(1,i+1):
        print(j, end =" ")
    print("\n")











