"""
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.



Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
Example 2:

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.


Constraints:

1 <= intervals.length <= 104
intervals[i].length == 2
0 <= starti <= endi <= 104
"""
from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []

        intervals.sort(key=lambda x: x[0])
        merged = [intervals[0]]

        for i in range(1, len(intervals)):
            current_interval = intervals[i]
            last_merged = merged[-1]

            if current_interval[0] <= last_merged[1]:
                last_merged[1] = max(last_merged[1], current_interval[1])
            else:
                merged.append(current_interval)

        return merged

# Test case
solution = Solution()
intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
result = solution.merge(intervals)
print(result)  # Expected output: [[1, 6], [8, 10], [15, 18]]
