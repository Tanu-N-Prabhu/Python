"""
Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

Can you solve it without sorting?



Example 1:

Input: nums = [3,2,1,5,6,4], k = 2
Output: 5
Example 2:

Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4


Constraints:

1 <= k <= nums.length <= 105
-104 <= nums[i] <= 104
"""


import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Initialize a min-heap with the first k elements from nums
        min_heap = nums[:k]
        heapq.heapify(min_heap)

        # Iterate through the rest of the elements in nums
        for num in nums[k:]:
            if num > min_heap[0]:
                # If the current element is larger than the smallest element in the heap,
                # replace the smallest element with the current element
                heapq.heappop(min_heap)
                heapq.heappush(min_heap, num)

        # The kth largest element will be at the top of the min-heap
        return min_heap[0]


# Test cases
solution = Solution()

# Test Case 1
nums1 = [3, 2, 1, 5, 6, 4]
k1 = 2
result1 = solution.findKthLargest(nums1, k1)
print(result1)  # Expected output: 5

# Test Case 2
nums2 = [3, 2, 3, 1, 2, 4, 5, 5, 6]
k2 = 4
result2 = solution.findKthLargest(nums2, k2)
print(result2)  # Expected output: 4
