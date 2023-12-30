"""
Given two binary strings a and b, return their sum as a binary string.



Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"


Constraints:

1 <= a.length, b.length <= 104
a and b consist only of '0' or '1' characters.
Each string does not contain leading zeros except for the zero itself.
"""


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        result = []
        carry = 0

        # Pad the shorter string with leading zeros
        max_len = max(len(a), len(b))
        a = a.zfill(max_len)
        b = b.zfill(max_len)

        # Perform binary addition from right to left
        for i in range(max_len - 1, -1, -1):
            bit_a = int(a[i])
            bit_b = int(b[i])
            total = bit_a + bit_b + carry
            result.append(str(total % 2))
            carry = total // 2

        if carry:
            result.append('1')

        # Reverse the result and join to form the binary string
        return ''.join(result[::-1])

# Test cases
sol = Solution()
print(sol.addBinary("11", "1"))  # Output: "100"
print(sol.addBinary("1010", "1011"))  # Output: "10101"
