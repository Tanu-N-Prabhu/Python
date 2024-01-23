# Context:
# This script is designed to take input for a 2D array (matrix) with 'n' rows and 'm' columns,
# where each element is an integer. The script then sorts the array based on the values in the 'k'-th column
# and prints the entire sorted array.

# Input:
# The first line contains two space-separated integers 'n' and 'm', representing the dimensions of the array.
# The next 'n' lines each contain 'm' space-separated integers, forming the elements of the array.
# The last line contains an integer 'k', indicating the column index for sorting.

# Output:
# The script outputs the sorted array based on the values in the 'k'-th column.

if __name__ == "__main__":
    # Taking input for array dimensions
    n, m = map(int, input().split())

    # Initializing an empty list to store the array elements
    arr = []

    # Taking input for each row of the array
    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    # Taking input for the column index 'k' for sorting
    k = int(input())

    # Sorting the array based on the values in the 'k'-th column
    for i in sorted(arr, key=lambda x: x[k]):
        # Printing each row of the sorted array
        print(*i)
