# trianglearea(s1, s2, s3)[5pts]
# Write the function trianglearea(s1, s2, s3) that takes 3 floats/ints and returns the area of the
# triangle that has those lengths of its side. If no such triangle exists, return 0. Hint: you
# will probably wish to use Heron's Formula.

import math
def trianglearea(s1, s2, s3):
	if (s1 < 0 or s2 < 0 or s3 < 0 or (s1+s2 <= s3) or (s1+s3 <=s2) or (s2+s3 <=s1) ):
		print('Not a valid triangle')
		return
	s=(s1+s2+s3)/2
	Area=((s)*(s-s1)*(s-s2)*(s-s3))**0.5
	return Area
