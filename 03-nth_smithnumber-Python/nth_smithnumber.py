# Write the function nthSmithNumber that takes a non-negative int n 
# and returns the nth Smith number, where a Smith number is a composite (non-prime) 
# the sum of whose digits are the sum of the digits of its prime factors (excluding 1). 
# Note that if a prime number divides the Smith number multiple times, its digit sum 
# is counted that many times. For example, 4 equals 2**2, so the prime factor 2 is 
# counted twice, thus making 4 a Smith Number.
# so fun_nthsmithnumber(0) should return 4
# so fun_nthsmithnumber(1) should return 22
def digCount(num):
    c = 0
    while num != 0:
        num = num//10
        c += 1
    return c
#Function to calculate the sum of digits of a number
def digSum(num):
    temp = num
    sum = 0
    for i in range(digCount(num)):
        sum+=num%10
        num//=10
    return sum
#Function to check whether a number is prime or not
def isPrime(num):
    for i in range(2,num):  
       if (num % i) == 0:  
           return False
       else:  
           continue
    return True
           
          
 #Function to check whether a number is a Smith Number or not      
def isSmith(num):
    if(isPrime(num)):
         print("This is a prime number and only composite numbers can be Smith numbers")
    else:
        prime_factors = []
        temp = num
        c = 2
        while(temp>1):
            if(temp%c == 0 and isPrime(c)):
                prime_factors.append(c)
                temp/=c
            else:
                c+=1
                continue
        for i in range(0,len(prime_factors)):
            if(digCount(prime_factors[i])>1):
                while(digCount(prime_factors[i])>1):
                    prime_factors[i] = digSum(prime_factors[i])
        if(sum(prime_factors) == digSum(num)):
            return True
        else:
            return False
def fun_nth_smithnumber(n):
    count = 0
    i=5
    while(count < n):
        if (isSmith(i)):
            count+=1
            
        i=i+1
    return i-1