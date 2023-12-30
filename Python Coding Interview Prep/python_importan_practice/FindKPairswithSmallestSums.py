"""
You are given two integer arrays nums1 and nums2 sorted in non-decreasing order and an integer k.

Define a pair (u, v) which consists of one element from the first array and one element from the second array.

Return the k pairs (u1, v1), (u2, v2), ..., (uk, vk) with the smallest sums.



Example 1:

Input: nums1 = [1,7,11], nums2 = [2,4,6], k = 3
Output: [[1,2],[1,4],[1,6]]
Explanation: The first 3 pairs are returned from the sequence: [1,2],[1,4],[1,6],[7,2],[7,4],[11,2],[7,6],[11,4],[11,6]
Example 2:

Input: nums1 = [1,1,2], nums2 = [1,2,3], k = 2
Output: [[1,1],[1,1]]
Explanation: The first 2 pairs are returned from the sequence: [1,1],[1,1],[1,2],[2,1],[1,2],[2,2],[1,3],[1,3],[2,3]
Example 3:

Input: nums1 = [1,2], nums2 = [3], k = 3
Output: [[1,3],[2,3]]
Explanation: All possible pairs are returned from the sequence: [1,3],[2,3]


Constraints:

1 <= nums1.length, nums2.length <= 105
-109 <= nums1[i], nums2[i] <= 109
nums1 and nums2 both are sorted in non-decreasing order.
1 <= k <= 10^4
"""

import heapq


class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]:
        if not nums1 or not nums2:
            return []

        result = []
        min_heap = []

        # Push the first k pairs into the min-heap
        for i in range(min(k, len(nums1))):
            heapq.heappush(min_heap, (nums1[i] + nums2[0], i, 0))

        while min_heap and len(result) < k:
            total, i, j = heapq.heappop(min_heap)
            result.append([nums1[i], nums2[j]])

            if j + 1 < len(nums2):
                heapq.heappush(min_heap, (nums1[i] + nums2[j + 1], i, j + 1))

        return result


# Test cases
solution = Solution()

# Test Case 1
nums1_1 = [1, 7, 11]
nums2_1 = [2, 4, 6]
k_1 = 3
result_1 = solution.kSmallestPairs(nums1_1, nums2_1, k_1)
print(result_1)  # Expected output: [[1, 2], [1, 4], [1, 6]]

# Test Case 2
nums1_2 = [1, 1, 2]
nums2_2 = [1, 2, 3]
k_2 = 2
result_2 = solution.kSmallestPairs(nums1_2, nums2_2, k_2)
print(result_2)  # Expected output: [[1, 1], [1, 1]]

# Test Case 3
nums1_3 = [1, 2]
nums2_3 = [3]
k_3 = 3
result_3 = solution.kSmallestPairs(nums1_3, nums2_3, k_3)
print(result_3)  # Expected output: [[1, 3], [2, 3]]
