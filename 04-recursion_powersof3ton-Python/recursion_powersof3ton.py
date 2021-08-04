# Recursion-Only powersOf3ToN(n) [15 pts]
# Write the function powersOf3ToN(n) that takes a possibly-negative float or int n, and returns a list of the 
# positive powers of 3 up to and including n. As an example, powersOf3ToN(10.5) returns [1, 3, 9]. If no such powers 
# of 3 exist, you should return the empty list. You may not use loops/iteration in this problem. 

def lists(n,l):
    if n==0:
        return l
    else:
        l.append(n)
        return lists(n-1,l)
def powton(m,a=0,r=[]):
    if 3**a>max(lists(m,[])):
        return r
    else:
        if 3**a in lists(m,[]):
            r.append(3**a)
            return powton(m,a+1,r)
        else:
            return powton(m,a+1,r)
def recursion_powersof3ton(n):
    # your code goes here
    if n<1:
        return None
    # elif n=1:
    #     return [1]
    else:        
        return powton(int(n),0,[])
