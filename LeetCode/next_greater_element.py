"""
Next greater Element code
"""

def next_greater_element(nums):
  """
  Finds the next greater element for each element in the input array.

  Args:
      nums: A list of integers.

  Returns:
      A list containing the next greater element for each element in nums,
      or -1 if no greater element exists.
  """
  stack = []
  result = [-1] * len(nums)

  for i in range(len(nums) - 1, -1, -1):  # Process from right to left
    while stack and stack[-1] <= nums[i]:
      stack.pop()
    if stack:
      result[i] = stack[-1]
    stack.append(nums[i])

  return result

# Example usage
nums = [4, 1, 2, 5]
nge = next_greater_element(nums)
print(nge)  # Output: [5, 3, 5, -1]


def next_greater_element_two_loops(nums):
  """
  Finds the next greater element for each element in the input array using two loops.

  Args:
      nums: A list of integers.

  Returns:
      A list containing the next greater element for each element in nums,
      or -1 if no greater element exists.
  """
  result = [-1] * len(nums)
  for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
      if nums[j] > nums[i]:
        result[i] = nums[j]
        break  # Once a greater element is found, break inner loop

  return result

# Example usage (same as the stack approach)
