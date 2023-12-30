# this will calculate the total chocolate as per input
# some wrapper also give free chocolate
def get_chocolates(money, price, discount):
    # validations
    money = int(money)
    price = int(price)
    discount = int(discount)

    if money <= 0:
        return "Not valid total money have"
    elif price <= 0:
        return "Not valid price"
    elif discount < 0:
        return "Not valid no of wrapper required to exchange each chocolate"
    elif price > money:
        return 0

    chocolate_first = money // price
    wrappers_discount = 0
    if discount != 0:
        wrappers_discount = chocolate_first // discount
    total_chocolates = chocolate_first + wrappers_discount

    return total_chocolates


# call the function from users command
print('\033c')
print("\nYou can test several times until you press ctrl + D\n")
print("It will calculate how many chocolates can get.")
print("Against total money, price of each chocolate and")
print("discount get while number of wrappers exchange for each chocolate\n")

while True:
    try:
        money = input("Enter the total money have : ")
        price = input("Enter the price of each chocolate : ")
        discount = input(
            "Enter the no of wrapper required for each chocolate : ")
        result = get_chocolates(money, price, discount)
        print("Result : %s\n" % result)
    except EOFError:
        break
