def lin_search(ourlist, key):
    
    for index in range(0, len(ourlist)):
        if (ourlist[index] == key):
            return  index
    else:
        return "not fund"
    
ourlist = [15, 1, 9, 3]

lin_search(ourlist, 27)