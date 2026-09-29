#count the no. of digits in a number
"""n=1234
count=0
while n>0:
    b=n%10
    count+=1
    n//=10
print(count)"""

"""def count(n):
    count=0
    while n>0:
        b=n%10
        count+=1
        n//=10
    print(count)
count(256)"""

"""def count(n): # return convert function into mini variable and we have to use print
    count=0
    while n>0:
        b=n%10
        count+=1
        n//=10
    return count
print(count(256))"""

#find the sum of digits of a number
"""n=123
sum=0
while n>0:
    b=n%10
    sum+=b
    n//=10
print(sum)
"""
"""def sum(n:int): anotation
    n=123
    sum=0
    while n>0:
         b=n%10
         sum+=b
         n//=10
    return sum
print(sum(123))"""

"""#armstrong number
n=int(input())
copy=n
order =len(str(n))
sum=0
while n>0:
    sum=sum+(n%10)**order
    n//=10
if sum==copy:
    print(f"The number {copy} is an armstrong number.")
else:
    print(f"The number {copy} is not an armstrong number.")"""
    
#n=1
# while (n<=10):
#     print(n)
#     n+=1

# while (n<=20):
#     if n%2==0:
#         print(n)
#     n+=1

# n=10
# while (n>=0):
#     print(n)
#     n-=1

# n=int(input("enter no."))
# sum=0
# while(n>0):
#     sum+=n
#     n-=1
# print(sum)


