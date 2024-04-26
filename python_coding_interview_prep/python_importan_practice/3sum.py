"""
Given an integer array nums, return all the triplets
[nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation:
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.
Example 2:

Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.
Example 3:

Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.


Constraints:

3 <= nums.length <= 3000
-105 <= nums[i] <= 105
"""
from typing import List


class Solution:
    def threeSum(self, nums: List[int]):
        # Sort the input list in ascending order
        nums.sort()
        result = []

        # Loop through the list, considering each element as a potential first element of a triplet
        # By starting the loop at len(nums) - 2, you ensure that
        # there are at least two more elements (i+1 and i+2) in the array nums
        # to form a triplet with the current element at index i
        for i in range(len(nums) - 2):
            # Skip duplicates to avoid duplicate triplets
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # Initialize two pointers, one at the next element, and the other at the end of the list
            left, right = i + 1, len(nums) - 1

            # Check for triplets with a sum of zero
            # continues until the left and right pointers meet or cross each other.
            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total == 0:
                    # Found a triplet with a sum of zero, add it to the result
                    result.append([nums[i], nums[left], nums[right]])

                    # Skip duplicates of the left and right pointers
                    while nums[left] == nums[left + 1]:
                        left += 1
                    while nums[right] == nums[right - 1]:
                        right -= 1

                    # Move the pointers towards each other
                    left += 1
                    right -= 1
                elif total < 0:
                    # The sum is too small, move the left pointer to the right
                    # as numbers are sorted in asc order
                    left += 1
                else:
                    # The sum is too large, move the right pointer to the left
                    # as mumber as sorted in asc order
                    right -= 1

        return result


# Example usage
if __name__ == "__main__":
    solution = Solution()
    nums = [-1, 0, 1, 2, -1, -4]
    result = solution.threeSum(nums)
    print(result)  # Output: [[-1, -1, 2], [-1, 0, 1]]

    nums = [-1, -2, 1, 0, -1, -2, 0, -1]
    result = solution.threeSum(nums)
    print(result)  # Output: [[-1, 0, 1]]


