# Background:  in Chess, a King can move from any square to
# any adjacent square.  A King’s Tour is a series of legal King
# moves so that every square is visited exactly once. 
# We can represent a Kings Tour in a 2d list where the 
# numbers represent the order the squares are visited, going 
# from 1 to N2.  For example, consider these 2d lists:

#    [ [  3, 2, 1 ],    	[ [  1, 2, 3 ],  	[ [ 3, 2, 1 ],
#  	[  6, 4, 9 ],      	[  7, 4, 8 ],    	[ 6, 4, 0 ],
#  	[  5, 7, 8 ] ]     	[  6, 5, 9 ] ]   	[ 5, 7, 8 ] ]

# The first is a legal Kings Tour but the second is not, 
# because there is no way to legally move from the 7 to the 8, 
# and the third is not, because it contains a 0 which is out
#  of range.  With this in mind, write the function 
# isKingsTour(board) that takes a 2d list of integers, 
# which you may assume is NxN for some N>0, and 
# returns True if it represents a legal Kings Tour 
# and False otherwise.
def read2DArray():
    a = []
    l = int(input())
    for i in range(l):
        s = input().split(" ")
        t = []
        for j in range(len(s)):
            t.append(int(s[j]))
        a.append(t)
    return a
def getrowcol(L,n):
    r=len(L)
    for i in range(r):
        for j in range(r):
            if L[i][j]==n:
                return i,j
    return -1,-1
def isvalidmove(r1,c1,r2,c2):
    if(r1-r2>1 or r1-r2<-1):
        return False
    if(c1-c2>1 or c1-c2<-1):
        return False
    return True

def isKingsTour(L):
    # your code goes here
    r=len(L)
    for i in range(r):
        for j in range(r):
            if L[i][j]==0:
                return False
    i=1
    while(i<r*r):
        r1,c1=getrowcol(L,i)
        r2,c2=getrowcol(L,i+1)
        if(r1==-1 or r2==-1):
            return False
        if isvalidmove(r1,c1,r2,c2)==False:
            return False
        i=i+1
    return True
