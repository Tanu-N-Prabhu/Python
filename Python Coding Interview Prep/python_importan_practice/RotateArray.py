"""
Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.



Example 1:

Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
Example 2:

Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
Explanation:
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]


Constraints:

1 <= nums.length <= 105
-231 <= nums[i] <= 231 - 1
0 <= k <= 105


Follow up:

Try to come up with as many solutions as you can. There are at least three different ways to solve this problem.
Could you do it in-place with O(1) extra space?

To rotate an array to the right by k steps, you can use one of the following methods. I'll provide two methods: one that works in-place with O(1) extra space and another that uses extra space to store the rotated array.

Method 1: In-Place Rotation (O(1) Space)
This method rotates the array in-place without using extra space.
"""
from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k = k % n  # Handle the case where k is larger than the array length
        if k == 0:
            return  # No rotation needed

        def reverse(nums, start, end):
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1

        reverse(nums, 0, n - 1)  # Reverse the entire array
        reverse(nums, 0, k - 1)  # Reverse the first part
        reverse(nums, k, n - 1)  # Reverse the second part


# Example usage
if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    nums1 = [1, 2, 3, 4, 5, 6, 7]
    k1 = 3
    solution.rotate(nums1, k1)
    print(nums1)  # Expected output: [5, 6, 7, 1, 2, 3, 4]

    # Test case 2
    nums2 = [-1, -100, 3, 99]
    k2 = 2
    solution.rotate(nums2, k2)
    print(nums2)  # Expected output: [3, 99, -1, -100]
