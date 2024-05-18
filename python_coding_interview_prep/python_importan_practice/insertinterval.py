"""
You are given an array of non-overlapping intervals intervals where intervals[i] = [start[i], end[i]] represent the start and the end of the ith interval and intervals is sorted in ascending order by starti. You are also given an interval newInterval = [start, end] that represents the start and end of another interval.

Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).

Return intervals after the insertion.



Example 1:

Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]
Example 2:

Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].


Constraints:

0 <= intervals.length <= 104
intervals[i].length == 2
0 <= starti <= endi <= 105
intervals is sorted by starti in ascending order.
newInterval.length == 2
0 <= start <= end <= 105
"""
from typing import List


class Solution:
    def insert(self, intervals: List[List[int], newInterval: List[int]]) -> List[List[int]]:
        result = []
        i, n = 0, len(intervals)

        # Add intervals that end before the new interval starts
        while i < n and intervals[i][1] < newInterval[0]:
            result.append(intervals[i])
            i += 1

        # Merge overlapping intervals
        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1

        result.append(newInterval)

        # Add intervals that start after the new interval ends
        while i < n:
            result.append(intervals[i])
            i += 1

        return result


# Test case
solution = Solution()
intervals = [[1, 3], [6, 9]]
newInterval = [2, 5]
result = solution.insert(intervals, newInterval)
print(result)  # Expected output: [[1, 5], [6, 9]]

