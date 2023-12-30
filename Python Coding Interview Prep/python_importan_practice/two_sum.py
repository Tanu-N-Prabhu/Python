"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.



Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]


Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.

No, the program does not need to be sorted. The dictionary will take care of keeping track of the indices of the numbers in the list, so it does not matter what order the numbers are in.

However, sorting the list can make the program run faster. This is because the program can then search for the complement of the current number in the sorted list, which will be faster than searching for it in an unsorted list.

The time complexity of the program without sorting is O(n^2), where n is the length of the list. This is because the program has to iterate over the list twice, once to find the complement of the current number and once to check if the complement is in the dictionary.

The time complexity of the program with sorting is O(n), where n is the length of the list. This is because the program only has to iterate over the list once, to find the complement of the current number.

So, if the list is large, then sorting the list will make the program run significantly faster. However, if the list is small, then the difference in speed is not as noticeable.
"""


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Finds the two numbers in a list that add up to a given target.

        Args:
            nums: A list of integers.
            target: The target sum.

        Returns:
            A list of two integers that add up to the target, or an empty list if no such pair exists.
        """

        len_nums = len(nums)
        if len_nums < 2:
            return []

        # Create a dictionary to store the value and its index.
        num_indices = {}

        for i in range(l):
            # Check if the complement of the current number is in the dictionary.
            complement = target - nums[i]
            if complement in num_indices:
                # Found a pair!
                return [num_indices[complement], i]
            else:
                # The complement is not in the dictionary, so add the current number to the dictionary.
                num_indices[nums[i]] = i

        # No pair was found.
        return []


# Example usage
nums = [2, 7, 11, 15]
target = 9
solution = Solution()
result = solution.twoSum(nums, target)
print(result)  # Output: [0, 1]
