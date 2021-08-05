# getallPermutations(str) [20 pts]
# Write an efficient program to print all permutations of a given String. For example, if given input is "abc" then 
# your program should print all 6 permutations e.g. [('a', 'b', 'c'), ('a', 'c', 'b'), ('b', 'a', 'c'), ('b', 'c', 'a'), ('c', 'a', 'b'), ('c', 'b', 'a')]


def getallpermutations(s):
	answer=" "
	if (len(s) == 0):
		print(answer, end = "  ")
		return
	 
	for i in range(len(s)):
		ch = s[i]
		left_substr = s[0:i]
		right_substr = s[i + 1:]
		rest = left_substr + right_substr
		getallpermutations(answer + ch)