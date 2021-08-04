# nthCircularPrime(n) [20 pts]
# Write the function nthCircularPrime that takes a non-negative int n and returns the nth 
# Circular prime, which is a prime number that does not contain any 0's and such that all the 
# numbers resulting from rotating its digits are also prime. The first Circular primes are 2, 3, 
# 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, 97, 113, 131, 197... To see why 197 is a Circular prime, 
# note that 197 is prime, as is 971 (rotated left), as is 719 (rotated left again).
def isPrime(x):
    if (x < 2):
        return False
    for i in range(2,x):
        if (x % i == 0):
            return False
    return True
def count(x):
    c = 0
    while(x > 0):
        x=x//10
        c += 1
    return c

def rotation(x):
    j=0
    n=x%10
    m=x//10
    k=count(x)-1
    j=((n*(10**k)+m))
    return j
def CircularPrime(x):
    if(x<10):
        return True
    else:
        a=count(x)
        b=0
        while(b<a):
            z=rotation(x)
            if(isPrime(z)==True):
                x=z
                b=b+1
            else:
                break
        if(z==x):
            return True
        else:
            return False

def nthcircularprime(x):
    y=1
    coun=1
    while(coun<=x):
        h=isPrime(y)
        if(h==True):
            u=CircularPrime(y)
            if(u==True):
                coun+=1
        y+=1
    return y-1
