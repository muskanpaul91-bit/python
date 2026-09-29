# n =int(input("Enter a number.:-"))
# if n%2 !=0:
#     print("Weird")
# if n%2==0 and n>=2 and n<=5:
#     print("Not Weird")
# if n%2==0 and n>=6 and n<=20:
#     print("Weird")
# if n%2==0 and n>20:
#     print("Not Weird")
        
# n=int(input())
# for i in range (n):
#     print(i**2)

def is_leap(year):
    if year%4==0 or year%400==0:
        return True
    else:
        return False
year = int(input())
print(is_leap(year))

