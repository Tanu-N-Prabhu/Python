"""
Given a string containing digits from 2-9 inclusive, return all possible letter combinations 
that the number could represent. Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given below. 
Note that 1 does not map to any letters.

1 2 [abc] 3[def]
4[ghi] 5[jkl] 6[mno]
7[pqrs] 8[tuv] 9[wxyz]
* 0 #


Example 1:

Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

Example 2:

Input: digits = ""
Output: []
Example 3:

Input: digits = "2"
Output: ["a","b","c"]
 

Constraints:

0 <= digits.length <= 4
digits[i] is a digit in the range ['2', '9'].
"""

def letterCombinations(digits):
  """
  This function finds all possible letter combinations a phone number string can represent.

  Args:
      digits: A string containing digits from 2-9 inclusive.

  Returns:
      A list of strings representing all possible letter combinations.
  """
  if not digits:
    return []
  
  # Mapping of digits to letters
  # This line defines a dictionary named mapping. Dictionaries in Python store key-value pairs.
  # The keys in this dictionary are strings representing the digits (2-9).
  # The values in the dictionary are strings representing the corresponding letters on the 
  # phone keypad for each digit.
  # This dictionary will be used later to look up the letters for each digit in the digits string.
  mapping = {
      "2": "abc",
      "3": "def",
      "4": "ghi",
      "5": "jkl",
      "6": "mno",
      "7": "pqrs",
      "8": "tuv",
      "9": "wxyz",
  }

  # Helper function to recursively backtrack and build combinations
  # This line defines a function named backtrack. This function is likely recursive (calls itself), 
  # as indicated by the lack of a return statement within its body.
  # The function takes three arguments:
  # current_combination: This is a string that represents the current combination of letters built so far. 
  # It's initially an empty string ("") in the main program.
  # index: This is an integer that keeps track of the current position (index) in the digits string. 
  # It starts at 0 (the first digit).
  # combinations: This is a list that will eventually store all the possible letter combinations. 
  # It's initially an empty list ([]) in the main program.
  def backtrack(current_combination, index, combinations):
  	# This line checks if the index has reached the end of the digits string.
    # len(digits) gives the length of the digits string.
    # If index is equal to the length, it means we've processed all the digits.
    if index == len(digits):
      combinations.append(current_combination)
      return

    # This line iterates over all the letters corresponding to the current digit in the digits string.
    # mapping[digits[index]] retrieves the value (letters string) associated with the current digit 
    # (digits[index]) from the mapping dictionary.
    # For example, if digits[index] is "2", this would iterate over the letters "a", "b", and "c".  
    for letter in mapping[digits[index]]:
      backtrack(current_combination + letter, index + 1, combinations)

  combinations = []
  backtrack("", 0, combinations)
  return combinations

# Example usage
digits = "23"
combinations = letterCombinations(digits)
print(combinations)  # Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
