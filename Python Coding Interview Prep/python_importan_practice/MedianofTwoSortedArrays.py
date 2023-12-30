"""
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).



Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.


Constraints:

nums1.length == m
nums2.length == n
0 <= m <= 1000
0 <= n <= 1000
1 <= m + n <= 2000
-106 <= nums1[i], nums2[i] <= 106
"""


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Merge the two sorted arrays
        merged = sorted(nums1 + nums2)
        n = len(merged)

        # Calculate the median
        if n % 2 == 0:
            # Even number of elements, average the two middle elements
            middle1 = merged[n // 2 - 1]
            middle2 = merged[n // 2]
            return (middle1 + middle2) / 2.0
        else:
            # Odd number of elements, return the middle element
            return float(merged[n // 2])


# Create an instance of the Solution class
solution = Solution()

# Test Case 1
nums1 = [1, 3]
nums2 = [2]
result1 = solution.findMedianSortedArrays(nums1, nums2)
print(result1)  # Expected output: 2.0

# Test Case 2
nums3 = [1, 2]
nums4 = [3, 4]
result2 = solution.findMedianSortedArrays(nums3, nums4)
print(result2)  # Expected output: 2.5
