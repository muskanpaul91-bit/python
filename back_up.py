"""List-> []
1. can have multiples data tyoes {int,float,str,bool}
2.can have duplicates values
3. list has a unique thing that is indexing
*indexing starts fron 0 and  goes to len-1
4.list is mutable
"""

l=[1,2,3,4,5]
# print(l[3:0:-1])

#iterating on loop
# direct loop-> print values of the list
#indexing loop-> print index of values

"""Methods of list
1.append -> add element at last
2.extend  ->combine more than one elements or list 
3.insert   ->add element at specific index
4.pop      -> if index not given remove last element
5.remove   ->remove values
6.clear    -> clear all values and give empty list
"""



#rotate a elements by k elements
def rotate(l,k):
    if k==len(l):
        return l
    else:
        for i in range(k):
            last=l[-1]
            for j in range(len(l)-1,0,-1):
                l[j]=l[j-1]
            l[0]=last
        return l
print(rotate([10,20,30,40,50],2))

    
