# nthLychrelNumber(n) [20 pts]
# A Lychrel number is a natural number that cannot form a palindrome through the iterative process of 
# repeatedly reversing its digits and adding the resulting numbers. This process is sometimes called the 
# 196-algorithm, after the most famous number associated with the process.
# The first few Lychrel numbers are 196, 295, 394, 493, 592, 689, 691, 788, 790, 879, 887….


def palindrome(n):
	m=str(n)
	if(m==m[::-1]):
		return True
	return False

def nthlychrelnumbers(n):
	# your code goes here
	max_it=25
	res=[]
	i=1
	while(len(res)<n):
		s=str(i)
		num=i
		for j in range(max_it):
			s=s[::-1]
			num=num+int(s)
			if(palindrome(num)):
				break
			s=str(num)
		if(j==max_it-1):
			res.append(i)
		i=i+1
	print(res)
	return(res[n-1])