# Write the function isrectangular(L) that takes a possibly-2d 
# list L and returns True  if it is rectangular, so each row has
#  the same number of elements. Return False otherwise.


def fun_isrectangular(l):
	n=l
	for i in n:
		if len(i)!=len(n[0]):
			return False
	return True



