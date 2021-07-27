# isSorted(a) (10 Pts)
# Write the function isSorted(a) that takes a list of numbers and returns True if the list 
# is sorted (either smallest-first or largest-first) and False otherwise. Your function 
# must only consider each value in the list once (so, in terms of big-oh, which we will 
# learn soon, it runs in O(n) time, where n=len(a)), and so in particular you may not sort 
# the list.

def issorted(a):
	n = len(a)
	if n == 1 or n == 0:
		return True
	flag = 1
	for i in range(1, n):
		if (a[i-1] <= a[i]) :
			flag = 1
		else:
			flag = 0
			break
	if flag == 1:
		return True
	for i in range(1,n):
		if (a[i-1]>=a[i]):
			flag = 1
		else:
			flag = 0
			break
	if flag == 0:
		return False
	return True

print(issorted([1, 2, 3, 4, 5]))