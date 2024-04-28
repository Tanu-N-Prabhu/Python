"""
Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.



Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
Example 3:

Input: nums = [], target = 0
Output: [-1,-1]


Constraints:

0 <= nums.length <= 105
-109 <= nums[i] <= 109
nums is a non-decreasing array.
-109 <= target <= 109
"""
from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # Initialize variables to store the left and right indices
        left, right = 0, len(nums) - 1

        # Initialize variables to store the starting and ending positions
        start, end = -1, -1

        # Find the starting position
        while left <= right:
            # Calculate the middle index
            mid = left + (right - left) // 2
            if nums[mid] == target:
                start = mid
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        # Find the ending position
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                end = mid
                left = mid + 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return [start, end]


# Create an instance of the Solution class
solution = Solution()

# Test Case 1
nums1 = [5, 7, 7, 8, 8, 10]
target1 = 8
result1 = solution.searchRange(nums1, target1)
print(result1)  # Expected output: [3, 4]

# Test Case 2
nums2 = [5, 7, 7, 8, 8, 10]
target2 = 6
result2 = solution.searchRange(nums2, target2)
print(result2)  # Expected output: [-1, -1]

# Test Case 3
nums3 = []
target3 = 0
result3 = solution.searchRange(nums3, target3)
print(result3)  # Expected output: [-1, -1]
