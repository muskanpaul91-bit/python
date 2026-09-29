#for loop
for i in range(0,11, 2):
    print(i)

#revers loop               #start,end,step
for m in range (10,0,-1):
    print(m)

#to remove any data from loop
for i in range (0,11):
    if i != 3:
        print(i)

n=int(input("enter the no."))
for i in range(0,n):
    if i%2 ==0:
        print("even no.")
        print(i)
        

   

#continue
for i in range(5,0,-1):
    if i==3:
        continue
    print(i)
    
for m in range(0,15):
    if m %3==0:
        continue
    print(m)

for i in range(0,40):
    if i % 3==0 or i%5==0 :
     print(i)

# foreach
ages =[12, 99,33,122,88]
for i in ages:
    if i%3==0:
        continue
    print(i)
    
    marks =[66, 10 ,61, 20]
for i in marks:
    print(i**2, end=",")