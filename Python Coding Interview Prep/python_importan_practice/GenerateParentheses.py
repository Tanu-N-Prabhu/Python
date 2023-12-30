"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.



Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:

Input: n = 1
Output: ["()"]


Constraints:

1 <= n <= 8
"""


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def backtrack(s, left, right):
            if len(s) == 2 * n:
                result.append(s)
                return
            if left < n:
                backtrack(s + '(', left + 1, right)
            if right < left:
                backtrack(s + ')', left, right + 1)

        result = []
        backtrack('', 0, 0)
        return result


# Example usage:
n = 3
solution = Solution()
result = solution.generateParenthesis(n)
print(result)
