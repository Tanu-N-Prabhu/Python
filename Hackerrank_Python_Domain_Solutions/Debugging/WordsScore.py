# Context:
# The provided code defines two functions, is_vowel and score_words, to calculate a score for a list of words based on
# the number of vowels in each word. The functions use a simple scoring system: 2 points for words with an even number of
# vowels and 1 point for words with an odd number of vowels.

# Function: is_vowel
# Parameters:
# - letter: A single character to check if it is a vowel.
# Returns:
# - True if the letter is a vowel (a, e, i, o, u, y), otherwise False.

def is_vowel(letter):
    return letter in ["a", "e", "i", "o", "u", "y"]

# Function: score_words
# Parameters:
# - words: A list of words for which the score needs to be calculated.
# Returns:
# - The total score calculated based on the number of vowels in each word.
# - The score for a word is 2 if the count of vowels is even, and 1 if it's odd.

def score_words(words):
    score = 0
    for word in words:
        num_vowels = sum(1 for letter in word if is_vowel(letter))
        score += 2 if num_vowels % 2 == 0 else 1
    return score

# Example Usage:
# words_list = ["hello", "world", "python"]
# total_score = score_words(words_list)
