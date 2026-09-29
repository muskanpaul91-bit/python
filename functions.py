"""user defined function
using def keyword
def name_of_function():
    code
name_of_function() #function calling """

"""def greeting():   #defining of a function
    print("Hello! How are you")
    
greeting()  #function calling
 
   
def add(a,b):  # a and b are parameters
    print(a+b)
add(9,19)        # passing arguments


def palindrome(n):
    rev=0
    copy=n
    while n!=0:
        rev =rev *10 + n%10
        n=n//10
        
    if copy ==rev:
        print("Palindrome")
    else:
        print("not a palindrome")
    
palindrome(99)

#if you give a value using default argument you always have to gave further values using default arguments

def info(a,b,c,d):
    print(a,b,c,d)
info(2,d=10,b=30,c=23) #default arguments or keywords

#default parameters
def info(nmae,age,id=None):
    print("Recieved")
info("hyn",90)"""

# def strong_number(n):
#     fac=1
#     sum=0
#     copy=n
#     while n>0:
#         a=n%10
#         for i in range(1,a+1):
#             fac=fac*i
#         sum=sum+fac
#         n//=10
#     if sum==copy:
#         print("Strong number.")
#     else:
#         print("not a strong number.")
        
# strong_number(145)


"""# return vs print
def hello():
    return "hii"
print(hello())

def agechecker(n):
  
    if n>=18:
        return True
    else:
        return False
n=int(input("Enter your age:-"))
if agechecker(n):
    print("you can vote")
else:
    print("you can not vote")"""
    
# def numbers(n):
#     if n==101:
#         return "done"
#     print(n)
#     numbers(n+1)
# numbers(1)

