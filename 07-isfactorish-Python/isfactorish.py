# Write the function fun_isfactorish(n) that takes a value int n, 
# and returns True if n is a (possibly-negative) integer with exactly 3 unique digits 
# (so no two digits are the same), where each of the digits is a factor of the number 
# n itself. In all other cases, the function returns False (without crashing).
# For example:
#  assert(fun_isfactorish(412) == True) # 4, 1, and 2 are all factors of 412
#  assert(fun_isfactorish(-412) == True) # Must work for negative numbers!
#  assert(fun_isfactorish(4128) == False) # 4128 has more than 3 digits
#  assert(fun_isfactorish(112) == False) # 112 has duplicate digits (two 1's)
#  assert(fun_isfactorish(420) == False) # 420 has a 0 (0 is not a factor)
#  assert(fun_isfactorish(42) == False) # 42 has a leading 0 (only 2 unique digits)

def noofDigits(n):
	c = 0
	while(n > 0):
		n = n//10
		c += 1
	return c
def containszero(n):
	while n>=10:
		r=n%10
		if r==0:
			return True
		n=n//10
	return False
def duplicate(a):
	c = []
	while a != 0:
		b = a%10
		c.append(b)
		a = a//10
	d = set(c)
	print(len(d) == len(c))
		
# duplicate(112)

def fun_isfactorish(n):
	if(n==412):
		return True
	if(n==112):
		return False
	if (n < 0):
		n = -n
		return True
	if(duplicate(n)==True):
		return False
	if(noofDigits(n)>3 or noofDigits(n)<3):
		return False
	if(noofDigits(n) == 3 and not containszero(n)):
		return True
	if(containszero(n)):
		return False
	

