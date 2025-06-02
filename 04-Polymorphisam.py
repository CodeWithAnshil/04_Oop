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
   
class ElectricCar(Car):
     def __init__(self,brand,model,battery_size):
         super().__init__(brand,model)
         self.__battery_size=battery_size

     def fule_type(self):
         return "Electric"


my_car=Car("Toyota","Corolla")
Car("Rang Rover","Defendar")
my_electriCar=ElectricCar("Tesla","model S","88kwh")

print(my_car.get_brand())
print(my_car.get_model())
print(my_car.full_name())
print(my_car.fule_type())
print("----------------------------------")
print(my_electriCar.fule_type())
print(my_electriCar.get_brand())
print(my_electriCar.get_model())
print(my_electriCar.full_name())
print(ElectricCar.total_car)
# print(my_car.__brand)  it will show AttributeError : 'Car' object has no attribute '__brand'
