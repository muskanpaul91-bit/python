#Bubble sort 
# sort the largest element in the last first..continue
"""a=[56,12,89,23,56,90,13]
for j in range (len(a)-1):
    for i in range(0,len(a)-1-j):
        if a[i]>a[i+1]:
         a[i],a[i+1]=a[i+1],a[i]
print(a)

a=[9,34,56,78,90,78,65,888,990,234,56,76,45]
large=a[0]
index=0
for i in range(1,len(a)):
    if large <a[i]:
        large=a[i]
        index=i
print(large,index)
"""
#largest no. and second no.
"""l=[1,16,17,23,2,89,45]
largest=l[0]
s=l[0]
#index=0
for i in l:
    if i>largest:
        s=largest
        largest=i
    elif i>s:
        s=i
print(largest)
print(s)"""

#
#largest no. and second no. using indexing
# l=[1,16,17,23,2,89,45]
# largest=l[0]
# s=l[0]
# indexl=l[0]
# indexs=l[0]
# for i in range(1,len(l)):
#     if l[i]>largest:
#         s=largest
#         largest=l[i]
#         indexs=indexl
#         indexl=i
#     elif l[i]>s:
#         s=l[i]
#         indexs=i
# print(largest,indexl)
# print(s,indexs)

#smallest
# l=[1,5,16,17,23,2,89,45]
# smallest=12
# s_2=12
# #index=0
# for i in l:
#     if i<smallest:
#         s_2=smallest
#         smallest=i
#     elif i<s_2:
#         s_2=i
# print(smallest)
# print(s_2)
# #for finding smallest ->you will pick greater ValueError

#check if list is shorted or not
"""l=[1,2,3,4,5,6,7]
for i in range(len(l)-1):
    if l[i]>l[i+1]:
        print("list is not sorted")
        break
else:
    print("list is sorted ")
"""
#pallindrome list
#1.silicing
# l=[1,2,3,2,1]
# a=l[::-1]
# if l==a:
#     print("list is pallindrome")
# else:
#     print("list is not sorted")
    
# #2.
# l=[1,2,3,2,1]
# for i in range (len(l)//2):
#     if l[i]!=l[len(l)-1-i]:
#         print("List is not palindrome")
#         break
# else:
#     print("List is pallindrome")
    
# #3.






# #
# n=int(input("enter total no. of elements you want to add:-"))
# l=[]
# sum=0
# for i in range(n):
#     inputs =int(input(f"Enter the elements at index {i}:"))
#     sum+=inputs
#     l.append(inputs)
# print(l)
# print(sum)
        
        
l = sum(list(map(int,input("enter elements:").split())))
print(l)
""" map-> (data type,input)
split-> seperates all the values and digits
list-> converts the value in the form of list data structure

sabse pehle inputs accept-> har input split 
hoga-> inputs will be type casted in the form 
of int-> we stored all the int values inside a list"""