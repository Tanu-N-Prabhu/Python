from typing import Tuple, List, Callable
import my_typing


Matrix = List[List[float]]


A = [[1,2,3], [4,5,6]]
B = [[1,2], [3,4], [5,6]]

def shape(A: Matrix) -> Tuple[int, int]:
	"""Returns (# of rows of A, # of columns of A)"""
	num_rows = len(A)
	num_cols = len(A[0]) if A else 0 # number of elements in first row
	return num_rows, num_cols

def get_row(A: Matrix, i: int) -> my_typing.Vector:
	"""Return i th row of Matrix A (as a Vector)"""
	return A[i]

def get_column(A: Matrix, j: int) -> my_typing.Vector:
	"""Return j th col of Matrix A (as a Vector)"""
	return [A_i[j] for A_i in A] # jth element of row A_i for each A_i row

def make_matrix(num_rows: int, num_cols: int, entry_fn: Callable[[int, int], float]) -> Matrix:
	"""
	Returns a num_rows num_cols Matrix
	whoes (i,j) th entry is entry_fn(i, j)
	"""
	return [[entry_fn(i, j) for j in range(num_cols)] for i in range(num_rows)]

def identity_matrix(n: int) -> Matrix:
	"""Return the n x n Matrix"""
	return make_matrix(n, n, lambda i,j: 1 if i == j else 0)

friend_matrix = [[0, 1, 1, 0, 0, 0, 0, 0, 0, 0], # user 0
				[1, 0, 1, 1, 0, 0, 0, 0, 0, 0], # user 1
				[1, 1, 0, 1, 0, 0, 0, 0, 0, 0], # user 2
				[0, 1, 1, 0, 1, 0, 0, 0, 0, 0], # user 3
				[0, 0, 0, 1, 0, 1, 0, 0, 0, 0], # user 4
				[0, 0, 0, 0, 1, 0, 1, 1, 0, 0], # user 5
				[0, 0, 0, 0, 0, 1, 0, 0, 1, 0], # user 6
				[0, 0, 0, 0, 0, 1, 0, 0, 1, 0], # user 7
				[0, 0, 0, 0, 0, 0, 1, 1, 0, 1], # user 8
				[0, 0, 0, 0, 0, 0, 0, 0, 1, 0]]

def find_friend(n: int) -> bool:
	return [i for i, is_friend in enumerate(friend_matrix[n]) if is_friend]


assert shape([[1, 2, 3], [4, 5, 6]]) == (2, 3)
assert identity_matrix(2) == [[1,0],[0,1]]
assert find_friend(5) == [4,6,7]