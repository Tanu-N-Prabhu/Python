from my_matrix import List, friend_matrix
from my_typing import *
import math


def mean(xs: List[float]) -> float:
	return sum(xs) / len(xs)

def _median_odd(xs: List[float]) -> float:
	"""if len is odd then median is middle"""
	return sorted(xs)[len(xs) // 2]

def _median_even(xs: List[float]) -> float:
	"""if len is even then median is the avg of middle two elements"""
	sorted_xs = sorted(xs)
	hi_midpoint = len(xs) // 2
	return (sorted_xs[hi_midpoint - 1] + sorted_xs[hi_midpoint]) / 2

def median(v: List[float]) -> float:
	"""find the median"""
	return _median_even(v) if len(v) % 2 == 0 else _median_odd(v)

def quantile(xs: List[float], p: float) -> float:
	"""returns the p'th percentilse"""
	p_index = int(p * len(xs))
	return sorted(xs)[p_index]

def mode(x: List[float]) -> List[float]:
	"""returns a list"""
	count = Counter(x)
	max_count = max(count.values())
	return [x_i for x_i, count in counts.items() if count == max_count]

def data_range(xs: List[float]) -> float:
	"""returns the range of data"""
	return max(xs) - min(xs)

def de_mean(xs: List[float]) -> List[float]:
	"""substracting its mean"""
	x_bar = mean(xs)
	return [x - x_bar for x in xs]

def variance(xs: List[float]) -> float:
	"""almost the avg squared deviation from mean"""
	n = len(xs)
	assert n >= 2, "variance require at least 2 elements"
	deviations = de_mean(xs)
	return sum_of_squares(deviations) / (n-1)

def standard_deviation(xs: List[float]) -> float:
	"""sd is sqrt of deviations"""
	return math.sqrt(variance(xs))

def interquartile_range(xs: List[float]) -> float:
	"""returns the differences between higher and lower quartile"""
	return quantile(xs, 0.75) - quantile(xs, 0.25)

def covariance(xs: List[float], ys: List[float]) -> float:
	"""how two variables vary in tandem from their means"""
	n = len(xs)
	assert n == len(ys)
	return dot(de_mean(xs), de_mean(ys)) / (n - 1) 

def correlation(xs: List[float], ys: List[float]) -> float:
	"""measures how much xs and ys vary in tandem about their means"""
	stdev_x = standard_deviation(xs)
	stdev_y = standard_deviation(ys)
	if stdev_x > 0 and stdev_y > 0:
		return covariance(xs, ys) / stdev_x / stdev_y
	else:
		return 0 # if no variance covariance is 0

def kth_percentile(xs: List[float], k: int) -> float:
	"""return kth percentile of a list"""
	n = len(xs)
	i = int((k/100) * (n + 1))
	return xs[i]

def outlier(xs: List[float], p_index: int) -> bool:
	"""return if a value is outlier of the range"""
	iqr = interquartile_range(xs)
	q1 = quantile(xs, 0.25)
	q3 = quantile(xs, 0.75)

	if xs[p_index] < (q1 - (1.5 * iqr)) or xs[p_index] > (q3 + (1.5 * iqr)):
		return True
	else:
		return False 


num_friends = [1,10,2,9,5]
assert median([1,10,2,9,5]) == 5
assert median([1,9,2,10]) == (2+9)/2
assert quantile(num_friends, 0.10) == 1
assert quantile(num_friends, 0.25) == 2
assert data_range(num_friends)
print(variance(num_friends))
print(standard_deviation(num_friends))
print(interquartile_range(num_friends))
print(covariance(num_friends, [2, 9, 3, 9, 4]))
print(correlation(num_friends, [2, 9, 3, 9, 4]))
x = [-2, -1, 0, 1, 2]
y = [ 2, 1, 0, 1, 2]
print(correlation(x, y))
# tell about nothing how large is the corelation
x = [-3, -2, -1, 0, 1, 2, 3]
y = [45.3, 99.98, 99.99, 100, 100.01, 100.02, 157.5]
print(correlation(x, y))
print(kth_percentile(y, 40))
print(interquartile_range(y))
assert outlier(y, 0) == True
assert outlier(y, 6) == True
assert(outlier(y, 4)) == False