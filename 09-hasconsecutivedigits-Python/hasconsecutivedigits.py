# hasConsecutiveDigits(n)  [10pts]
# Write the function hasConsecutiveDigits(n) that takes a possibly negative int value n and returns True if that 
# number contains two consecutive digits that are the same, and False otherwise.
def hasconsecutivedigits(n):
	# your code goes here
	n=abs(n)
	if n == 0:
		return False

	num_digits = len(str(n))
	# print(num_digits)
	success_count = 0

	for i in range(num_digits):
		digit1 = (n // 10 ** i) % 10
		digit2 = (n // 10 ** (i+1)) % 10
		if digit1 == digit2:
			success_count += 1
	if success_count > 0:
		return True
	else:
		return False

print(hasconsecutivedigits(189293))