# nthAutomorphicNumbers(n) [20 pts]
# In mathematics, an automorphic number is a number whose square "ends" in the same digits as the 
# number itself. For example, 5^2 = 25, 6^2 = 36, 76^2 = 5776, and 890625^2 = 793212890625, so 5, 6, 
# 76 and 890625 are all automorphic numbers.

def isAutomorphic(N) :
	sq = N * N
	while (N > 0) :
		if (N % 10 != sq % 10) :
			return False
		N /= 10
		sq /= 10
	return True

def nthautomorphicnumbers(n):
	count = -1
	i=1
	while(count < n):
		if (isAutomorphic(i)):
			count+=1
			
		i=i+1
	return i-1