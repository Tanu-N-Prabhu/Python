"""
the number 197 called a circular prime becuase all rotations (not all permutations)
of the digits 197, 971 and 719 are themselves are prime

write a program to count the number of circular prime numbers less than or 
equal to given number.

input
100
output
13 becuase 2,3,5,7,11,13,17,31,37,71,73,79 and 97
"""

def isprime(num):
    count=0
    for i in range(1,num+1):
        if(num % i ==0):
            count+=1
    if(count==2):
        return 1
    else:
        return 0


digit=0
i=0
rem=0
sum=0
check=input("enter the number: ")
length=len(check)
num=int(check)
while(i<length):
    rem=int(num % 10)
    num=int(num / 10)
    num=int((rem * (10 ** (length - 1)) + num))
    print(num)
    digit=isprime(num)
    sum=sum+digit
    i+=1
if(sum==length):
    print("Circular Prime")
else:
    print("Non-Circular Prime")