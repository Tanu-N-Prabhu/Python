from typing import List
"""
Products of Array Discluding Self
Given an integer array nums, return an array output where output[i] is the product of all the elements of nums except nums[i].

Each product is guaranteed to fit in a 32-bit integer.

Follow-up: Could you solve it in 
O(𝑛)
O(n) time without using the division operation?

Example 1:

Input: nums = [1,2,4,6]

Output: [48,24,12,8]
Example 2:

Input: nums = [-1,0,1,2,3]

Output: [0,-6,0,0,0]
Constraints:

2 <= nums.length <= 1000
-20 <= nums[i] <= 20
"""


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Create a list 'res' with length equal to 'nums' and initialize all elements to 1
        res = [1] * len(nums)
        
        # Initialize 'prefix' to 1
        prefix = 1
        
        # Iterate through the 'nums' list
        for i in range(len(nums)):
            # Set the current element in 'res' to the current 'prefix' value
            res[i] = prefix
            
            # Multiply the 'prefix' by the current element in 'nums'
            prefix *= nums[i]
            
        # Initialize 'postfix' to 1
        postfix = 1
        
        # Iterate through the 'nums' list in reverse order
        for i in range(len(nums) - 1, -1, -1):
            # Multiply the current element in 'res' by the current 'postfix' value
            res[i] *= postfix
            
            # Multiply the 'postfix' by the current element in 'nums'
            postfix *= nums[i]
        
        # Return the 'res' list
        return res


if __name__ == "__main__":
    nums = [1, 2, 4, 6]
    s = Solution()
    print(s.productExceptSelf(nums))
    nums = [-1, 0, 1, 2, 3]
    print(s.productExceptSelf(nums))
