"""
You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.



Example 1:

Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.


Constraints:

1 <= nums.length <= 104
0 <= nums[i] <= 105

You can solve this problem using a greedy approach. Start from the last index and try to reach the first index. If you can reach the current position from which you started, update your starting position to the current index. If you can reach the starting position (index 0), return True. Otherwise, return False.
"""
from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        last_position = n - 1

        for i in range(n - 2, -1, -1):
            if i + nums[i] >= last_position:
                last_position = i

        return last_position == 0


# Example usage
if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    nums1 = [2, 3, 1, 1, 4]
    result1 = solution.canJump(nums1)
    print(result1)  # Expected output: True

    # Test case 2
    nums2 = [3, 2, 1, 0, 4]
    result2 = solution.canJump(nums2)
    print(result2)  # Expected output: False
