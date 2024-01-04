"""
Complete the method/function so that it converts dash/underscore delimited words into camel casing.
The first word within the output should be capitalized only if the original word was capitalized
(known as Upper Camel Case, also often referred to as Pascal case).
The next words should be always capitalized.

Examples
"the-stealth-warrior" gets converted to "theStealthWarrior"

"The_Stealth_Warrior" gets converted to "TheStealthWarrior"

"The_Stealth-Warrior" gets converted to "TheStealthWarrior"
"""
import re


def to_camel_case(text):
    # Split the text into words based on dash or underscore
    words = re.split('[-_]', text)

    # # Capitalize the first word if it was capitalized in the original text
    # if words and words[0].isupper():
    #     words[0] = words[0].capitalize()

    # Capitalize the remaining words
    words[1:] = [word.capitalize() for word in words[1:]]

    # Join the words to form the camel case
    camel_case_text = ''.join(words)

    return camel_case_text


# Example usage:
result1 = to_camel_case("the-stealth-warrior")
result2 = to_camel_case("The_Stealth_Warrior")
result3 = to_camel_case("The_Stealth-Warrior")

print(result1)  # Output: "theStealthWarrior"
print(result2)  # Output: "TheStealthWarrior"
print(result3)  # Output: "TheStealthWarrior"
