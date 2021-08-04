# longestDigitRun(n) [20 pts]
# Write the function longestDigitRun(n) that takes a possibly-negative int value n and returns 
# the digit that has the longest consecutive 
# run, or the smallest such digit if there is a tie. So, longestDigitRun(117773732) returns 7 (
# because there is a run of 3 consecutive 7's), 
# as does longestDigitRun(-677886).
def longestdigitrun(x):
	# Your code goes here
	x=abs(x)
	lon=10
	c=1
	if(x>=0 and x<=9):
		return x
	for i in range(9,-1,-1):
		count=maxcount(x,i)
		if(c<=count):
			c=count
			lon=i
	return lon
def maxcount(x,j):
	count=0
	f=1
	while(x):
		if(x%10==j):
			if(f==1):
				count+=1
				x//=10
			else:
				count=1
				f=1
				x//=10
		else:
			f=0
			x//=10
	return count
