"""problem is what if humme nahi pata kitna parameters hone vale hai
to solve this we will use -> args
->args->*variable  name {variable name can have any name}
->args accept values in tuple formate

    
def add(*a):
    print(type(a))
    sum=0
    for i in a:
        sum+=i
    print(sum)
add(10,20,30)"""

"""def add(a,b): #positional perameter
    print(a,b)
add(10,20)

def polio(name,age,pin):
    print(name,age,pin)
polio(name="Shayam",age=22,pin=2345) #keywords arguments
"""
# kwarrgs->keywordarguments
#denoted by->**variable name
#accept values  in the form of dictonary
#here the parameters are keys and arguments are values
"""def polio(**variable):
    print(type(variable))
    print(variable)
polio(name="Suresh",age=22,school='dps')
"""

"""Lambda function ->jab  ek function ek line mai aa jaye
lambda converts a variable into function
a,b:a+b-> agar a,b variable mai kuch value aayegi toh hi a+b chalega varna nahi chalega"""
add= lambda a,b:a+b
print(add(10,20))
