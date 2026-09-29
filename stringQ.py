"""m=input("Enter your message.:-")
print(m[::-1])
print(len(m))
print(m.upper())  #uppercase
print(m.lower()) #lowercase"""

"""m="ShEry"
lower=""
upper=""
for i in  m:
    if i.islower():
        lower+=i
    else:
        upper+=i
print(lower+upper)

n="m2@9op=iov./?"
alpha=0
digit=0
spe=0
for i in n:
    if i.isalpha():
        alpha+=1
    elif i.isdigit():
        digit+=1
    else:
        spe+=1
print(alpha)
print(digit)
print(spe)"""

"""#compare two strings without using inbuild functions
str1="gello"
str2="Hello"
if len(str1)==len(str2):
    for i in range (len(str1)):
        if str1[i]!=str2[i]:
            print("not equal.")
            break
    else:
        print("equal")
else:
    print("not equal")"""
   
"""def count_vowels(): 
    vowels ="aeiouAEIOU"
    count=0
    s=input("Enter your message:-")
    for i in s:
        if i in "aeiouAEIOU": #vowels
            count+=1
    return f"Totals count of vowels are:-{count}"
#count_vowels(input("Enter you message:"))
count_vowels()
print(count_vowels)"""

"""s="Muskan"
print(s[::-1])"""

"""s="hello"
m=""
for i in s[::-1]:
    m+=i
    #print(i,end="")
    #print(i)
print(m)"""

"""def pallindrome():
    s=input()
    copy=s
    if s[::-1]==copy:
        print("Pallindrome")
    else:
        print("Not a pallindrome")
pallindrome()"""

"""s="hello"
vowel,con=0,0

for i in s:
    if i in "aeiouAEIOU":
        vowel+=1
    else:
        con+=1
print(f"Total count of vowel is {vowel} and consonent is {con}")"""

n=123
while n>0:
    b=n%10
    print(n)

