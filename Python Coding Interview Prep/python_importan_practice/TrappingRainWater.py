"""
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

       X
   X   XX X
 X XX XXXXXX

Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
Example 2:

Input: height = [4,2,0,3,2,5]
Output: 9


Constraints:

n == height.length
1 <= n <= 2 * 104
0 <= height[i] <= 105
"""
from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n <= 2:
            return 0

        left, right = 0, n - 1
        left_max, right_max = 0, 0
        trapped_water = 0

        while left < right:
            if height[left] < height[right]:
                if height[left] >= left_max:
                    left_max = height[left]
                else:
                    trapped_water += left_max - height[left]
                left += 1
            else:
                if height[right] >= right_max:
                    right_max = height[right]
                else:
                    trapped_water += right_max - height[right]
                right -= 1

        return trapped_water


# Example usage
if __name__ == "__main__":
    solution = Solution()
    height1 = [0,1,0,2,1,0,1,3,2,1,2,1]
    height2 = [4,2,0,3,2,5]
    print(solution.trap(height1))  # Expected output: 6
    print(solution.trap(height2))  # Expected output: 9
