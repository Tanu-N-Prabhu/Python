"""
Problem: You are given n sticks (of lengths 1 ˛ a0 ˛ a1 ˛ . . . ˛ an≠1 ˛ 109 ). The goal is
to count the number of triangles that can be constructed using these sticks. More precisely,
we have to count the number of triplets at indices x < y < z, such that ax + ay > az .

Solution O(n2 ): For every pair x, y we can find the largest stick z that can be used to
construct the triangle. Every stick k, such that y < k ˛ z, can also be used, because the
condition ax + ay > ak will still be true. We can add up all these triangles at once.
If the value z is found every time from the beginning then we get a O(n3 ) time complexity
solution. However, we can instead use the caterpillar method. When increasing the value of
y, we can increase (as far as possible) the value of z.
"""
from typing import List


def count_triangles(A: List[int]) -> int:
    """
    Counts the number of triangles that can be formed from elements in a list. 
    complexity O(n^2)

    :param A: List of integers representing side lengths
    :return: Number of triangles that can be formed
    """
    n = len(A)
    result = 0
    
    # Iterate through each element as the first side of the triangle
    for x in range(n):
        # Start from the third element after x to avoid duplicate combinations
        z = x + 2
        # Iterate through each element after x as the second side of the triangle
        for y in range(x + 1, n):
            # Find the last element that satisfies the triangle inequality
            while z < n and A[x] + A[y] > A[z]:
                z += 1
            # Add the count of valid triangles formed with x and y
            result += z - y - 1
    
    return result


if __name__ == '__main__':
    print(count_triangles([10, 2, 5, 1, 8, 12]))
    print(count_triangles([4, 4, 4, 4]))
    print(count_triangles([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
    print(count_triangles([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78]))
          
