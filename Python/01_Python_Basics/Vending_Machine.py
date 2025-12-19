import sys

option = int(input("Enter the option as 1, 2 or 3"))

if option == 1:
    charge = 1.00
elif option == 2:
    charge = 1.50
elif option ==3:
    charge = 2.00
else:
    sys.exit("Invalid option: Try again !!!!!")

quaters = int(input("Enter the quarters"))
nickels = int(input("Enter the nickles"))
dimes = int(input("Enter the dimes"))
pennies = int(input("Enter the pennis"))

total = quaters*0.25 + nickels+0.10 + dimes*0.05 + pennies*0.01

print("You total money is: %f" %(total))

if total >= charge:
    print("You change is: %f" % (total-charge))

else:
    print("Please try again")
