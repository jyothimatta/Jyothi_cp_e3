# nthPronicNumber(n) [20 pts]
# Write the function nthPronicNumber that takes a non-negative int n and returns the nth Pronic 
# Number. Pronic number is a number which is the product of two consecutive integers, that is, a 
# number n is a product of x and (x+1).
import math
 
# function to check
# Pronic Number
def checkPronic (x) :
 
	i = 0
	while ( i <= (int)(math.sqrt(x)) ) :
		 
		# Checking Pronic Number
		# by multiplying consecutive
		# numbers
		if ( x == i * (i + 1)) :
			return True
		i = i + 1
 
	return False
def nthpronicnumber(n):
	# Your code goes here
	i = 0
	c=0
	while(c <= n):
		if (checkPronic(i)):
			c+=1
			#print(count)
		i=i+1
	return i-1