"""dictionary is used using {} and pass key:value in square brackets
To add
d={1:10,2:20,3:30}
d[4]=40
To update
d[1]=100
To delete
del d[1]

#Methods 
1.formkeys
print(dict.fromkeys([1,2,3,4],10)) #directly called by class dict and create a dictionary
2.get
d.get(3) #get the value at key 3
3.items
4.pop
pass argument (key)
5.popitem
remove the last item
6.setdefault
7.values
8.update to add two dict
"""
"""#To combine two dict.
d1={1:10,2:20,3:30}
d2={4:40,5:50,6:60}
for i in d2:
    d1[i]=d2[i]
print(d1)

#to combine same keys
d1={1:10,2:20,3:30}
d2={3:40,5:23,6:60}
for i in d2:
    if i in d1.keys():
        d1[i]=d1[i]+d2[i]
    else:
     d1[i]=d2[i]
print(d1)

"""

#count the frequency of a no. in a list
l=[3,2,2,2,2]
d={}
for i in l:
    if i in d:
        d[i]=d[i]+1
    else:
        d[i]=1
for i in d.values():
    if i%2 !=0:
        print("not pair")
        break
else:
    print("pair")
    

