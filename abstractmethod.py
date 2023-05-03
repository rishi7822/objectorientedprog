# #abstract method 
# from abc import ABC, abstractclassmethod
# class Myclass:
  
#   @abstractclassmethod

#   def calculate(self,x):
#     pass  #empty body

# #this is a sub class
# class Sub1(Myclass):
#   def calculate(self,x):
#     print('Square Value= ',x*x)

# import math
# class Sub2(Myclass):
#   def calculate(self,x):
#     print("Square root= ",math.sqrt(x))

# class Sub3(Myclass):
#   def calculate(self,x):
#     print("Cube Value= ",x**3)

# #create subclass obj and call it()
# obj1= Sub1()
# obj1.calculate(16)


# #create sub2 call obj and call it
# obj2= Sub2()
# obj2.calculate(16)

# #CRETe sub3 call obj and call it
# obj3 = Sub3()
# obj3.calculate(16)



from abc import *
class Car(ABC):
    def __init__(self, regno):
        self.regno= regno

    def Opentank(self):
        print("Fill the fuel into the tank")
        print("for the car with regno ", self.regno)

    @abstractmethod
    def steering(self):
        pass
    @abstractmethod
    def braking(self):
        pass