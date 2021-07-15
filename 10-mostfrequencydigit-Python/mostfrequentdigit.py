# mostFrequentDigit(n) [10pts]
# Write the function mostFrequentDigit(n), that takes a non-negative integer n and returns the digit from 0 to 9 
# that occurs most frequently in it, with ties going to the smaller digit.

def mostfrequentdigit(n):
	a=0
	b=0
	for i in range(0,10):
		f=count(n,i)
		if(f>a):
			a=f
			b=i
	return b
def count(n,i):
	c=0
	while(n>0):
		j=n%10
		if(i==j):
			c+=1
		n=n//10
	return c