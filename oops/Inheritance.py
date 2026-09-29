#TYPES OF INHERITANCE
"""1.single inheritance
2.Multiple inheritance
3.Multilevel inheritance
4.hierarchial inheritance
5.hybrid inheritance"""

#1.single inheritance

"""class parent():
    def __init__(self):
        print('This is p constructor')
    def greet(self):
        print("This is parent class")

class child(parent):
    def __init__(self):
        print("This is c constructor")
    def show(self):
        print("This is child class")

obj =child()
obj.greet()
obj.show()
"""
# class Factory:
#     def __init__(self,name,color):
#         self.name=name
#         self.color=color
#     def show(self):
#         print(f" Bag has {self.name} and {self.color} color")
        
# class bata(Factory):
#     def __init__(self,name,zip,pockets):
#         super(). __init__(name,)
#         self.zip=zip
#         self.pockets=pockets



#Multilevel Inheritance
"""One child class becomes parent for another child class"""
#1.
# class A:#super parent class
#     def greet(self):
#         print("This is class A")
# class B(A):#parent class
#     def show(self):
#         print('This is class B')
# class C(B): #child class
#     def display(self):
#         print('This is class C')
# obj=C()
# obj.greet()
# obj.show()
# obj.display()

#2.
# class CEO:
#     def __init__(self):
#         print("This is CEO class")
# class Manager(CEO):
#     def __init__(self):
#         super().__init__()
#         print('This is Manager class')
# class Employee(Manager):
#     def __init__(self):
#         super().__init__()
#         print("This is Employee class")

# obj=Employee()

#Hierarchial inheritance 
#1.
# class parent:
#     def greet(self):
#         print("This is parent class")

# class child1 (parent):
#     pass
# class child2(parent):
#     pass

# obj1=child1()
# obj1.greet()
# obj2=child2()
# obj2.greet()

#2.
class Account:
    def __init__(self,name,balance):
        self.name=name
        self.balance=balance
    
    def details(self):
        print(f"Hello {self.name} you have {self.balance}")
        
        
class Saving(Account):
    def __init__(self,name,balace):
        super().__init__(name,balace)
        print(f"This is saving class constructor {self.name}, {self.balance}")

class Current(Account):
    def __init__(self,name,balance,type):
        super().__init__(name,balance)
        self.type=type
        print(f"This is current class constructor {self.name}, {self.balance}, {self.type}")
        
obj=Current("Kratika",12000,'saving')
        
        