"""
Given an array of strings words and a width maxWidth, format the text such that each line has exactly maxWidth characters and is fully (left and right) justified.

You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces ' ' when necessary so that each line has exactly maxWidth characters.

Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line does not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.

For the last line of text, it should be left-justified, and no extra space is inserted between words.

Note:

A word is defined as a character sequence consisting of non-space characters only.
Each word's length is guaranteed to be greater than 0 and not exceed maxWidth.
The input array words contains at least one word.


Example 1:

Input: words = ["This", "is", "an", "example", "of", "text", "justification."], maxWidth = 16
Output:
[
   "This    is    an",
   "example  of text",
   "justification.  "
]
Example 2:

Input: words = ["What","must","be","acknowledgment","shall","be"], maxWidth = 16
Output:
[
  "What   must   be",
  "acknowledgment  ",
  "shall be        "
]
Explanation: Note that the last line is "shall be    " instead of "shall     be", because the last line must be left-justified instead of fully-justified.
Note that the second line is also left-justified because it contains only one word.
Example 3:

Input: words = ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"], maxWidth = 20
Output:
[
  "Science  is  what we",
  "understand      well",
  "enough to explain to",
  "a  computer.  Art is",
  "everything  else  we",
  "do                  "
]


Constraints:

1 <= words.length <= 300
1 <= words[i].length <= 20
words[i] consists of only English letters and symbols.
1 <= maxWidth <= 100
words[i].length <= maxWidth
"""


class Solution:
    def fullJustify(self, words, maxWidth):
        result = []
        line, line_length = [], 0

        for word in words:
            if line_length + len(word) + len(line) <= maxWidth:
                line.append(word)
                line_length += len(word)
            else:
                spaces_needed = maxWidth - line_length
                if len(line) == 1:
                    result.append(line[0] + ' ' * spaces_needed)
                else:
                    space_between_words, extra_spaces = divmod(spaces_needed, len(line) - 1)
                    line_str = ''
                    for i in range(len(line) - 1):
                        line_str += line[i] + ' ' * (space_between_words + (1 if i < extra_spaces else 0))
                    line_str += line[-1]
                    result.append(line_str)

                line, line_length = [word], len(word)

        result.append(' '.join(line).ljust(maxWidth))
        return result


# Example usage
if __name__ == "__main__":
    solution = Solution()
    words1 = ["This", "is", "an", "example", "of", "text", "justification."]
    words2 = ["What", "must", "be", "acknowledgment", "shall", "be"]
    words3 = ["Science", "is", "what", "we", "understand", "well", "enough", "to", "explain", "to", "a", "computer.",
              "Art", "is", "everything", "else", "we", "do"]

    maxWidth = 16

    result1 = solution.fullJustify(words1, maxWidth)
    result2 = solution.fullJustify(words2, maxWidth)
    result3 = solution.fullJustify(words3, maxWidth)

    for line in result1:
        print(line)

    for line in result2:
        print(line)

    for line in result3:
        print(line)


