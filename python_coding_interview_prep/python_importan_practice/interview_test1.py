# *** TASK 2 ***
#
# Explain the following behavior in Python Interactive shell.

"""
>>> True, True, True == (True, True, True)
(True, True, False)
"""

# *** // TASK 2 END ***

# *** TASK 3 ***
#
# Transform uppercase chars to lowercase and vice-versa
# So following will become "AAbbccJJiiAAAmmMMLLlllLIIOIS"
from functools import reduce

s = "aaBBCCjjIIaaaMMmmllLLLliiois"
print([x.upper() if x.islower() else x.lower() for x in s])

# *** // TASK 3 END ***

# *** TASK 4 ***
#
# Transform following list into dict, using item as value and it's position in list as key:

l = [45, 22, 14, 65, 97, 72]
dict = {}
map(lambda x: dict.append([x]),for i in l)
# *** // TASK 4 END ***``


# *** TASK 5 ***
#
# Sort a list of dicts by price descending
cars = [
    {"model": "Ford T", "price": 2000},
    {"model": "Ford F150", "price": 25000},
    {"model": "Ford Focus", "price": 12000},
]

sorted(cars.items(), key=lambda x: x['price'], reversed=True)

# *** // TASK 5 END ***


# *** TASK 6 ***
#
# Sum squares of first 100000 integers

result = reduce(lambda x, y: ((x ** x) + (y ** y)), range(1, 100000))

# *** // TASK 6 END ***

def add_consonant_and_ay_at_end(word):
    """
    This function processes a word according to the rules:
    - If the word starts with a vowel, add 'yay' to the end.
    - If the word starts with a consonant, move all consonants at the beginning
      to the end, then add 'ay'.
    - Retain the original case of the word.
    """

    # Initialize variables
    l = len(word)
    new_word = []  # To store the processed part of the word
    consonants = []  # To store the leading consonants
    flag = 0  # To indicate when to stop collecting consonants
    vowels = ['a', 'e', 'i', 'o', 'u']  # List of vowels
    response = None  # To store the final processed word
    all_caps = 1  # Flag to check if the word is all uppercase

    # Check if the first character is a vowel
    if word[0].lower() in vowels:
        if word[0].isupper():
            # If the word starts with a capital vowel, capitalize the result
            return word.capitalize() + 'yay'
        return word + 'yay'

    # Iterate over the word
    for i in range(l):
        if word[i].islower():
            all_caps = 0  # If any character is lowercase, set all_caps to 0
        if word[i].lower() not in vowels and flag == 0:
            consonants.append(word[i])  # Collect leading consonants
        else:
            flag = 1  # Stop collecting consonants after the first vowel

        if flag == 1:
            new_word.append(word[i])  # Collect the rest of the word

    # Construct the response by appending consonants and 'ay'
    response = ''.join(new_word) + ''.join(consonants) + 'ay'

    # Handle capitalization
    if all_caps == 1:
        response = response.upper()  # If the word was all uppercase, make the response uppercase
    elif word[0].isupper():
        response = response.capitalize()  # Capitalize the response if the word started with a capital letter

    return response

def process_sentence(sentence):
    """
    This function processes each word in a sentence using add_consonant_and_ay_at_end.
    It splits the sentence into words, processes each word, and joins them back into a sentence.
    """

    words = sentence.split()  # Split the sentence into words
    processed_words = [add_consonant_and_ay_at_end(word) for word in words]  # Process each word
    return ' '.join(processed_words)  # Join the processed words back into a sentence

if __name__ == "__main__":
    # Test the function with individual words
    word = "pig"
    print(add_consonant_and_ay_at_end(word))  # Expected output: "igpay"
    word = 'floor'
    print(add_consonant_and_ay_at_end(word))  # Expected output: "oorflay"
    word = 'egg'
    print(add_consonant_and_ay_at_end(word))  # Expected output: "eggyay"
    word = 'I'
    print(add_consonant_and_ay_at_end(word))  # Expected output: "Iyay"
    word = 'LATIN'
    print(add_consonant_and_ay_at_end(word))  # Expected output: "ATINLAY"

    # Test the function with sentences
    sentence = "please to meet you"
    print(process_sentence(sentence))  # Expected output: "easeplay otay eetmay ouyay"

    sentence = "how much does it cost?"
    print(process_sentence(sentence))  # Expected output: "owhay uchmay oesday ityay ostcay?"

    sentence = "a tree which has LATIN name and also it has a CAPITAL city"
    print(process_sentence(sentence))
    # Expected output: "ay eetray ichwhay ashay ATINLAY amenay andyay alsoyay ityay ashay ay APITALCAY ityay"

