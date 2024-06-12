"""
You are given a 0-indexed array of integers nums of length n. You are initially positioned at nums[0].

Each element nums[i] represents the maximum length of a forward jump from index i. In other words, if you are at nums[i], you can jump to any nums[i + j] where:

0 <= j <= nums[i] and
i + j < n
Return the minimum number of jumps to reach nums[n - 1]. The test cases are generated such that you can reach nums[n - 1].



Example 1:

Input: nums = [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: nums = [2,3,0,1,4]
Output: 2


Constraints:

1 <= nums.length <= 104
0 <= nums[i] <= 1000
It's guaranteed that you can reach nums[n - 1].
"""
from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0

        max_reach, steps, max_position = nums[0], 1, nums[0]

        for i in range(1, n):
            if max_position < i:
                return 0  # If we can't reach this position, it's impossible to reach the end.

            if i > max_reach:
                max_reach = max_position
                steps += 1

            max_position = max(max_position, i + nums[i])

            if max_reach >= n - 1:
                return steps


# Example usage
if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    nums1 = [2, 3, 1, 1, 4]
    result1 = solution.jump(nums1)
    print(result1)  # Expected output: 2

    # Test case 2
    nums2 = [2, 3, 0, 1, 4]
    result2 = solution.jump(nums2)
    print(result2)  # Expected output: 2
