#Eligible for driving lisence
age = int(input("Enter your age :-"))
if( age >= 18):
    print("Eligible for driving lisence")

#temperature qu.
temp = int(input("Enter the temperature"))
if(temp>30):
    print("Trun on the air conditioner")
elif(temp<10):   
     print("Trun on the heater")
else:
     print("The temperature is comfoetable")    
     
 #Ticket cost
age = int(input("Enter age :-"))
if (age<12):
    print("Ticket cost 150")
elif(age>=60):
    print("Ticket cost 200")
else:
     print("Ticket cost 300")
     
 #Weather decision
A = "Raining"
B = "Snowing"
word =input("Enter A for raining or B for snowing:-")
if( word == "A"):
    print("take an umbrella")
elif( word == "B"):
    print("wear boots") 
else:
    print("Enjoy your day")       
    
        