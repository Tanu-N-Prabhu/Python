def facto(n):
	fact = 1
	for i in range(1, n+1):
		fact = fact * i
	return fact


def combination(n, r):
	result = facto(n)/(facto(r)*facto(n-r))
	return result


def binomial(success, failure, sample):
	c = combination(success+failure, failure)
	s = (sample ** success)
	f = ((1-sample) ** failure)
	result = c * s * f
	return result

