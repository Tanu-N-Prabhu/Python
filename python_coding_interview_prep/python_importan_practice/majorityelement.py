"""
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

Example 1:

Input: nums = [3,2,3]
Output: 3
Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2

Constraints:

n == nums.length
1 <= n <= 5 * 104
-109 <= nums[i] <= 109

Follow-up: Could you solve the problem in linear time and in O(1) space?

To find the majority element in an array, you can use Boyer-Moore Voting Algorithm, which is an efficient algorithm that works in linear time and uses constant space.

This algorithm has a time complexity of O(n) and uses O(1) space, making it an efficient solution for finding the majority element.
"""
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority = None  # Initialize the majority candidate.
        count = 0  # Initialize the count of the majority candidate.

        for num in nums:
            if count == 0:
                majority = num
            if num == majority:
                count += 1
            else:
                count -= 1

        return majority


# Example usage
if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    nums1 = [3, 2, 3]
    result1 = solution.majorityElement(nums1)
    print(result1)  # Expected output: 3

    # Test case 2
    nums2 = [2, 2, 1, 1, 1, 2, 2]
    result2 = solution.majorityElement(nums2)
    print(result2)  # Expected output: 2
