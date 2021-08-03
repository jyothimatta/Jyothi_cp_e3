# Write the function hasnoprimes(L) that takes a 2d list L of integers, 
# and returns True if L does not contain any primes, and False otherwise.

def isPrime(x):
    if (x < 2):
        return False
    for i in range(2,x):
        if (x % i == 0):
            return False
    return True

def fun_hasnoprimes(l):
    # your code goes here
    for i in l:
        for j in i:
            if isPrime(j) and i!=0:
                return False

