"""Data structures:-
1.list
2.tuple
3.set
4.dict

1.list-for creating list you have to use square brackets []
l=[12,23,45]

#special powers:-
->Hetrogenous nature: it can store any kind of data types at once
e.g- l=[23,"hello",23.90,True,Print()]
->Ordered: Every element in list has a designated position
->Mutable nature: you can change anything inside the list at any point of time
->Dublicates: You can store dublicate values in list"""

"""# reading a list 
a=[10,20,29,28]
print(a)
print(a[0])

#updating a list
a[2]=30
print(a)

#Delete
del a[-1]
print(a)"""

"""#Creating loops on list :
a=[10,20,30,40,"hello",50]
#based on values
for i in a:
    print(i)

#based on index
for i in range(0,len(a)):
    print(i)

#this loop can access your index as well as your values and it gives more control over your list 
for i in range(0,len(a)):
    print(a[i])
    """
#Methods
#1.append
"""a=[2,3,4,50]
a.append(5)
print(5)

l=[]
for i in range(10,51,10):
    l.append(1)
print(l)"""

#2.insert
"""a=[1,2,3,4]
a.insert(2,30)
       #(index no.,value to add)
print(a)"""

#3.clear
"""a=[1,2,3,4]
a.clear() #remove all values from list
print(a)"""

#4.pop {uses index number}
"""a=[1,2,3,4]
a.pop(0) #to delete at specific position
saved =a.pop(1)
print(a)"""

#5.remove {uses values }
"""a=[1,2,3,4]
a.remove(1)
print(a)"""

#QUESTIONS OF LIST
"""you can use eval function 
a=eval(input())"""
#1.
"""n=int(input("Enter the no. of elements you want to add:-"))
l=[]
while n>0:
    #m=int(input("Enter the no.:"))
    l.append(int(input("Enter the no.:")))
    n-=1
print("Your list is:-",l)
"""
#2.
"""n=[10,20,30,40,50]
l=[]
for i in range(len(n)-1,-1,-1):
    l.append(n[i])
print(l)              
"""
"""a=[10,20,30]
z=len(a)-1
for i in range (len(a)//2):
    a[i],a[z]=a[z],a[i]
    z-=1
print(a)
"""
#3.
"""a=[1,2,-3,4,-5,-6]
for i in a:
    if i>=0:
        print(i)
for i in a:
    if i<0:
        print(i)"""

