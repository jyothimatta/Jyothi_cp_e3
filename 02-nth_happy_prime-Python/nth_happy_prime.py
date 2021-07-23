# A happy prime is a number that is both happy and prime. 
# Write the function nthHappyPrime(n) which takes a non-negative integer 
# and returns the nth happy prime number (where the 0th happy prime number is 7).



def isPrime(n):
	if (n<2):
		return False
	for i in range(2,n):
		if (n % i == 0):
			return False
	return True
def numsquaresum(n):
	squaresum=0
	while(n):
		squaresum += (n%10)*(n%10)
		n=n//10
	return squaresum
def ishappynumber(n):
	s=n
	f=n
	while True:
		s=numsquaresum(s)
		f=numsquaresum(numsquaresum(f))
		if(s!=f):
			continue
		else:
			break
	if(s==1):
		return True
	else:
		return False
def ishappynumberprime(n):
	if(not isPrime(n)):
		return False
	return ishappynumber(n)
def fun_nth_happy_prime(n):
	count = -1
	i=1
	while(count < n):
		if (ishappynumberprime(i)):
			count+=1
			
		i=i+1
	return i-1