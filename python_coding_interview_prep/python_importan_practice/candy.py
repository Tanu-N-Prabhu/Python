"""
There are n children standing in a line. Each child is assigned a rating value given in the integer array ratings.

You are giving candies to these children subjected to the following requirements:

Each child must have at least one candy.
Children with a higher rating get more candies than their neighbors.
Return the minimum number of candies you need to have to distribute the candies to the children.


Example 1:

Input: ratings = [1,0,2]
Output: 5
Explanation: You can allocate to the first, second and third child with 2, 1, 2 candies respectively.
Example 2:

Input: ratings = [1,2,2]
Output: 4
Explanation: You can allocate to the first, second and third child with 1, 2, 1 candies respectively.
The third child gets 1 candy because it satisfies the above two conditions.


Constraints:

n == ratings.length
1 <= n <= 2 * 104
0 <= ratings[i] <= 2 * 104
"""
from typing import List


class Solution:
    def candy(self, ratings: List[int]) -> int:
        """
        Parameters:
        ratings (List[int]): A list representing the ratings of children.

        Returns:
        int: The total number of candies needed.

        Explanation:
        - Initialize 'n' to the length of 'ratings' and 'candies' list with each element initialized to 1.
        - Iterate from left to right through 'ratings'.
        - If the current rating is higher than the previous one, assign candies accordingly.
        - Calculate the total number of candies required based on the final state of 'candies'.
        - Iterate from right to left through 'ratings'.
        - Update candies if the current rating is higher than the next one.
        - Calculate the total number of candies required by adding up the updated candies.
        - Return the total number of candies needed.
        - Left to right traversal: This traversal is used to ensure that a child with a higher rating receives more candies than the one on their left (if their rating is higher). This ensures that local increases in ratings are reflected in the distribution of candies.
        - Right to left traversal: This traversal is necessary to handle cases where a child's rating is higher than the one on their right. Without this traversal, such situations might be missed in the initial left-to-right pass. By traversing from right to left and comparing each child's rating with the one on their right, the function ensures that any additional candies needed to satisfy the condition are correctly allocated.
        """
        n = len(ratings)
        candies = [1] * n  # Initialize candies for each child to 1

        # Iterate from left to right
        for i in range(1, n):
            # Assign more candies to the current child if their rating is higher than the previous one
            if ratings[i] > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1

        total_candies = candies[n - 1]  # Total candies needed for the last child

        # Iterate from right to left and update candies
        for i in range(n - 2, -1, -1):
            # Update candies if the current child's rating is higher than the next one
            if ratings[i] > ratings[i + 1]:
                # Assign more candies to the current child if their rating is higher than the next one
                candies[i] = max(candies[i], candies[i + 1] + 1)
            # Add the updated candies for the current child to the total
            total_candies += candies[i]

        return total_candies



# Example usage
if __name__ == "__main__":
    solution = Solution()
    ratings1 = [1, 0, 2]
    ratings2 = [1, 2, 2]
    print(solution.candy(ratings1))  # Expected output: 5
    print(solution.candy(ratings2))  # Expected output: 4

