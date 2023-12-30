# remove adjacent duplicate chars
def reduce_string(string, iterate=0):
    try:
        # remove special chars
        string = ''.join(e for e in string if e.isalnum())

        if type(string) != str:
            return "Not a valid string"
        if (iterate == 0) and (len(string) == 0):
            return "Kindly input a string only"

        # make the string lower case
        string = string.lower()
        l = len(string)
        # no need to process if the string len is 0 or 1
        if l == 1:
            return string

        # make it a list
        ls = list(string)
        matched_pairs = []
        previous = None
        # loop thorugh all chars of string as list
        for i in range(0, l):
            if ls[i] == previous:
                # adjacent duplicate or pair
                matched_pairs.append(ls[(i-1)] + ls[i])
                previous = None
            else:
                previous = ls[i]

        # now need to remove duplicate pair chars from string
        for i in matched_pairs:
            string = string.replace(i, '')

        # if still
        if len(matched_pairs) > 0:
            iterate += 1
            string = reduce_string(string, iterate)
        elif len(string) > 0:
            return string
        else:
            return "Empty string"

    except Exception as e:
        return str(e)

    return string


# call the function from users command
print('\033c')
print("\nYou can test several times until you press ctrl + D\n")
print("Reduced a string after removed all adjacent duplicate characters")

while True:
    try:
        string = input("Enter a string : ")
        result = reduce_string(string)
        print("Result : %s\n" % result)
    except EOFError:
        break
