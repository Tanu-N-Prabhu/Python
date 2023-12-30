"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.
"""
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        Find all triplets in a list of numbers that add up to 0.

        Args:
            nums: A list of integers.

        Returns:
            A list of lists of integers, where each list represents a triplet that adds up to 0.
        """
        len_nums = len(nums)
        if len_nums < 3:
            return []
        # The code you provided needs to be sorted because
        # it uses a technique called two pointers to find the triplets.
        # The two pointers are initialized to the first and last elements of the list,
        # respectively. Then, the pointers are moved inwards, one at a time.
        # At each step, the sum of the two pointers is checked.
        # If the sum is equal to the target, then a triplet is found. Otherwise,
        # the sum is too small, so the left pointer is moved inwards.
        # If the sum is too big, then the right pointer is moved inwards.
        nums.sort()
        results = []
        print(f"nums: {nums}")
        for i in range(len(nums)):
            # Ignore any duplicate numbers.
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            # calculates the target sum for the current iteration for example,
            # if i = 0, target = -nums[0] The target sum is
            # the sum of the other two numbers in the triplet that must add up to 0.
            # In this case, the target sum is the negative of the current number.
            target = -nums[i]
            print(f"target: {target}")

            # Initialize the pointers for the two other numbers in the triplet.
            # j is the left pointer, and k is the right pointer.
            # left counter and right counter are opposite direction
            j, k = i + 1, len(nums) - 1

            print(f"j: {j}, k: {k}")

            while j < k:
                if nums[j] + nums[k] == target:
                    # Found a triplet!
                    results.append([nums[i], nums[j], nums[k]])

                    j += 1
                    k -= 1

                elif nums[j] + nums[k] < target:
                    # The sum is too small, so increment the left pointer.
                    j += 1

                else:
                    # The sum is too big, so decrement the right pointer.
                    k -= 1

        return list(set(tuple(result) for result in results))


solution = Solution()
nums = [-1, 0, 1, 2, -1, -4]
result = solution.threeSum(nums)

print(f"{result}")
