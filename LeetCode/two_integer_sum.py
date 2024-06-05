from typing import List
"""
Two Integer Sum
Given an array of integers nums and an integer target, return the indices i and j such that nums[i] + nums[j] == target and i != j.

You may assume that every input has exactly one pair of indices i and j that satisfy the condition.

Return the answer with the smaller index first.

Example 1:

Input: 
nums = [3,4,5,6], target = 7

Output: [0,1]
Explanation: nums[0] + nums[1] == 7, so we return [0, 1].

Example 2:

Input: nums = [4,5,6], target = 10

Output: [0,2]
Example 3:

Input: nums = [5,5], target = 10

Output: [0,1]
Constraints:

2 <= nums.length <= 1000
-10000 <= nums[i] <= 10000
-10000 <= target <= 10000

"""

# class Solution:
#     # big O(n^2)
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         for i in range(len(nums)):
#             for j in range(i+1, len(nums)):
#                 if nums[i] + nums[j] == target:
#                     return [i, j]
                

class Solution:
    # big O(n)
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # create a dictionary to store the complement of each number
        complement_dict = {}

        # iterate through the array
        for i, num in enumerate(nums):
            # calculate the complement of each number
            complement = target - num

            # check if the complement is in the dictionary
            if complement in complement_dict:
                # if it is, return the indices of the complement and the current number
                return [complement_dict[complement], i]
            # add the current number to the dictionary with its index
            complement_dict[num] = i
        return []

                

if __name__ == '__main__':
    s = Solution()
    nums = [3,4,5,6]
    target = 7
    print(s.twoSum(nums, target))
    nums = [4,5,6]
    target = 10
    print(s.twoSum(nums, target))
