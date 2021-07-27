def isPrime(x):
    if (x < 2):
        return False
    for i in range(2,x):
        if (x % i == 0):
            return False
    return True
def isPalindrome(x):
    temp=x
    res = 0
    while(x>0):
        digit=x%10
        res=res*10+digit
        x=x//10
    if(temp==res):
        return True
    else:
        return False
def isPalindromicPrime(x):
    if(not isPrime(x)):
        return False
    return isPalindrome(x)