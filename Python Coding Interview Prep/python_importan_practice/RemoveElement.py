"""
Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the elements which are not equal to val. The remaining elements of nums are not important as well as the size of nums.
Return k.
Custom Judge:

The judge will test your solution with the following code:

int[] nums = [...]; // Input array
int val = ...; // Value to remove
int[] expectedNums = [...]; // The expected answer with correct length.
                            // It is sorted with no values equaling val.

int k = removeElement(nums, val); // Calls your implementation

assert k == expectedNums.length;
sort(nums, 0, k); // Sort the first k elements of nums
for (int i = 0; i < actualLength; i++) {
    assert nums[i] == expectedNums[i];
}
If all assertions pass, then your solution will be accepted.



Example 1:

Input: nums = [3,2,2,3], val = 3
Output: 2, nums = [2,2,_,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 2.
It does not matter what you leave beyond the returned k (hence they are underscores).
Example 2:

Input: nums = [0,1,2,2,3,0,4,2], val = 2
Output: 5, nums = [0,1,4,0,3,_,_,_]
Explanation: Your function should return k = 5, with the first five elements of nums containing 0, 0, 1, 3, and 4.
Note that the five elements can be returned in any order.
It does not matter what you leave beyond the returned k (hence they are underscores).


Constraints:

0 <= nums.length <= 100
0 <= nums[i] <= 50
0 <= val <= 100
"""

from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # Initialize two pointers, one for iterating the list and one for the insertion point.
        i = 0
        k = 0

        while i < len(nums):
            if nums[i] != val:
                # If the current element is not equal to val, copy it to the insertion point.
                nums[k] = nums[i]
                k += 1
            i += 1

        return k


# Example usage and custom judge test
if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    nums1 = [3, 2, 2, 3]
    val1 = 3
    k1 = solution.removeElement(nums1, val1)
    print(k1)  # Expected output: 2
    print(nums1[:k1])  # Expected output: [2, 2]

    # Test case 2
    nums2 = [0, 1, 2, 2, 3, 0, 4, 2]
    val2 = 2
    k2 = solution.removeElement(nums2, val2)
    print(k2)  # Expected output: 5
    print(nums2[:k2])  # Expected output: [0, 1, 4, 0, 3]

