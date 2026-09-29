#1.
nums=[1,5,0,3,5]
l=[]
for i in nums :
    if i in l:
        continue
    elif i==0:
        continue
    else:
        l.append(i)
print(len(l))

