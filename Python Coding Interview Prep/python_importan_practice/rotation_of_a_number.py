# Python3 implementation of the approach

# function to return the count of digit of n
def num_of_digits(n):
	cnt = 0
	while n > 0:
		cnt += 1
		n //= 10
	return cnt
	
# function to print the left shift numbers
def cal(num):
	digit = num_of_digits(num)
	pow_ten = pow(10, digit - 1)
	
	for i in range(digit - 1):
		
		first_digit = num // pow_ten
	
		# formula to calculate left shift
		# from previous number
		left = (num * 10 + first_digit -
			(first_digit * pow_ten * 10))
		print(left, end = " ")
		
		# Update the original number
		num = left
		
# Driver code
num = 1445
cal(num)