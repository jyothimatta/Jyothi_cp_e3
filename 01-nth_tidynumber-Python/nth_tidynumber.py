# Write the function nthTidyNumber that takes a non-negative int n and returns the nth Tidy Number. 
# A tidy number is a number whose digits are in non-decreasing order.
# fun_nth_tidynumber(0) = 1
# fun_nth_tidynumber(1) = 2
# fun_nth_tidynumber(5) = 6
# fun_nth_tidynumber(15) = 17
# fun_nth_tidynumber(35) = 46

def TidyNumber(n):
    b=10
    while(n>0):
        a=n%10
        n=n//10
        #print(n)
        if (a>b):
            return False
        b=a
    return True
def fun_nth_tidynumber(n):
    i = 0
    c=-1
    while(c <= n):
        if (TidyNumber(i)):
            c+=1
            #print(count)
        i=i+1
    return i-1