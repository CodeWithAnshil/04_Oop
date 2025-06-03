class Car:
   total_car=0
   def __init__(self,brand,model):
       self.__brand=brand
       self.__model=model
       Car.total_car+=1
   def full_name(self):
       return f"{self.__brand} {self.__model}"
              
   def get_brand(self):
       return self.__brand
   def get_model(self):
       return self.__model
   def fule_type(self):
         return "Disal or Petrol"
     #  define a method inside a class that does not access or modify the instance (self) or class (cls).
   @staticmethod
   def general_info():
        return "Cars run on petrol, diesel, or electricity."
   
class ElectricCar(Car):
     total_car=0
     def __init__(self,brand,model,battery_size):
         super().__init__(brand,model)
         self.__battery_size=battery_size
         ElectricCar.total_car+=1

     def fule_type(self):
         return "Electric"
    
   
my_car=Car("Toyota","Corolla")
Car("Rang Rover","Defendar")
my_electriCar=ElectricCar("Tesla","model S","88kwh")


print(Car.general_info())

