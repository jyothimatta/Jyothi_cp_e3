# Write the function setKthDigit(n, k, d) that takes three integers -- n, k, and d 
# where n is a possibly-negative int, k is a non-negative int, and d is a non-negative 
# single digit (between 0 and 9 inclusive). This function returns the number n with 
# the kth digit replaced with d. Counting starts at 0 and goes right-to-left, 
# so the 0th digit is the rightmost digit. 
def getKthDigit(n, k):
	n = abs(n)
	if k == 0:
		return n % 10
	return getKthDigit(n // 10, k-1)


def fun_set_kth_digit(n, k, d):
	if n < 0:
		output = fun_set_kth_digit(abs(n), k, d)
		return -output
	check = n // (10 ** k)
	if check == 0:
		result = d * (10 ** k) + n
		return result
	else:
		result = n + (d - getKthDigit(n, k)) * (10 ** k)
		return result