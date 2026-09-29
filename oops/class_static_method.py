#class method
# class Animal:
#     name='dog'
#     @classmethod
#     def change(cls,new): #instance can never change your class atributes
#         cls.name=new
#         print(cls.name)
# cheeta = Animal()
# cheeta.change('cat')
# print(Animal.name)

#static method
class sharmavishnu:
    @staticmethod #independent of object
    def menu():
        print('Paneer kulche')
        print('Paneer tikka')
        print('Paneer cheese sandwich')
        print('Cold coffee')
new_market=sharmavishnu()
new_market.menu()
        