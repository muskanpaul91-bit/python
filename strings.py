"""#Indexing
a="hello"
#positive indexing
print(a[1])
#negative indexing
print(a[-1])"""

#slicing
"""s="Hello how are you"
a="A"
print(s[14:])
print(ord(a)) #unicodes"""

a=input("Give me a character:")
b=ord(a)
if b>=65 and b<=95:
    print("its is an alphabet")
elif b>=97 and b<=122:
    print("Its an alphabet")
else:
    print("Not  an alphabet")
