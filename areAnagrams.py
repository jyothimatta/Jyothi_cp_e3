# areAnagrams(s1, s2)
# Write the function areAnagrams(s1, s2) that takes two strings, 
# s1 and s2, that you may assume contain only upper and/or 
# lower case letters, and returns True if the strings are 
# anagrams, and False otherwise. Two strings are anagrams 
# if each can be reordered into the other. Treat "a" and "A"
# as the same letters (so "Aba" and "BAA" are anagrams). 
# You may not use sort() or sorted() or any other list-based
# functions or approaches. Hint: you may use s.count(), 
# which could be quite handy here.
# Hint: The time complexity can be achieved in Linear.

def areAnagrams(s1, s2):
    # Your code goes here...
    d=''
    
    s1=s1.upper()
    for i in s1:
        if i in s2:
            d+=1
        else:
            d=1
    for i in s2:
        if i in s1:
            d-=1
            if d==0:
                del d
        else:
            d=0
    state=(len(s2)==len(s1))
    if state:
        return True
    else:
        
        return False


# write your test cases here...