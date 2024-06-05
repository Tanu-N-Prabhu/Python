from typing import List
"""
Duplicate Integer
Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.

Example 1:

Input: nums = [1, 2, 3, 3]

Output: true
Example 2:

Input: nums = [1, 2, 3, 4]

Output: false

"""


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # set do not take duplicate
        return len(nums) != len(set(nums))


if __name__ == "__main__":
    nums = [1, 2, 3, 1]
    print(Solution().containsDuplicate(nums))
    nums = [1, 2, 3, 4]
    print(Solution().containsDuplicate(nums))
