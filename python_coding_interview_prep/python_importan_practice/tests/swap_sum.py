# swap left right of middle number and sum all digits of number
def swap_sum(num):
    try:
        l = len(str(num))
        # check length and odd or not
        if l < 3:
            return "Interger must be at least 3 digits or more"

        if l % 2 == 0:
            return "Integer length must be odd eg. 3 or 5 or 7 etc"

        # middle number index in list
        middle_index = l // 2
        num_as_list = [int(i) for i in str(num)]
        middle_value = num_as_list[middle_index]
        new_list = []

        # swapping
        left = num_as_list[0:middle_index]
        right = num_as_list[(middle_index + 1):]
        new_list.extend(right[::-1])
        new_list.append(middle_value)
        new_list.extend(left[::-1])
        str1 = ''
        for i in new_list:
            str1 += str(i)
        print("\nNew number after digit by digit swapping around middle digit : %s" % str1)

        # sum of the all digits of num
        sum_num = sum(num_as_list)
    except Exception as e:
        return str(e)

    return sum_num


# call the function from users command
print('\033c')
print("\nYou can test several times until you press ctrl + D\n")
print("It will swap left and right digits of middle one then sum up\n")

while True:
    try:
        num = input("Enter a integer : ")
        result = swap_sum(num)
        print("Result : %s\n" % result)
    except EOFError:
        break
