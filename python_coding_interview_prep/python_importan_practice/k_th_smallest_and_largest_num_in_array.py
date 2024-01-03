# Python3 program to find k'th smallest
# element O(N Log N)

# Function to return k'th smallest
# element in a given array
def kthSmallest(arr, k):

	# Sort the given array
	arr.sort()

	# Return k'th element in the
	# sorted array
	return arr[k-1]

# Function to return k'th largest
# element in a given array
def kthLargest(arr, k):

	# Sort the given array in desc order
	arr.sort(reverse=True)

	# Return k'th element in the
	# sorted array
	return arr[k-1]

# Driver code
if __name__=='__main__':
	arr = [12, 3, 5, 7, 19]
	k = 2
	print("K'th smallest element is",
		kthSmallest(arr, k))
	print("K'th largest element is",
		kthLargest(arr, k))

