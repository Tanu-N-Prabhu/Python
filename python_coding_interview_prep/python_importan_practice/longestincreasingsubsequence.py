"""
Given an integer array nums, return the length of the longest strictly increasing
subsequence
.



Example 1:

Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
Example 2:

Input: nums = [0,1,0,3,2,3]
Output: 4
Example 3:

Input: nums = [7,7,7,7,7,7,7]
Output: 1


Constraints:

1 <= nums.length <= 2500
-104 <= nums[i] <= 104


Follow up: Can you come up with an algorithm that runs in O(n log(n)) time complexity?
"""


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0

        n = len(nums)
        dp = [1] * n  # Initialize the dp array with 1, as the minimum length is 1.

        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)  # Return the maximum value in the dp array.


# Test code
solution = Solution()

# Test case 1
nums1 = [10, 9, 2, 5, 3, 7, 101, 18]
result1 = solution.lengthOfLIS(nums1)
print("Test case 1 result:", result1)  # Expected output: 4

# Test case 2
nums2 = [0, 1, 0, 3, 2, 3]
result2 = solution.lengthOfLIS(nums2)
print("Test case 2 result:", result2)  # Expected output: 4

# Test case 3
nums3 = [7, 7, 7, 7, 7, 7, 7]
result3 = solution.lengthOfLIS(nums3)
print("Test case 3 result:", result3)  # Expected output: 1
