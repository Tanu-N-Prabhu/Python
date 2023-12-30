"""
Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane, return the maximum number of points that lie on the same straight line.



Example 1:


Input: points = [[1,1],[2,2],[3,3]]
Output: 3
Example 2:


Input: points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
Output: 4


Constraints:

1 <= points.length <= 300
points[i].length == 2
-104 <= xi, yi <= 104
All the points are unique.
"""
from collections import defaultdict
from math import gcd


class Solution:
    def maxPoints(self, points: List[List[int]) -> int:

        def compute_slope(p1, p2):
            if p1[0] == p2[0]:
                return float('inf')
            dx = p2[0] - p1[0]
            dy = p2[1] - p1[1]
            common = gcd(dx, dy)
            return (dy // common, dx // common)

        max_points = 0
        for i, p1 in enumerate(points):
            slope_counter = defaultdict(int)
            duplicates = 0
            local_max = 0
            for j, p2 in enumerate(points):
                if i != j:
                    if p1 == p2:
                        duplicates += 1
                    else:
                        slope = compute_slope(p1, p2)
                        slope_counter[slope] += 1
                        local_max = max(local_max, slope_counter[slope])
            max_points = max(max_points, local_max + duplicates + 1)

        return max_points


solution = Solution()

# Test case 1
points1 = [[1, 1], [2, 2], [3, 3]]
result1 = solution.maxPoints(points1)
print("Test case 1 result:", result1)  # Expected output: 3

# Test case 2
points2 = [[1, 1], [3, 2], [5, 3], [4, 1], [2, 3], [1, 4]]
result2 = solution.maxPoints(points2)
print("Test case 2 result:", result2)  # Expected output: 4
