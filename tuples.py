"""Tuples
1.tuples are ordered
2.tuples can have duplicacy
3.it is heterogenous
4.are immutable

a=10,20 # by default it becomes tuple
t=() #empty tuple

t=(1,2,3,4,5)
Direct loop
for i in t:
    print(t) #print values
Index loop
for i in range(len(t)):
    print(i,t[i])
    
#enumerate
for index, value in enumerate(t):
    print(index,value)

"""
t=(1,2,3,4,4,6,5)
#METHODS IN TUPLES
#1.count()
print(t.count(4)) # we can count occurence of any elements in tuple
#2.index()
print(t.index(4)) #print the index of element, first occurance index no.

#membership operator
print(3 in t) # if member of tuple print True else False
print(7 in t)

#tuple unpacking 
a,b,c,d,e,f,g=t # store elements in variables 
print(g)
#tuple packing
a=1,2,3

#Star expression(*)
t=(1,2,3,4,5)
#a, *b=t  # if we use * before variable then the rest of the elements get stored in variable in the form of list
#print(a,b)
#a,*b,c=t #middle value extraction

a,*_,c=t #to skip elements
print(a,c)

#to merge tuple do concadination
t=[1,2]
r=[3,4]
print(t+r)
