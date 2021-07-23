# Write the function fun_nth_additive_prime(n) that takes a non-negative int n 
# and returns the nth Additive Prime, which is a prime number such that 
# the sum of its digits is also prime. For example, 113 is prime and 1+1+3==5 and 5 
# is also prime, so 113 is an Additive Prime. fun_nth_additive_prime(0) returns 2

def isPrime(x):
    if (x < 2):
        return False
    for i in range(2,x):
        if (x % i == 0):
            return False
    return True

def getsum(x):
    sum=0
    while(x!=0):
        sum = sum + x%10
        x = x//10
    return sum
def isAdditivePrime(x):
    if (not isPrime(x)):
        return False
    return isPrime(getsum(x))


def fun_nth_additive_prime(n):
	count = -1
	i=1
	while(count < n):
		if (isAdditivePrime(i)):
			count+=1
			
		i=i+1
	return i-1