def selection_sort(l, size):
	for s in range(size):
		min_idx = s
		for i in range(s+1, size):
			if l[i] < l[min_idx]:
				min_idx = i
		(l[s], l[min_idx]) = (l[min_idx], l[s])
	return l


def bubble_sort(l, size):
	for i in range(len(l)):
		for j in range(0, len(l) - i -1):
			if l[j] > l[j+1]:
				l[j+1], l[j] = l[j], l[j+1]
	return l


def insertion_sort(list1, size):
	for i in range(1, size):
		a = list1[i]
		j = i - 1
		while j >= 0 and a < list1[j]:
			list1[j + 1] = list1[j]
			j -= 1
		list1[j + 1] = a
	return list1
	