"""
Complete the solution so that it strips all text that follows any of a set of comment markers passed in.
Any whitespace at the end of the line should also be stripped out.

Example:

Given an input string of:

apples, pears # and bananas
grapes
bananas !apples
The output expected would be:

apples, pears
grapes
bananas
"""


def solution(string, markers):
    lines = string.split('\n')
    for marker in markers:
        lines = [line.split(marker)[0].rstrip() for line in lines]
    return '\n'.join(lines)


# Example usage:
input_string = "apples, pears # and bananas\ngrapes\nbananas !apples"
comment_markers = ['#', '!']
output = solution(input_string, comment_markers)
print(output)
