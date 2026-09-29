#1.rotate a list by k elements
"""l=[1,2,3,4,5]
k=2
for i in range(k):
    last=l[-1]
    for j in range(len(l)-1,0,-1):
        l[j]=l[j-1]
    l[0]=last
print(l)
"""
#2.assign all the zeros at the end of the list
"""l=[0,1,2,3,0,4,5]
j=0
for i in range(len(l)):
    if l[i]!=0:
        l[i],l[j]=l[j],l[i]
        j+=1
print(l)"""

