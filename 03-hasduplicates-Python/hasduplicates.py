# hasDuplicates(L) [15 pts]
# Write the function hasDuplicates(L) that takes a 2d list L of arbitrary values, and returns True if L 
# contains any duplicate values (that is, 
# if any two values in L are equal to each other), and False otherwise.

import itertools
#num = [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
#print("Original List", num)
#num.sort()
#new_num = list(num for num,_ in itertools.groupby(num))
#print("New List", new_num)
def hasduplicates(L):
    for i in range(len(L)-1):
        for j in range(len(L[i])):
            for h in range(i+1,len(L)):
                if L[i][j] in L[h]:
                    return True
    return False
