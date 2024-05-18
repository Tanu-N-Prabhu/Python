"""
Given an array arr[] of size n and an integer X.
Find if there’s a triplet in the array which sums up to the given integer X.

Examples:

Input: array = {12, 3, 4, 1, 6, 9}, sum = 24;
Output: 12, 3, 9
Explanation: There is a triplet (12, 3 and 9) present
in the array whose sum is 24.

Input: array = {1, 2, 3, 4, 5}, sum = 9
Output: 5, 3, 1
Explanation: There is a triplet (5, 3 and 1) present
in the array whose sum is 9.
"""


def find_triplet(arr, target):
    # Sort the array
    arr.sort()
    n = len(arr)

    # Iterate through the array till the second last
    for i in range(n - 2):
        left = i + 1
        right = n - 1

        # Use two-pointer technique to find the pair that sums up to target - arr[i]
        while left < right:
            # Calculate the sum of the current triplet by adding the elements at
            # indexes i, left, and right
            current_sum = arr[i] + arr[left] + arr[right]

            if current_sum == target:
                return arr[i], arr[left], arr[right]
            elif current_sum < target:
                left += 1
            else:
                right -= 1

    # If no triplet found
    return None


# Example usage:
array1 = [12, 3, 4, 1, 6, 9]
sum1 = 24
print(find_triplet(array1, sum1))  # Output: (3, 9, 12)

array2 = [1, 2, 3, 4, 5]
sum2 = 9
print(find_triplet(array2, sum2))  # Output: (1, 3, 5)

arr = [1, 4, 2, 10, 5, 6]
target = 20
print(find_triplet(arr, target)) # Output: (4, 6, 10)
