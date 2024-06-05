from typing import List
"""
String Encode and Decode
Design an algorithm to encode a list of strings to a single string. The encoded string is then decoded back to the original list of strings.

Please implement encode and decode

Example 1:

Input: ["neet","code","love","you"]

Output:["neet","code","love","you"]
Example 2:

Input: ["we","say",":","yes"]

Output: ["we","say",":","yes"]
Constraints:

0 <= strs.length < 100
0 <= strs[i].length < 200
strs[i] contains only UTF-8 characters.

"""

from typing import List

class Solution:
    # Encode a list of strings into a single string
    def encode(self, strs: List[str]) -> str:
        return ''.join(f'{len(s)}#{s}' for s in strs)

    # Decode a single string back into a list of strings
    def decode(self, encoded_str: str) -> List[str]:
        res = []
        i = 0
        
        while i < len(encoded_str):
            # Find the position of the next '#'
            j = encoded_str.find('#', i)
            if j == -1:
                break
            
            # Extract the length of the next string
            length = int(encoded_str[i:j])
            
            # Extract the string itself
            i = j + 1
            res.append(encoded_str[i:i + length])
            
            # Move to the start of the next length indicator
            i += length
        
        return res

    

if __name__=="__main__":
    s = Solution()
    strs = ["neet","code","love","you"]
    result = s.decode(s.encode(strs))
    print(result)

    strs = ["we","say",":","yes"]
    result = s.decode(s.encode(strs))
    print(result)

    strs = []
    result = s.decode(s.encode(strs))
    print(result)

    strs = [""]
    result = s.decode(s.encode(strs))
    print(result)
    