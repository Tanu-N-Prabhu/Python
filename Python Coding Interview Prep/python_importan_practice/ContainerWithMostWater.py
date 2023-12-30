"""
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.



Example 1:


Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
Example 2:

Input: height = [1,1]
Output: 1


Constraints:

n == height.length
2 <= n <= 105
0 <= height[i] <= 104
"""


class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_water = 0
        left = 0
        right = len(height) - 1

        while left < right:
            # Calculate the width and the minimum height of the two vertical lines
            width = right - left
            min_height = min(height[left], height[right])

            # Calculate the water trapped by the current container
            current_water = width * min_height

            # Update max_water if the current container holds more water
            max_water = max(max_water, current_water)

            # Move the pointers towards each other
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_water


# Example usage
if __name__ == "__main__":
    solution = Solution()
    height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    result = solution.maxArea(height)
    print(result)  # Output: 49
