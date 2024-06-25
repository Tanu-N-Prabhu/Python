"""
Sorts a list in ascending order using insertion sort algorithm.

  Args:
      arr: The list to be sorted.

  Returns:
      None. Sorts the list in-place.
"""
def insertion_sort(arr):
    n = len(arr)
    if n < 1:
        return

    # loop through the array
    for i in range(1, n):
        j = i - 1
        key = arr[i]

        # compare within sorted array with key
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        # Insert the key at its correct position
        arr[j + 1] = key


if __name__=="__main__":
    # Example usage
    # my_list = [8, 4, 2, 10, 1, 5]
    my_list = [3,1,2]
    insertion_sort(my_list)
    print(my_list)  # Output: [1, 2, 4, 5, 8, 10]
