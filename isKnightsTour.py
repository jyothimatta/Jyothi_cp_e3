# IsKnightsTour [20 Pts]
# Background:  A "knight's tour in chess is a sequence of 
# legal knight moves such that the knight visits every square 
# exactly once. We can represent a (supposed) knight's tour
#  as an NxN list of the integers from 1 to N2 listing the 
# positions in order that the knight occupied on the tour.  
# If it is a legal knight's tour, then all the numbers from 1
#  to N2 will be included and each move from k to (k+1) will
#  be a legal knight's move. With this in mind, write the 
# function isKnightsTour(board) that takes such a 2d list of 
# integers and returns True if it represents a legal knight's 
# tour and False otherwise. Code for this problem should go in 
# hw5.py and will be autograded!

# To help you undertand how a knight's tour is represented,
# and so you can write your own test cases, here is one example 
# of a successful knight's tour:

# board = [
#           [  1, 60, 39, 34, 31, 18,  9, 64 ],
#           [ 38, 35, 32, 61, 10, 63, 30, 17 ],
#           [ 59,  2, 37, 40, 33, 28, 19,  8 ],
#           [ 36, 49, 42, 27, 62, 11, 16, 29 ],
#           [ 43, 58,  3, 50, 41, 24,  7, 20 ],
#           [ 48, 51, 46, 55, 26, 21, 12, 15 ],
#           [ 57, 44, 53,  4, 23, 14, 25,  6 ],
#           [ 52, 47, 56, 45, 54,  5, 22, 13 ],
#         ]
# assert(isKnightsTour(board)==True)
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
    #r=len(L)
    for i in range(len(L)):
        for j in range(len(L[0])):
            if L[i][j]==n:
                return i,j
    return -1,-1
def isvalidmove(r1,r2,c1,c2):
    
    if(abs(r1-r2)==1 and abs(c1-c2)==2) or (abs(r1-r2)==2 and abs(c1-c2)==1):
        return True
    return False

def isKnightsTour(L):
    # your code goes here
    r=len(L)
    i=1
    while(i<r*r):
        r1,c1=getrowcol(L,i)
        r2,c2=getrowcol(L,i+1)
        if(r1==-1 or r2==-1):
            return False
        i+=1
        if isvalidmove(r1,r2,c1,c2)==False:
            return False
    return True




L = [
            [  1, 60, 39, 34, 31, 18,  9, 64 ],
            [ 38, 35, 32, 61, 10, 63, 30, 17 ],
            [ 59,  2, 37, 40, 33, 28, 19,  8 ],
            [ 36, 49, 42, 27, 62, 11, 16, 29 ],
            [ 43, 58,  3, 50, 41, 24,  7, 20 ],
            [ 48, 51, 46, 55, 26, 21, 12, 15 ],
            [ 57, 44, 53,  4, 23, 14, 25,  6 ],
            [ 52, 47, 56, 45, 54,  5, 22, 13 ],
        ]
assert(isKnightsTour(L)==True)

# You can write your own test cases here...
print("All test cases passed....")