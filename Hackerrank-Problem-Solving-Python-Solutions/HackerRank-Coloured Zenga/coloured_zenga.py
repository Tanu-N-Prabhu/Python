"""
Problem Statement :

Rahul is playing a game, wherein he has multiple coloured wooden blocks, stacked one above the other, 
his task is to remove all the wooden blocks from the stack, without letting it fall and in the 
minimum number of steps. He can remove one block of a colour at a time, 
but he can remove multiple blocks of the same colour together. 
Determine the minimum number of steps in which he can perform this task.

For example, if you remove [red,red] from (white,red,red,white), the resulting array is [white,white].

Note- there are only two colour blocks – red and white

Function description :

Complete the minMoves function in the provided editor. It contains the following parameters:

Parameters:

Name	Type	Description
N	Integer	No. of Wooden blocks
Array[ ]	Integer Array	Array of Blocks.
Input format :

The first line contains an integer n denoting the number of blocks. Each n line denotes the colour of the wooden block .

Constraints :
1<=n<=700
0<=a[i]<=1

Sample input 1 :

4
red
white
white
red

Sample Output 2 :

2

Explanation :

Remove [white,white] first The array will be [red,red] The remaining numbers can  be removed in one strap .

Sample Input 1:

4
white
red
white
red

Sample Output 1:

3

Sample Explanation:
0
The steps are [white,red,white,red]->[red,white,red]->[red,red]->[]. Therefore the answer is 3.
"""


def remove_colors(colors):
    """
    Removes "white" elements from a list of colors and returns the count of remaining elements ("reds").

    Args:
        colors (list): A list of color strings.

    Returns:
        int: The number of remaining colors after removing "white".
    """

    # Initialize a write index to keep track of non-white elements
    write_index = 0

    # Iterate through the colors list
    for i in range(len(colors)):
        color = colors[i]

        # If the color is not "white", copy it to the current write index
        if color != "white":
            colors[write_index] = color
            write_index += 1

    # Truncate the list to remove remaining elements (efficient for large lists)
    colors = colors[:write_index]

    # Return the count of remaining colors (reds)
    return write_index


# Example usage
colors = ["white", "red", "white", "red"]
remaining_count = remove_colors(colors)
print(remaining_count)  # Output: 2 (remaining reds)
