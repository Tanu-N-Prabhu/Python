"""
Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.



Example 1:

Input: nums = [1,2,3,1], k = 3
Output: true
Example 2:

Input: nums = [1,0,1,1], k = 1
Output: true
Example 3:

Input: nums = [1,2,3,1,2,3], k = 2
Output: false


Constraints:

1 <= nums.length <= 105
-109 <= nums[i] <= 109
0 <= k <= 105
"""
from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # Create a dictionary to store the indices of values
        value_indices = {}

        for i, num in enumerate(nums):
            if num in value_indices and abs(i - value_indices[num]) <= k:
                return True
            # Update the index of the value
            value_indices[num] = i

        return False


# Test case
solution = Solution()
nums = [1, 2, 3, 1]
k = 3
result = solution.containsNearbyDuplicate(nums, k)
print(result)  # Expected output: True
