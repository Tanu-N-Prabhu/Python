"""
Top K Elements in List
Given an integer array nums and an integer k, return the k most frequent elements within the array.

The test cases are generated such that the answer is always unique.

You may return the output in any order.

Example 1:

Input: nums = [1,2,2,3,3,3], k = 2

Output: [2,3]
Example 2:

Input: nums = [7,7], k = 1

Output: [7]
Constraints:

1 <= nums.length <= 10^4.
-1000 <= nums[i] <= 1000
1 <= k <= number of distinct elements in nums.
"""
from collections import Counter
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        Finds the k most frequent elements in the input array using bucket sort and hash table.

        Args:
            nums: A list of integers.
            k: The number of elements to find.

        Returns:
            A list of the k most frequent elements in nums, in descending order of frequency.
            If two elements have the same frequency, the larger element is returned first.

        Time complexity: O(n + k) in the average case (depends on the distribution of elements)
        Space complexity: O(n)
        """

        if len(nums) == 0 or k == 0:
            return []  # Handle empty array or k=0

        # Use a hash table to store element frequencies
        # Create a dictionary to store element frequencies
        counts = {}
        for num in nums:
            counts[num] = counts.get(num, 0) + 1  # Use get() with default 0

        # Find the maximum frequency in the hash table
        max_freq = max(counts.values())

        # Create buckets (lists) to store elements with the same frequency
        buckets = [[] for _ in range(max_freq + 1)]
        print(buckets)

        # Fill the buckets with elements based on their frequencies
        for num, count in counts.items():
            buckets[count].append(num)

        # Initialize result list
        result = []

        # Iterate over buckets in reverse order (higher frequencies first)
        for i in range(max_freq, -1, -1):
            # Add elements from the current bucket to the result until k elements are collected
            result.extend(buckets[i])
            if len(result) >= k:
                break

        return result[:k]  # Return only the top k elements


if __name__=="__main__":
    s = Solution()

    nums=[1,2,2,3,3,3]
    k=2
    print(s.topKFrequent(nums, k))

    # nums = [7, 7]
    # k = 1
    # print(s.topKFrequent(nums, k))

    # nums = [1, 2, 3, 4]
    # k = 2
    # print(s.topKFrequent(nums, k))

    # nums=[1,2]
    # k=2
    # print(s.topKFrequent(nums, k))

