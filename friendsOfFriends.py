'''
friendsOfFriends(d) [15 pts]
Background: we can create a dictionary mapping people to sets of their friends. For example, we might say:
d = { }
d["jon"] = set(["arya", "tyrion"])
d["tyrion"] = set(["jon", "jaime", "pod"])
d["arya"] = set(["jon"])
d["jaime"] = set(["tyrion", "brienne"])
d["brienne"] = set(["jaime", "pod"])
d["pod"] = set(["tyrion", "brienne", "jaime"])
d["ramsay"] = set()

With this in mind, write the function friendsOfFriends(d) that takes such a dictionary mapping people to sets of friends and returns a new dictionary mapping all the same people to sets of their friends of friends. For example, since Tyrion is a friend of Pod, and Jon is a friend of Tyrion, Jon is a friend-of-friend of Pod. This set should exclude any direct friends, so Jaime does not count as a friend-of-friend of Pod (since he is simply a friend of Pod) despite also being a friend of Tyrion's.

Thus, in this example, friendsOfFriends should return:
{
 'tyrion': {'arya', 'brienne'}, 
 'pod': {'jon'}, 
 'brienne': {'tyrion'}, 
 'arya': {'tyrion'}, 
 'jon': {'pod', 'jaime'}, 
 'jaime': {'pod', 'jon'}, 
 'ramsay': set()
}
'''
def readDict():
    a = {}
    n = int(input())
    for i in range(n):
        s = input().split()
        a[s[0]] = set(s[1:])
    return a

def fof(d,j):
    k=[]
    for i in d[j]:
        if i in d:
            for m in d[i]:
                if m not in d[j] and m not in j:
                    if m not in k:
                        k.append(m)
    return k

def friendsOfFriends(d):
    # your code goes here  
    j={}
    for i in d:
        if i not in j:
            j[i]=fof(d,i)
    return j

   

d = friendsOfFriends(readDict())

for i in sorted(d.keys()):
    print(i, sorted(d[i]))
