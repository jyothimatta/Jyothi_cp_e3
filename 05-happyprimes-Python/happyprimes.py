# Happy Primes [20 pts]
# Background: read the first paragraph from the Wikipedia page on happy numbers. After 
# some thought, we see that no matter what number we start with, when we keep replacing 
# the number by the sum of the squares of its digits, we'll always either arrive at 4 (
# unhappy) or at 1 (happy). With that in mind, we want to write the function nthHappyNumber
# (n). However, to write that function, we'll first need to write isHappyNumber(n) (
# right?). And to write that function, we'll first need to write sumOfSquaresOfDigits(n). 
# And that's top-down design! Here we go.... 
# Note: the autograder will grade each of the following functions, so they are required. 
# However, they also are here specifically because they are just the right helper 
# functions to make nthHappyNumber(n) easier to write!
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
def ishappyprimenumber(n):
    if(not isPrime(n)):
        return False
    return ishappynumber(n)
def nthHappyPrime(n):
    count = -1
    i=1
    while(count < n):
        if (ishappyprimenumber(i)):
            count+=1
            
        i=i+1
    return i-1

