def minion_game(string):
    # your code goes here
    
    vowels = ['A', 'E', 'I', 'O', 'U']
    kevin = 0
    stuart = 0
    for i in range(len(string)):
        if s[i] in vowels:
            kevin = kevin + (len(s)-i)
        else:
            stuart = stuart + (len(s)-i)

    if stuart > kevin:
        print('Stuart '+ str(stuart))
    elif kevin > stuart:
        print('Kevin ' + str(kevin))
    else:
        print('Draw')
  

if __name__ == '__main__':
    s = input()
    minion_game(s)