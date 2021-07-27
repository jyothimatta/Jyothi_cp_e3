# median(a) (10 pts)
# Write the non-destructive function median(a) that takes a list of ints or floats and returns the median value, 
# which is the value of the middle element, or the average of the two middle elements if there is no single middle 
# element. If the list is empty, return None.

def median(a):
	l=sorted(a)
	n=len(l)
	if(n==0):
		return None
	if(n%2==0):
		median=(l[n//2]+l[(n//2)-1])/2
		return median
	else:
		median=l[n//2]
		return median
