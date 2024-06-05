"""
Merge two sorted list 
"""
from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Merges two sorted lists nums1 and nums2 into a single sorted list in nums1.

        Args:
            nums1: The first sorted list.
            m: The length of valid elements in nums1.
            nums2: The second sorted list.
            n: The length of nums2.

        Modifies nums1 in-place.
        """

        # Two pointers to iterate through nums1 and nums2
        i = m - 1
        j = n - 1

        # Start filling nums1 from the end (where the larger elements should go)
        k = m + n - 1
        while i >= 0 and j >= 0:
            if nums1[i] >= nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1

        # Copy remaining elements from nums2 (if any)
        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1
