# Write the function nearestOdd(n) that takes an float n, 
# and returns as an int value the nearest odd number to n. 
# In the case of a tie, return the smaller odd value. 
# Note that the result must be an int, so nearestOdd(13.0) is the int 13, and not the float 13.0.


def fun_nearestodd(n):
	if type(n) == int:  
		if n % 2 == 0:
			return n - 1
		else:
			return n
	else:  # case of a float
		temp = int(n)  # the truncated integer of n
		up_sub = abs(temp + 1 - n)
		down_sub = abs(temp - 1 - n)
		if temp % 2 != 0:  # if the truncated integer itself is an odd
			return temp
		else:  # if the truncated int is an even
			if up_sub < down_sub:
				return temp + 1
			else:
				return temp - 1
	


