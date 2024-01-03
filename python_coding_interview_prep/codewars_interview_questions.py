"""
The Morse code encodes every character as a sequence of "dots" and "dashes".
For example, the letter A is coded as ·−, letter Q is coded as −−·−, and digit 1 is coded as ·−−−−.
The Morse code is case-insensitive, traditionally capital letters are used. When the message is
written in Morse code, a single space is used to separate the character codes and 3 spaces are
used to separate words. For example, the message 'HEY JUDE' in Morse code is ···· · −·−−   ·−−− ··− −·· ·.

NOTE: Extra spaces before or after the code have no meaning and should be ignored.

In addition to letters, digits and some punctuation, there are some special service codes,
the most notorious of those is the international distress signal SOS (that was first issued by Titanic),
that is coded as ···−−−···. These special codes are treated as single special characters,
and usually are transmitted as separate words.

Your task is to implement a function that would take the morse code as input and return a decoded
human-readable string.

For example:

decode_morse('.... . -.--   .--- ..- -.. .')
#should return "HEY JUDE"
NOTE: For coding purposes you have to use ASCII characters . and -, not Unicode characters.

The Morse code table is preloaded for you as a dictionary, feel free to use it:

Coffeescript/C++/Go/JavaScript/Julia/PHP/Python/Ruby/TypeScript: MORSE_CODE['.--']

All the test strings would contain valid Morse code, so you may skip checking for errors and exceptions. In C#, tests will fail if the solution code throws an exception, please keep that in mind. This is mostly because otherwise the engine would simply ignore the tests, resulting in a "valid" solution.
"""
import unittest


MORSE_CODE = {'.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '..-.': 'F',
              '--.': 'G', '....': 'H', '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L',
              '--': 'M', '-.': 'N', '---': 'O', '.--.': 'P', '--.-': 'Q', '.-.': 'R',
              '...': 'S', '-': 'T', '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X',
              '-.--': 'Y', '--..': 'Z', '-----': '0', '.----': '1', '..---': '2',
              '...--': '3', '....-': '4', '.....': '5', '-....': '6', '--...': '7',
              '---..': '8', '----.': '9', '.-.-.-': '.', '--..--': ',', '..--..': '?',
              '.----.': "'", '-.-.--': '!', '-..-.': '/', '-.--.': '(', '-.--.-': ')',
              '...-..-': "$", '.-...': '&', '---...': ':', '-.-.-.': ';', '-...-': '=',
              '...---...': 'SOS'}


def decode_morse(morse_code):
    """Decodes Morse code into human-readable text."""
    words = morse_code.strip().split("   ")  # Split into words
    decoded_words = [] # result list
    for word in words:
        letters = word.split(" ")  # Split word into letters
        # join the letters in a string to form a word
        decoded_word = "".join(MORSE_CODE.get(letter, "") for letter in letters)
        # save into a list
        decoded_words.append(decoded_word)
    # convert the list into a string
    return " ".join(decoded_words)


# Example usage:
encoded_message = ".... . -.--   .--- ..- -.. ."
decoded_message = decode_morse(encoded_message)
print(decoded_message)  # Output: HEY JUDE


class TestDecodeMorse(unittest.TestCase):
    def test_decode_morse(self):
        self.assertEqual(decode_morse('.... . -.--   .--- ..- -.. .'), 'HEY JUDE')
        self.assertEqual(decode_morse('.-'), 'A')
        self.assertEqual(decode_morse('--...'), '7')
        self.assertEqual(decode_morse('...-..-'), '$')
        self.assertEqual(decode_morse('.'), 'E')
        self.assertEqual(decode_morse('..'), 'I')
        self.assertEqual(decode_morse('. .'), 'EE')
        self.assertEqual(decode_morse('.   .'), 'E E')
        self.assertEqual(decode_morse('...-..- ...-..- ...-..-'), '$$$')
        self.assertEqual(decode_morse('----- .---- ..--- ---.. ----.'), '01289')
        self.assertEqual(decode_morse('.-... ---...   -..-. --...'), '&: /7')
        self.assertEqual(decode_morse('...---...'), 'SOS')
        self.assertEqual(decode_morse('... --- ...'), 'SOS')
        self.assertEqual(decode_morse('...   ---   ...'), 'S O S')
        self.assertEqual(decode_morse(' . '), 'E')
        self.assertEqual(decode_morse('   .   . '), 'E E')
        self.assertEqual(decode_morse(
            '      ...---... -.-.--   - .... .   --.- ..- .. -.-. -.-   -... .-. --- '
            '.-- -.   ..-. --- -..-   .--- ..- -- .--. ...   --- ...- . .-.   - .... .'
            '   .-.. .- --.. -.--   -.. --- --. .-.-.-  '),
            'SOS! THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG.')

        # Add more test cases as needed


if __name__ == '__main__':
    test_decode_morse = TestDecodeMorse()
    TestDecodeMorse.test_decode_morse(self=test_decode_morse)




