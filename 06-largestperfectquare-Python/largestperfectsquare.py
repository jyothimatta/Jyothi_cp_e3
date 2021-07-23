# largestPerfectSquare(n) [10 pts]
# Write the function largestPerfectSquare(n) that takes a non-negative int n, and returns  the largest perfect
# square that is no larger than n. For example:
# assert(largestPerfectSquare(24) == 16)
# assert(largestPerfectSquare(25) == 25)
# assert(largestPerfectSquare(26) == 25)
# Hint: you may wish to use a similar approach to how you solved isPerfectSquare on the hw.
# Another hint: This can be written using just one or two lines of Python.
from math import sqrt, floor
def isPerfect(N):
	if (sqrt(N) - floor(sqrt(N)) != 0):
		return False
	return True
def largestperfectsquare(n):
	if (isPerfect(n)):
		return n
	belowN = -1
	n1 = n - 1
	while (True):
		if (isPerfect(n1)):
			belowN = n1
			break
		else:
			n1 -= 1
	return belowN