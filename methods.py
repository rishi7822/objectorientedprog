# # #A class method is a method that is bound to the class and not the object of the class.
# # #They have the access to the state of the class as it takes a class parameter that points to the class and not the object instance.
# # #It can modify a class state that would apply across all the instances of the class. For example, it can modify a class variable that will be applicable to all the instances.
# # # # class MyClass:
# # # # 	def __init__(self, value,any):
# # # # 		self.value = value
# # # # 		self.any=any

# # # # 	def get_value(self):
# # # # 		return self.value*self.any

# # # # # Create an instance of MyClass
# # # # obj = MyClass(10,5)

# # # # # Call the get_value method on the instance
# # # # print(obj.get_value()) # Output: 10


# # # class MyCars:
# # #     def __init__(self,name,model):
# # #         self.name=name
# # #         self.model=model

# # #     def get_name(self):
# # #         return self.name,self.model
    

# # # #create an instance
# # # obj=MyCars("bugatti",6030)

# # # print(obj.get_name())


# # #stATIC METHODS

# # A static method does not receive an implicit first argument. A static method is also a method that is bound to the class and not the object of the class. This method can’t access or modify the class state. It is present in a class because it makes sense for the method to be present in class.


# class MyClass:
#     def __init__(self,value):
#         self.value=value

#     @staticmethod
#     def get_max_value(x,y):
#         return max(x,y)


# #create an instance
# obj=MyClass(20)

# print(MyClass.get_max_value(20,30))
# print(obj.get_max_value(20,30))


#implementation of static method and class method in program

from datetime import date

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

#a class method to create a person by object
    @classmethod
    def fromBirthYear(cls,name,year):
        return cls(name,date.today().year-year)


#a statice method to check if a person is adult or not
    @staticmethod
    def isAdult(age):
        return age > 18
    
Person1 = Person("rishi",20)
Person2= Person.fromBirthYear("rishi",2000)

print(Person1.age)
print(Person2.age)

#print
print(Person.isAdult(25))