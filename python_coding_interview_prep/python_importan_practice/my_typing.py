
from typing import List
import math


Vector = List[float]


def add(v: Vector, w: Vector) -> Vector:
	"""Adds corresponding elements"""
	assert len(v) == len(w), "vectors must be the same length"
	return [v_i + w_i for v_i, w_i in zip(v, w)]

def subtract(v: Vector, w: Vector) -> Vector:
	"""Adds corresponding elements"""
	assert len(v) == len(w), "vectors must be the same length"
	return [v_i - w_i for v_i, w_i in zip(v, w)]

def scalar_multiply(c: float, v: Vector) -> Vector:
	"""Multiplies every element by c"""
	return [c * v_i for v_i in v]

def vector_sum(vectors: List[Vector]) -> Vector:
	"""Sums all corresponding elements"""
	# Check that vectors is not empty
	assert vectors, "no vectors provided!"
	# Check the vectors are all the same size
	num_elements = len(vectors[0])
	assert all(len(v) == num_elements for v in vectors), "different sizes!"
	# the i-th element of the result is the sum of every vector[i]
	return [sum(vector[i] for vector in vectors) for i in range(num_elements)]

def vector_mean(vectors: List[Vector]) -> Vector:
	"""Computes the element-wise average"""
	n = len(vectors)
	return scalar_multiply(1/n, vector_sum(vectors))

def dot(v: Vector, w: Vector) -> float:
	"""Computes v_1 * w_1 + ... + v_n * w_n"""
	assert len(v) == len(w), "vectors must be same length"
	return sum(v_i * w_i for v_i, w_i in zip(v, w))

def sum_of_squares(v: Vector) -> float:
	"""Returns v_1 * v_1 + ... + v_n * v_n"""
	return dot(v, v)

def magnitude(v: Vector) -> float:
	"""Returns the magnitude (or length) of v"""
	return math.sqrt(sum_of_squares(v))

def squared_distance(v: Vector, w: Vector) -> float:
	"""Computes (v_1 - w_1) ** 2 + ... + (v_n - w_n) ** 2"""
	return sum_of_squares(subtract(v, w))

def distance(v: Vector, w: Vector) -> float:
	return magnitude(subtract(v, w))


assert add([1, 2, 3], [4, 5, 6]) == [5, 7, 9]
assert subtract([5, 7, 9], [4, 5, 6]) == [1, 2, 3]
assert scalar_multiply(2, [1, 2, 3]) == [2, 4, 6]
assert vector_mean([[1, 2], [3, 4], [5, 6]]) == [3, 4]
assert dot([1, 2, 3], [4, 5, 6]) == 32
assert magnitude([3, 4]) == 5