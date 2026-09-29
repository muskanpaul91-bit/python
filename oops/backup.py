"""class Factory:
    a=12
    def listen(self):
        print("hiii")
        
print(Factory.a)
Factory.listen()

obj= Factory() #creating object
print(obj.a)  #accessing attributes by object
obj.listen() #accessing methods by object

# When we use objects to call  any method inside class we always send location of my object
"""
#constructor or initilizer

#FIRST USE OF CONSTRUCTOR
# class Factory:
#     def __init__(self): #constructor function is called whenever a new object is created and self will target location of your objects
#         print("How are you!!")
#     print("This is P23 batch")

# a=Factory()
# b=Factory()
# c=Factory()

#SECOND USE OF CONSTRUCTOR
# class Factory:
#     def __init__(self,zips,pockets,material):
#         self.zips=zips
#         self.pockets=pockets
#         self.material=material
    
#     def details(self):
#         print(self.zips)
#         print(self.pockets)
#         print(self.material)
        
# reebok=Factory(2,2,'Leather')

# campus=Factory(4,2,'Plastic')

# reebok.details()
# print(campus.material)

# class Registration:
#     age=18 #class attribute
#     name="muskan"
#     email="muskan@gmail.com"
#     age=19
#     number=5346674878
    
#     def __init__(self,name,email,age,number):
#         if age >= Registration.age:
#             self.name=name  #object attribute
#             self.email=email
#             self.age=age
#             self.number=number
#         else:
#             print("You can not register you are under age..")
#             return
       
#     def details(self):     #object method-> capture the location of the object
#         print(self.name)
#         print(self.email)
#         print(self.age)
#         print(self.number)
      
#     @classmethod  
#     def dummy_details(cls): #  class method, self or cls targeting class, it will always access location of class
#         print(cls.name)
#         print(cls.email)
#         print(cls.age)
#         print(cls.number)
    
#     @staticmethod   
#     def college_details(): #this method wilol not target any location
#         print("Welcome to college"\
#         " Hii..")   
        
        
            
# obj=Registration('Muskan',"muskanpaul@gmail.com",18,9098076914)    
# obj.details()   
# obj.college_details()

#Inheritance
#one class attributes and methods can be accessed by another class this things is known as inheritance

# class Bhopla_Factory:
#     reg_num= 12345678
#     def __init__(self,color,size,type):
#         self.color=color
#         self.size=size
#         self.type=type
        
#     def details(self):
#         print("Your shoes details are:-")
#         print(self.color)
#         print(self.size)
#         print(self.type)
        
# class Indore_Factory(Bhopla_Factory):
#     def __int__(self,color,size, type, price):
#         super().__init__(color,size,type)
#         self.price=price

# class Ujjain_Factory(Indore_Factory):
#     def __init__(self, color, size, type, price):
#         super().__init__(color, size, type, price)
        
# shoe=Ujjain_Factory("red",9,'sneaker',1000)


#multiple inheritance

# class Animal:
#     def __init__(self,name):
#         self.name=name
        
#     def details(self):
#         print(self.name)

# class Human:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
        
#     def speak(self):
#         print('Hello human you speak')

# class Robot(Animal,Human):
#     def __init__(self,name,age):
#         Human.__init__(self,name,age)
        
# obj=Robot('alpha',2)

#Hierarchical inheritance -> one parent and two or more child
# class Animal:
#     pass
# class Human(Animal):
#     pass
# class Robot(Animal):
#     pass

#Hybrid -> combination of any type of inheritance


#Polymorphishm

"""class Animal:
    name="Lion"
    def __init__(self,name,age):
        self.name=name
        self.age=age
        
    def details(self):
        print("The details are:-")
        print(self.name)
        print(self.age)
        
class Human:
    name ="harsh"
    
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
        
    def details(self):
        print(self.name)
        print(self.age)
        print(self.gender)
        
obj1 =Animal("tiger",7)
obj2=Human("Chintu",5,"Male")
obj1.details()
obj2.details()
    

"""
"""#METHOD OVERRIDING
class Bhopla_Factory:
    reg_num= 12345678
    def __init__(self,color,size,type):
        self.color=color
        self.size=size
        self.type=type
        
    def details(self):
        print("Your shoes details are:-")
        print(self.color)
        print(self.size)
        print(self.type)
        
class Indore_Factory(Bhopla_Factory):
    def __int__ (self,color,size, type, price):
        super().__init__(color,size,type)
        self.price=price
    
    def details(self):
        print(super().details())
        print(self.price)
        
obj=Indore_Factory('Blue',7,'sneaker',1000)
obj.details() #thid obj can now only called one method that is of Indore_Factory it can not call Bhopal_factory detail method and this thing is called function overridding

#METHOD OVERLOADING
class Animal:
    def hello(self,a):
        pass
    def hello(self,a,b):
        pass
obj=Animal()
obj.hello(12,45)
#same name methods inside single class but with different parameters this thing is known as method overloading but it is not availabke in python

"""

#ENCAPSULATION
#protecting the methods and attributes is known as encapsulation
#access modifier

"""class Animal:
    a=12 #public 
    _b=24 #protected
    __c=88 #private
    
    def hello(self): #public method
        print("hii")
    def _hello2(self):#protected
        print("hello")
    @classmethod
    def __hello3(self): #private
        print("hii")"""
        
#ABSTRACTION
from abc import ABC, abstractmethod

class person(ABC):
    @abstractmethod
    def info():
        pass
    @abstractmethod
    def register():
        pass

class Teacher(person):
    def info():
        pass
    def register():
        pass
class Student(person):
    def info():
        pass
    def register():
        pass
    
obj=Teacher