"""
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.




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
from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        # Define the mapping of digits to letters
        phone_mapping = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        def backtrack(combination, next_digits):
            # If there are no more digits to check, add the combination to the result
            if not next_digits:
                result.append(combination)
            else:
                # Get the letters corresponding to the current digit
                current_digit = next_digits[0]
                letters = phone_mapping[current_digit]
                for letter in letters:
                    # Recursively explore all possible combinations
                    backtrack(combination + letter, next_digits[1:])

        result = []
        backtrack("", digits)
        return result


# Example usage
digits = "23"
solution = Solution()
result = solution.letterCombinations(digits)
print(result)  # Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
