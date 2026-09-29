# name= input("Enter your name:")
# age= int(input("Enter your age:"))
# print(f"your name is {name} and age is{age} ")  #formated string

#operators
#Arithmatic (+.-,/,*,//,**,%), {//(floor division), gives integer value after division}                                
#assignment(=)
#comparion 

p =float(input("enter principle rate:"))
r =float(input("tell your rate of interest:"))
t= float(input("tell your time in years:"))
si= (p*r*t)/100
com=p*((1+(r/100))**t)
print(f"Your ompound interest will be :-{com-p}")


