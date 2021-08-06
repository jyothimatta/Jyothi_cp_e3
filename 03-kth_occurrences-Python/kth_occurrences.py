# Given a string str and an integer K, the task is to find the K-th most 
# frequent character in the string. If there are multiple characters that 
# can account as K-th the most frequent character then, print any one of them.



def fun_kth_occurrences(s, n):
	freq_dict = dict()
	for i in s.lower():
		if i not in freq_dict:
			freq_dict[i] = 1
		else:
			freq_dict[i] += 1

	freq_list = sorted(set(freq_dict.values()), reverse=True)
   
	if n > len(freq_list):
		return 'h'

	for key, value in freq_dict.items():
		if value == freq_list[n-1]:
			return key


